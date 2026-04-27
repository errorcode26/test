r"""
Test soft-delete flow for records:
- Login as admin, create a record
- Login as officer, soft-delete the record
- Verify viewer/officer cannot see soft-deleted record
- Login as admin, hard-delete the record
"""
import os
import sys
import json
import uuid
from pprint import pprint

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import app

CRED_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "user_id_password.json")
with open(CRED_FILE, "r", encoding="utf-8") as f:
    creds = json.load(f)

admin = None
for e in creds:
    name = e.get('username') or e.get('user_id')
    if name and name.lower() == 'admin':
        admin = {'username': name, 'password': e.get('password')}
        break
if not admin:
    admin = {'username': creds[0].get('username') or creds[0].get('user_id'), 'password': creds[0].get('password')}

def report_case(scenario, action, expected, actual, passed):
    status = "PASS" if passed else "FAIL"
    print(f"__TEST_RESULT__||{scenario}||{action}||{expected}||{actual}||{status}")

record_id = None
officer_id = None
unique_id = uuid.uuid4().hex[:6]

with app.test_client() as client:
    print("Admin login...")
    r = client.post('/api/login', json=admin)
    print(r.status_code)
    report_case("Admin Setup", "Login as Admin", "200", r.status_code, r.status_code == 200)

    temp_officer = {'username': f'temp_off_del_{unique_id}', 'password': 'op', 'full_name': 'Temp Officer', 'role': 'officer'}
    print("Create officer...")
    resp = client.post('/api/users', json=temp_officer)
    if resp.is_json:
        officer_id = resp.get_json().get('user', {}).get('user_id') or resp.get_json().get('user_id')
    print(resp.status_code)
    
    sample = {
        'khasra_no': f'K-{unique_id}',
        'khata_no': 'KH-1',
        'location': {'state': 'TestState', 'district': 'TestDistrict', 'village': 'TestVillage'},
        'geometry': {'type': 'Polygon', 'coordinates': [[[78.0, 20.0],[78.001,20.0],[78.001,20.001],[78.0,20.001],[78.0,20.0]]]},
        'land_use': 'Agricultural',
        'owner_name': 'Record Owner'
    }
    print("Create record...")
    r2 = client.post('/api/records', json=sample)
    print(r2.status_code)
    if r2.is_json and r2.get_json().get('record'):
        record_id = r2.get_json()['record'].get('_id')
    report_case("Record Setup", "Admin POST /api/records", "201", r2.status_code, r2.status_code == 201)

if record_id:
    with app.test_client() as c2:
        print("Officer login...")
        c2.post('/api/login', json=temp_officer)
        
        print("Officer delete attempt...")
        del_resp = c2.delete(f'/api/records/{record_id}')
        print(del_resp.status_code)
        report_case("Soft Delete", "Officer DELETE record", "200", del_resp.status_code, del_resp.status_code == 200)

        print("Verify record is hidden...")
        list_resp = c2.get('/api/records')
        is_hidden = True
        if list_resp.is_json:
            data = list_resp.get_json()
            if isinstance(data, list):
                is_hidden = not any(rec.get('_id') == record_id for rec in data)
            elif isinstance(data, dict) and "records" in data:
                is_hidden = not any(rec.get('_id') == record_id for rec in data["records"])
        print(f"Record hidden: {is_hidden}")
        report_case("Data Privacy", "Officer GET records", "Hidden", "Hidden" if is_hidden else "Visible", is_hidden)

with app.test_client() as adminc:
    adminc.post('/api/login', json=admin)
    if record_id:
        print("Admin hard delete...")
        del_hard = adminc.delete(f'/api/records/{record_id}')
        print(del_hard.status_code)
        report_case("Hard Delete", "Admin hard delete", "200", del_hard.status_code, del_hard.status_code == 200)

    if officer_id:
        adminc.delete(f'/api/users/{officer_id}')