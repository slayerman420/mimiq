#!/usr/bin/env python3
"""
Mimiq Memory — Save a new style fingerprint version
Usage: python3 save_fingerprint.py --data '<fingerprint JSON string>'
"""

import json
import argparse
import uuid
from datetime import datetime, timezone
from pathlib import Path

MEMORY_DIR = Path.home() / ".claude" / "mimiq-memory"
FINGERPRINTS_PATH = MEMORY_DIR / "fingerprints.json"


def save_fingerprint():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True, help="Fingerprint data as JSON string")
    args = parser.parse_args()

    try:
        fingerprint_data = json.loads(args.data)
    except json.JSONDecodeError:
        # Accept plain text fingerprint too
        fingerprint_data = {"raw": args.data}

    fp_store = json.loads(FINGERPRINTS_PATH.read_text()) if FINGERPRINTS_PATH.exists() else {"versions": [], "active_id": None}

    new_version = {
        "id": str(uuid.uuid4())[:8],
        "version": len(fp_store["versions"]) + 1,
        "data": fingerprint_data,
        "feedback_count": 0,
        "feedback_deltas": [],
        "created_at": datetime.now(timezone.utc).isoformat()
    }

    fp_store["versions"].append(new_version)
    fp_store["active_id"] = new_version["id"]

    FINGERPRINTS_PATH.write_text(json.dumps(fp_store, indent=2))
    print(f"✅ Fingerprint v{new_version['version']} saved (id: {new_version['id']})")


if __name__ == "__main__":
    save_fingerprint()
