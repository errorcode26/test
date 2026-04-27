#!/usr/bin/env python3
"""Inspect superadmin and recovery accounts in the database."""
from dotenv import load_dotenv
import os
load_dotenv()
from pymongo import MongoClient
try:
    from config import MONGO_URI
except Exception:
    MONGO_URI = os.environ.get('MONGO_URI')

def main():
    uri = MONGO_URI or os.environ.get('MONGO_URI')
    if not uri:
        raise SystemExit('MONGO_URI not found in config or environment')
    client = MongoClient(uri)
    db = client.get_database('indialims')
    users = list(db.users.find({}, {'password_hash': 0}))
    print('Total users:', len(users))
    print('\nSuperadmin users:')
    for u in users:
        if u.get('role') == 'superadmin':
            print('-', u.get('username'), '| is_recovery=', u.get('is_recovery', False))

    print('\nRecovery-flagged users:')
    for u in users:
        if u.get('is_recovery'):
            print('-', u.get('username'), '| role=', u.get('role'))

if __name__ == '__main__':
    main()
