r"""
robust_role_test.py - Improved Role-Based Access Testing
Follows the user's logic:
1. Scan user_id_password.json to identify accounts.
2. Verify roles via API.
3. Dynamically create an Admin if none is found.
4. Test hierarchy: SuperAdmin > Admin > Officer.
5. Automatic cleanup.
"""
import os
import sys
import json
import uuid

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app
from core import load_users

CRED_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "user_id_password.json")

def report_case(scenario, action, expected, actual, passed):
    status = "PASS" if passed else "FAIL"
    print(f"__TEST_RESULT__||{scenario}||{action}||{expected}||{actual}||{status}")

def run_tests():
    # 1. Load Credentials
    if not os.path.exists(CRED_FILE):
        print(f"Error: {CRED_FILE} not found.")
        return

    with open(CRED_FILE, "r", encoding="utf-8") as f:
        creds = json.load(f)

    super_admin_cred = None
    existing_admin_cred = None
    
    with app.test_client() as client:
        print("--- PHASE 1: Account Discovery ---")
        for entry in creds:
            uname = entry.get("username") or entry.get("user_id")
            pwd = entry.get("password")
            
            # Try login
            print(f"Attempting login for: {uname}")
            resp = client.post("/api/login", json={"username": uname, "password": pwd})
            if resp.status_code == 200:
                # Check role
                info = client.get("/api/session-info").get_json()
                role = (info.get("role") or "").lower()
                print(f"  Success! Discovered: {uname} is {role}")
                
                if role == "superadmin" and not super_admin_cred:
                    super_admin_cred = {"username": uname, "password": pwd}
                elif role == "admin" and not existing_admin_cred:
                    existing_admin_cred = {"username": uname, "password": pwd}
                
                client.post("/api/logout")
            else:
                err_msg = "Unknown error"
                try:
                    err_msg = resp.get_json().get('error', 'No error msg')
                except: pass
                print(f"  Failed login for {uname}: {resp.status_code} - {err_msg}")

        if not super_admin_cred:
            print("Error: No SuperAdmin account found in user_id_password.json")
            return

        # 2. Dynamic Provisioning
        print("\n--- PHASE 2: Dynamic Provisioning ---")
        client.post("/api/login", json=super_admin_cred)
        
        temp_admin_uname = f"tmp_admin_{uuid.uuid4().hex[:4]}"
        temp_admin_pwd = "password123"
        temp_admin_id = None
        
        if not existing_admin_cred:
            print(f"No Admin found. Creating temporary Admin: {temp_admin_uname}")
            r_create = client.post("/api/users", json={
                "username": temp_admin_uname,
                "password": temp_admin_pwd,
                "full_name": "Temporary Test Admin",
                "role": "admin"
            })
            if r_create.status_code in (200, 201):
                temp_admin_id = r_create.get_json().get("user", {}).get("user_id")
                existing_admin_cred = {"username": temp_admin_uname, "password": temp_admin_pwd}
                report_case("Discovery", "Create temp Admin", "201", r_create.status_code, True)
        else:
            print(f"Using existing Admin: {existing_admin_cred['username']}")

        # Create a temp Officer for the Admin to manage
        temp_off_uname = f"tmp_off_{uuid.uuid4().hex[:4]}"
        temp_off_id = None
        r_off = client.post("/api/users", json={
            "username": temp_off_uname,
            "password": "password123",
            "full_name": "Temporary Test Officer",
            "role": "officer"
        })
        if r_off.status_code in (200, 201):
            temp_off_id = r_off.get_json().get("user", {}).get("user_id")
            report_case("Provisioning", "Create temp Officer", "201", r_off.status_code, True)

        client.post("/api/logout")

        # 3. Hierarchy Testing
        print("\n--- PHASE 3: Hierarchy Testing ---")
        
        # Test 1: Admin Power
        print("Test 1: Admin Managing Officer...")
        client.post("/api/login", json=existing_admin_cred)
        r_edit = client.put(f"/api/users/{temp_off_id}", json={"full_name": "Officer Renamed By Admin"})
        report_case("Hierarchy", "Admin edits Officer", "200", r_edit.status_code, r_edit.status_code == 200)
        
        # Test 2: Admin Restrictions
        print("Test 2: Admin cannot delete SuperAdmin...")
        # Get SuperAdmin ID first
        client.post("/api/logout")
        client.post("/api/login", json=super_admin_cred)
        users = client.get("/api/users").get_json()
        sa_obj = next((u for u in users if u['role'].lower() == 'superadmin'), None)
        sa_id = sa_obj['user_id'] if sa_obj else "bootstrap-admin-01"
        
        client.post("/api/logout")
        client.post("/api/login", json=existing_admin_cred)
        r_del_sa = client.delete(f"/api/users/{sa_id}")
        report_case("Security", "Admin attempts delete SuperAdmin", "403/404", r_del_sa.status_code, r_del_sa.status_code in (403, 404))
        
        # Test 3: Admin creating peer Admin (Should be allowed based on current code)
        r_peer = client.post("/api/users", json={"username": f"peer_{uuid.uuid4().hex[:4]}", "password": "123", "full_name": "Peer", "role": "admin"})
        report_case("Hierarchy", "Admin creates peer Admin", "201", r_peer.status_code, r_peer.status_code == 201)
        if r_peer.status_code == 201:
            client.delete(f"/api/users/{r_peer.get_json().get('user', {}).get('user_id')}")

        client.post("/api/logout")

        # 4. Cleanup
        print("\n--- PHASE 4: Cleanup ---")
        client.post("/api/login", json=super_admin_cred)
        if temp_off_id:
            client.delete(f"/api/users/{temp_off_id}")
        if temp_admin_id:
            client.delete(f"/api/users/{temp_admin_id}")
        print("Cleanup completed.")

if __name__ == "__main__":
    run_tests()
