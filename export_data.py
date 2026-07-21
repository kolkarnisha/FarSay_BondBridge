"""
export_data.py
--------------
Exports users and events from MongoDB into db_export.json
so that user_data_table.html can display them.

Run this whenever you want fresh data:
    python export_data.py
"""

from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime
import os
import json

# Load credentials from .env
load_dotenv()

MONGODB_USERNAME = os.getenv("MONGODB_USERNAME")
MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")
MONGODB_CLUSTER  = os.getenv("MONGODB_CLUSTER")
DATABASE_NAME    = os.getenv("DATABASE_NAME")

if not all([MONGODB_USERNAME, MONGODB_PASSWORD, MONGODB_CLUSTER, DATABASE_NAME]):
    print("✗ Missing MongoDB credentials in .env file")
    exit(1)

MONGODB_URI = (
    f"mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}"
    f"@{MONGODB_CLUSTER}/{DATABASE_NAME}?retryWrites=true&w=majority"
)

print("Connecting to MongoDB…")
try:
    client = MongoClient(MONGODB_URI, serverSelectionTimeoutMS=8000)
    client.server_info()          # force connection check
    db = client[DATABASE_NAME]
    print("✓ Connected!")
except Exception as e:
    print(f"✗ Connection failed: {e}")
    exit(1)


def serialize(doc):
    """Convert MongoDB document to a JSON-safe dict."""
    out = {}
    for k, v in doc.items():
        if k == "_id":
            out[k] = str(v)
        elif isinstance(v, datetime):
            out[k] = v.isoformat()
        else:
            out[k] = v
    return out


# Fetch all users
users  = [serialize(u) for u in db["users"].find()]
events = [serialize(e) for e in db["events"].find()]

export = {
    "exported_at": datetime.now().isoformat(),
    "users":  users,
    "events": events
}

output_file = "db_export.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(export, f, indent=2, ensure_ascii=False)

print(f"\n✓ Exported {len(users)} user(s) and {len(events)} event(s) → {output_file}")
print("  Open user_data_table.html in your browser to view the data.")
