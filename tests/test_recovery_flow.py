r"""
Recovery account integration smoke test (create + delete superadmin)
Run: .venv\Scripts\python tests\test_recovery_flow.py
"""
import os, sys, json
import uuid
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import app

CRED_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "user_id_password.json")
with open(CRED_FILE, "r", encoding="utf-8") as f:
    creds = json.load(f)

# find recovery creds (explicit or by username prefix)
recov = None
for c in creds:
    uname = c.get('username') or c.get('user_id')
    if uname and uname.startswith('recovery_sa_'):
        recov = c
        break
if not recov:
    print("No recovery credentials in user_id_password.json — add them and re-run.")
    raise SystemExit(1)

recov_username = recov.get('username') or recov.get('user_id')
recov_password = recov.get('password')

def report_case(scenario, action, expected, actual, passed):
    status = "PASS" if passed else "FAIL"
    print(f"__TEST_RESULT__||{scenario}||{action}||{expected}||{actual}||{status}")


with app.test_client() as client:
    # Login as recovery
    r = client.post('/api/login', json={"username": recov_username, "password": recov_password})
    report_case("Recovery Login", "Login with recovery creds", "200", r.status_code, r.status_code == 200)
    if r.status_code != 200:
        raise SystemExit(2)

    # Create a new superadmin (unique username)
    ts = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    new_username = f"sa_test_create_{ts}_{str(uuid.uuid4())[:6]}"
    new_sa = {"username": new_username, "password": "TempP@ss123!", "full_name": "SA Test", "role": "superadmin"}
    resp = client.post('/api/users', json=new_sa)
    created = resp.status_code in (200, 201)
    report_case("Create SuperAdmin", "POST /api/users as recovery", "201", resp.status_code, created)

    created_id = None
    if resp.is_json:
        created_id = resp.get_json().get('user', {}).get('user_id') or resp.get_json().get('user_id')

    # Delete created superadmin (cleanup)
    if created_id:
        d = client.delete(f"/api/users/{created_id}")
        report_case("Delete SuperAdmin", "DELETE /api/users/<id> as recovery", "200", d.status_code, d.status_code == 200)
    else:
        print("No created_id returned; skipping delete step.")
