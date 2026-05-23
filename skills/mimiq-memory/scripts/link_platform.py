#!/usr/bin/env python3
"""
Mimiq Memory — Link a new platform handle to existing profile
Usage: python3 link_platform.py --platform "substack" --handle "salman-writes"
"""

import json
import argparse
from datetime import datetime, timezone
from pathlib import Path

MEMORY_DIR = Path.home() / ".claude" / "mimiq-memory"
PROFILES_PATH = MEMORY_DIR / "profiles.json"


def link_platform():
    parser = argparse.ArgumentParser()
    parser.add_argument("--platform", required=True)
    parser.add_argument("--handle", required=True)
    args = parser.parse_args()

    if not PROFILES_PATH.exists():
        print("❌ No profile found. Run init_db.py and save_profile.py first.")
        return

    profile = json.loads(PROFILES_PATH.read_text())
    profile.setdefault("platforms", {})
    profile["platforms"][args.platform.lower()] = args.handle
    profile["updated_at"] = datetime.now(timezone.utc).isoformat()

    PROFILES_PATH.write_text(json.dumps(profile, indent=2))
    print(f"✅ Linked {args.platform} → @{args.handle} to profile '{profile.get('name', 'unknown')}'")
    print(f"   All platforms: {json.dumps(profile['platforms'], indent=4)}")


if __name__ == "__main__":
    link_platform()
