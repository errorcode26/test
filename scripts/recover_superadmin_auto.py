#!/usr/bin/env python3
"""Server-only recovery script to upsert or reset a superadmin account.

Run this from the server/host with access to the MongoDB instance (SSH).
It prints the generated password once — copy it securely and rotate after first login.
Supports `--dry-run` to show actions without modifying the database.
"""
import secrets
import argparse
import os
from datetime import datetime
from dotenv import load_dotenv

# Load .env into environment so MONGO_URI is available when running the script
load_dotenv()


def random_password(length=20):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+"
    return ''.join(secrets.choice(alphabet) for _ in range(length))


def upsert_superadmin(username=None, password=None, dry_run=False):
    now = datetime.utcnow().isoformat() + "Z"
    username = username or f"recovery_sa_{now.replace(':','').replace('-','').replace('T','_')}"
    password = password or random_password()

    if dry_run:
        print("[DRY-RUN] Would ensure a superadmin exists or be updated with the following:")
        print("USERNAME:", username)
        print("PASSWORD:", password)
        print("[DRY-RUN] No database connections or writes were performed.")
        return username, password, False

    # Perform actual DB operations
    # Import heavy dependencies only when performing real DB operations so
    # `--dry-run` remains usable in minimal environments.
    from werkzeug.security import generate_password_hash
    from pymongo import MongoClient

    # Load MONGO_URI from project config if available, otherwise from env
    try:
        from config import MONGO_URI
    except Exception:
        MONGO_URI = os.environ.get("MONGO_URI")
    if not MONGO_URI:
        raise RuntimeError("MONGO_URI is not set in config.py or environment.")

    client = MongoClient(MONGO_URI)
    db = client.get_database("indialims")
    users = db.users

    sa = users.find_one({"role": "superadmin"})
    if sa:
        users.update_one({"_id": sa["_id"]}, {"$set": {
            "username": username,
            "password_hash": generate_password_hash(password),
            "is_active": True,
            "last_login": now,
            "is_recovery": True
        }})
        created = False
    else:
        users.insert_one({
            "user_id": f"recovery-sa-{now}",
            "username": username,
            "password_hash": generate_password_hash(password),
            "role": "superadmin",
            "full_name": "Recovery SuperAdmin",
            "email": "",
            "phone": "",
            "is_active": True,
            "is_recovery": True,
            "created_at": now,
            "last_login": now
        })
        created = True
    print("SuperAdmin created" if created else "SuperAdmin updated")
    print("USERNAME:", username)
    print("PASSWORD:", password)
    print("IMPORTANT: copy the password now and rotate on first login.")
    return username, password, created


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upsert/reset superadmin (server-only).")
    parser.add_argument("username", nargs="?", help="Optional username to set")
    parser.add_argument("password", nargs="?", help="Optional password to set")
    parser.add_argument("--dry-run", action="store_true", help="Show actions without writing to DB")
    parser.add_argument("--dump", action="store_true", help="Dump credentials to a file in the scripts folder")
    parser.add_argument("--dump-file", help="Optional path for dumped credentials (overrides default)")
    args = parser.parse_args()

    username, password, created = upsert_superadmin(args.username, args.password, dry_run=args.dry_run)

    # If requested, write the last generated credentials to a file for operator convenience.
    # Note: `upsert_superadmin` prints credentials; to capture them here we re-run a quiet
    # generation when --dump is requested but do not modify DB again.
    if args.dump and not args.dry_run:
        # Use the exact credentials returned from the upsert operation
        # (so the dump matches what was written to the DB)
        dump_username = username
        dump_password = password

        # If user provided --dump-file use it; otherwise place in scripts folder
        dump_path = args.dump_file
        if not dump_path:
            scripts_dir = os.path.dirname(__file__)
            safe_now = datetime.utcnow().isoformat().replace(':', '').replace('.', '_')
            dump_path = os.path.join(scripts_dir, f"recovery_credentials_{safe_now}.txt")

        with open(dump_path, 'w', encoding='utf-8') as f:
            f.write(f"# Recovery credentials generated: {datetime.utcnow().isoformat()}Z\n")
            f.write(f"USERNAME: {dump_username}\n")
            f.write(f"PASSWORD: {dump_password}\n")
            f.write("# IMPORTANT: rotate this password immediately after first login.\n")

        print(f"Credentials dumped to: {dump_path}")
