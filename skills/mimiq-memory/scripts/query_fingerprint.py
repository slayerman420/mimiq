#!/usr/bin/env python3
"""
Mimiq Memory — Query current style fingerprint
Usage: python3 query_fingerprint.py [--all-versions]
"""

import json
import argparse
from pathlib import Path

MEMORY_DIR = Path.home() / ".claude" / "mimiq-memory"
FINGERPRINTS_PATH = MEMORY_DIR / "fingerprints.json"


def query_fingerprint():
    parser = argparse.ArgumentParser()
    parser.add_argument("--all-versions", action="store_true")
    args = parser.parse_args()

    if not FINGERPRINTS_PATH.exists():
        print("No fingerprint found. Run voice-capture first.")
        return

    fp_store = json.loads(FINGERPRINTS_PATH.read_text())
    versions = fp_store.get("versions", [])
    active_id = fp_store.get("active_id")

    if not versions:
        print("No fingerprint versions saved yet.")
        return

    if args.all_versions:
        print(f"✍️  All fingerprint versions ({len(versions)} total)\n")
        for v in versions:
            active_marker = " ← active" if v["id"] == active_id else ""
            print(f"  v{v['version']} [{v['id']}]{active_marker} — {v['created_at'][:10]}")
            print(f"  Feedback applied: {v.get('feedback_count', 0)} corrections")
            print()
    else:
        active = next((v for v in versions if v["id"] == active_id), versions[-1])
        print(f"✍️  Active Fingerprint — v{active['version']} [{active['id']}]")
        print(f"   Created: {active['created_at'][:10]}")
        print(f"   Feedback corrections: {active.get('feedback_count', 0)}")
        print()
        if isinstance(active["data"], dict):
            print(json.dumps(active["data"], indent=2))
        else:
            print(active["data"])

        deltas = active.get("feedback_deltas", [])
        if deltas:
            print(f"\n📝 Feedback history ({len(deltas)} items):")
            for d in deltas:
                print(f"  [{d['created_at'][:10]}] {d['notes']}")


if __name__ == "__main__":
    query_fingerprint()
