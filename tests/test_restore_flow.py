r"""
Test restore flow:
- Login as admin, create temp officer and a record
- Login as officer, soft-delete the record
- Login as admin, restore the record
- Verify record is present after restore
- Cleanup created users and record
"""
import os, sys, json, uuid
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import app

CRED_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "user_id_password.json")
with open(CRED_FILE, "r", encoding="utf-8") as f: creds = json.load(f)

admin = None
for e in creds:
    name = e.get('username') or e.get('user_id')
    if name and name.lower() == 'admin':
        admin = {'username': name, 'password': e.get('password')}
        break
if not admin: admin = creds[0]

def report_case(scenario, action, expected, actual, passed):
    status = "PASS" if passed else "FAIL"
    print(f"__TEST_RESULT__||{scenario}||{action}||{expected}||{actual}||{status}")

record_id = None
officer_id = None
unique_id = uuid.uuid4().hex[:6]

with app.test_client() as c_admin:
    print("Admin login...")
    r = c_admin.post('/api/login', json=admin)

    temp_officer = {'username': f'temp_off_res_{unique_id}', 'password': 'pw', 'full_name': 'Restore Officer', 'role': 'officer'}
    resp = c_admin.post('/api/users', json=temp_officer)
    if resp.is_json:
        officer_id = resp.get_json().get('user', {}).get('user_id') or resp.get_json().get('user_id')

    sample = {
        'khasra_no': f'REST-{unique_id}', 'khata_no': 'REST-K',
        'location': {'state': 'TS', 'district': 'TD', 'village': 'TV'},
        'geometry': {'type': 'Polygon', 'coordinates': [[[78.0,20.0],[78.001,20.0],[78.001,20.001],[78.0,20.001],[78.0,20.0]]]},
        'land_use': 'Agricultural', 'owner_name': 'Restore Owner'
    }
    r2 = c_admin.post('/api/records', json=sample)
    if r2.is_json and r2.get_json().get('record'):
        record_id = r2.get_json()['record'].get('_id')

if record_id:
    with app.test_client() as c_off:
        c_off.post('/api/login', json=temp_officer)
        print("Officer soft delete...")
        c_off.delete(f'/api/records/{record_id}')

    with app.test_client() as c_admin2:
        c_admin2.post('/api/login', json=admin)
        print("Admin restore...")
        restore = c_admin2.post(f'/api/records/{record_id}/restore')
        print(restore.status_code)
        report_case("Restore Record", "Admin POST restore", "200", restore.status_code, restore.status_code == 200)

        getr = c_admin2.get(f'/api/records/{record_id}')
        data = getr.get_json() if getr.is_json else {}
        is_restored = getr.is_json and data.get('deleted') is False
        report_case("Verify Restore", "Admin GET record", "deleted=False", f"deleted={not is_restored}", is_restored)

        if officer_id: c_admin2.delete(f'/api/users/{officer_id}')
        c_admin2.delete(f'/api/records/{record_id}')