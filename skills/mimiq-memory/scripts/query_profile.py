#!/usr/bin/env python3
"""
Mimiq Memory — Query user profile and linked platforms
Usage: python3 query_profile.py
"""

import json
from pathlib import Path

MEMORY_DIR = Path.home() / ".claude" / "mimiq-memory"
PROFILES_PATH = MEMORY_DIR / "profiles.json"


def query_profile():
    if not PROFILES_PATH.exists():
        print("No profile found. Run save_profile.py first.")
        return

    profile = json.loads(PROFILES_PATH.read_text())
    print(f"👤 Name: {profile.get('name', 'Unknown')}")
    print(f"   Created: {profile.get('created_at', 'unknown')[:10]}")
    print(f"   Community opt-in: {profile.get('community_opt_in', 'Not decided')}")
    print()

    platforms = profile.get("platforms", {})
    if platforms:
        print("🔗 Linked Platforms:")
        for platform, handle in platforms.items():
            print(f"   {platform:<12} @{handle}")
    else:
        print("No platforms linked yet.")


if __name__ == "__main__":
    query_profile()
