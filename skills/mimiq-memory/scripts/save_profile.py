#!/usr/bin/env python3
"""
Mimiq Memory — Save/Update User Profile
Usage: python3 save_profile.py --name "Salman" --linkedin "m-salman-shahid" --twitter "slayerman420"
"""

import json
import argparse
from datetime import datetime, timezone
from pathlib import Path

MEMORY_DIR = Path.home() / ".claude" / "mimiq-memory"
PROFILES_PATH = MEMORY_DIR / "profiles.json"

SUPPORTED_PLATFORMS = [
    "linkedin", "twitter", "reddit", "medium",
    "substack", "instagram", "facebook"
]

def save_profile():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True)
    for platform in SUPPORTED_PLATFORMS:
        parser.add_argument(f"--{platform}", default=None)
    args = parser.parse_args()

    profile = json.loads(PROFILES_PATH.read_text()) if PROFILES_PATH.exists() else {}

    profile["name"] = args.name
    profile.setdefault("platforms", {})
    profile.setdefault("created_at", datetime.now(timezone.utc).isoformat())
    profile["updated_at"] = datetime.now(timezone.utc).isoformat()

    for platform in SUPPORTED_PLATFORMS:
        handle = getattr(args, platform)
        if handle:
            profile["platforms"][platform] = handle

    PROFILES_PATH.write_text(json.dumps(profile, indent=2))
    print(f"✅ Profile saved: {profile['name']}")
    print(f"   Platforms: {json.dumps(profile['platforms'], indent=4)}")


if __name__ == "__main__":
    save_profile()
