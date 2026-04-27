import os
import sys
import json
import uuid
from datetime import datetime

# Ensure project root is importable
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import app

def report_case(scenario, action, expected, actual, passed):
    status = "PASS" if passed else "FAIL"
    print(f"__TEST_RESULT__||{scenario}||{action}||{expected}||{actual}||{status}")

# 1. Setup credentials
CRED_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "user_id_password.json")
with open(CRED_FILE, "r", encoding="utf-8") as f:
    creds = json.load(f)
# Use Premithiews as the test user
admin = next((c for c in creds if c.get('username') == 'Premithiews' or c.get('user_id') == 'Premithiews'), creds[0])

# 2. Test Data
# A 1km x 1km square in Delhi area
base_poly = {
    "type": "Polygon",
    "coordinates": [[[77.100, 28.600], [77.110, 28.600], [77.110, 28.610], [77.100, 28.610], [77.100, 28.600]]]
}
# An overlapping square
overlap_poly = {
    "type": "Polygon",
    "coordinates": [[[77.105, 28.605], [77.115, 28.605], [77.115, 28.615], [77.105, 28.615], [77.105, 28.605]]]
}
# Invalid: Too few points
bad_poly = {
    "type": "Polygon",
    "coordinates": [[[77.100, 28.600], [77.110, 28.600]]]
}

base_record_id = None

with app.test_client() as client:
    print("--- STARTING ADVANCED GIS SUITE ---")
    
    # STEP 1: LOGIN
    r_login = client.post('/api/login', json={"username": admin.get('username') or admin.get('user_id'), "password": admin.get('password')})
    report_case("Auth", "Admin Login", "200", r_login.status_code, r_login.status_code == 200)

    # STEP 2: INSERT BASE RECORD
    print("\nInserting Base Parcel...")
    base_data = {
        "khasra_no": "TEST-BASE-001", "khata_no": "KH-99",
        "location": {"state": "Delhi", "district": "New Delhi", "village": "Chanakyapuri"},
        "geometry": base_poly, "land_use": "Institutional", "owner_name": "Initial Owner"
    }
    r_base = client.post('/api/records', json=base_data)
    if r_base.status_code == 201:
        base_record_id = r_base.get_json().get('record', {}).get('_id')
    report_case("Insertion", "Insert Base Parcel", "201", r_base.status_code, r_base.status_code == 201)

    # STEP 3: TEST OVERLAP DETECTION
    if base_record_id:
        print("\nTesting Overlap Detection (should be blocked)...")
        overlap_data = base_data.copy()
        overlap_data["khasra_no"] = "TEST-OVERLAP-ERR"
        overlap_data["geometry"] = overlap_poly
        r_overlap = client.post('/api/records', json=overlap_data)
        report_case("Security", "Detect Parcel Overlap", "409", r_overlap.status_code, r_overlap.status_code == 409)

    # STEP 4: TEST GEOMETRY VALIDATION
    print("\nTesting Bad Geometry (should be blocked)...")
    bad_data = base_data.copy()
    bad_data["khasra_no"] = "TEST-BAD-GEOM"
    bad_data["geometry"] = bad_poly
    r_bad = client.post('/api/records', json=bad_data)
    report_case("Security", "Validate Geometry", "400", r_bad.status_code, r_bad.status_code == 400)

    # STEP 5: TEST OWNERSHIP MUTATION
    if base_record_id:
        print("\nTesting Ownership Mutation (Sale Deed)...")
        mutation_data = {
            "mutation": True,
            "new_owner_name": "Purchaser Name",
            "mutation_type": "Sale Deed",
            "new_share_pct": 100
        }
        r_mut = client.put(f'/api/records/{base_record_id}', json=mutation_data)
        report_case("Logic", "Perform Mutation", "200", r_mut.status_code, r_mut.status_code == 200)

    # STEP 6: CLEANUP
    if base_record_id:
        print("\nCleaning up test data...")
        r_del = client.delete(f'/api/records/{base_record_id}')
        report_case("Cleanup", "Delete Base Parcel", "200", r_del.status_code, r_del.status_code == 200)

    print("\n--- ADVANCED GIS SUITE COMPLETE ---")
