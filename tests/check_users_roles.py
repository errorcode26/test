r"""
Simple verifier: list users and their stored roles
"""
import os, sys, json
try:
    from config import MONGO_URI
    from utils import resource_path
except Exception:
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from config import MONGO_URI
    from utils import resource_path

def report_case(scenario, action, expected, actual, passed):
    status = "PASS" if passed else "FAIL"
    print(f"__TEST_RESULT__||{scenario}||{action}||{expected}||{actual}||{status}")

def check():
    if MONGO_URI:
        from pymongo import MongoClient
        import certifi
        client = MongoClient(MONGO_URI, tlsCAFile=certifi.where(), serverSelectionTimeoutMS=5000)
        users = list(client.get_database("indialims").users.find({}))
        client.close()
    else:
        with open(os.path.join(resource_path("data"), "users.json"), "r", encoding="utf-8") as f:
            users = json.load(f)
    
    for u in users:
        uid = u.get('user_id') or u.get('_id')
        uname = u.get('username')
        role = u.get('role')
        print(f"Found User: {uname} ({role})")
        report_case("Data Integrity", f"Check user {uname}", "Has Role", "Has Role" if role else "No Role", bool(role))

if __name__ == '__main__':
    check()