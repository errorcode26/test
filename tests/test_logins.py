r"""
Test login flow using Flask test client and credentials in user_id_password.json
Usage: .venv\Scripts\python tests\test_logins.py
"""
import os
import sys
import json
from pprint import pprint

# Ensure project root is importable
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from app import app
except Exception as e:
    print(f"Failed to import app: {e}")
    sys.exit(1)

CRED_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "user_id_password.json")
if not os.path.exists(CRED_FILE):
    print(f"Credentials file not found: {CRED_FILE}")
    sys.exit(1)

with open(CRED_FILE, "r", encoding="utf-8") as f:
    try:
        creds = json.load(f)
    except Exception as e:
        print(f"Failed to parse credentials file: {e}")
        sys.exit(1)

if not isinstance(creds, list):
    print("Expected JSON array of credentials objects")
    sys.exit(1)

def report_case(scenario, action, expected, actual, passed):
    status = "PASS" if passed else "FAIL"
    print(f"__TEST_RESULT__||{scenario}||{action}||{expected}||{actual}||{status}")

with app.test_client() as client:
    # 1. Test Valid Logins
    for entry in creds:
        username = entry.get("username") or entry.get("user_id")
        password = entry.get("password")
        if not username or not password:
            continue
        print(f"\nTesting valid login for: {username}")
        resp = client.post("/api/login", json={"username": username, "password": password})
        print(f"Status: {resp.status_code}")
        try: pprint(resp.get_json(force=True))
        except: print(resp.data.decode()[:200])
        report_case(f"Valid Login ({username})", "Submit correct credentials", "200", resp.status_code, resp.status_code == 200)

    # 2. Test Invalid Username
    print("\nTesting Invalid Username")
    resp = client.post("/api/login", json={"username": "doesnotexist_user", "password": "password123"})
    print(f"Status: {resp.status_code}")
    try: pprint(resp.get_json(force=True))
    except: print(resp.data.decode()[:200])
    report_case("Invalid Username", "Submit non-existent username", "401", resp.status_code, resp.status_code == 401)

    # 3. Test Invalid Password
    if creds and len(creds) > 0:
        valid_user = creds[0].get("username") or creds[0].get("user_id")
        print(f"\nTesting Invalid Password for user: {valid_user}")
        resp = client.post("/api/login", json={"username": valid_user, "password": "wrongpassword!"})
        print(f"Status: {resp.status_code}")
        try: pprint(resp.get_json(force=True))
        except: print(resp.data.decode()[:200])
        report_case("Invalid Password", f"Submit wrong password for {valid_user}", "401", resp.status_code, resp.status_code == 401)
