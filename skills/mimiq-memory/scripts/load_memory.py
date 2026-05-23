#!/usr/bin/env python3
"""
Mimiq Memory — Load full memory state at session start
Usage: python3 load_memory.py
"""

import json
import sqlite3
from pathlib import Path
from datetime import datetime, timezone

MEMORY_DIR = Path.home() / ".claude" / "mimiq-memory"


def load_memory():
    if not MEMORY_DIR.exists():
        print("⚠️  No Mimiq memory found. Run init_db.py to initialize.")
        return

    print("🪞 Mimiq Memory — Session Start\n")

    # Profile
    profiles_path = MEMORY_DIR / "profiles.json"
    if profiles_path.exists():
        profile = json.loads(profiles_path.read_text())
        name = profile.get("name", "Unknown")
        platforms = profile.get("platforms", {})
        print(f"👤 User: {name}")
        if platforms:
            print("   Linked platforms:")
            for platform, handle in platforms.items():
                print(f"     {platform}: @{handle}")
        else:
            print("   No platforms linked yet.")
        print()

    # Fingerprint
    fingerprints_path = MEMORY_DIR / "fingerprints.json"
    if fingerprints_path.exists():
        fp_data = json.loads(fingerprints_path.read_text())
        versions = fp_data.get("versions", [])
        active_id = fp_data.get("active_id")
        if versions:
            active = next((v for v in versions if v["id"] == active_id), versions[-1])
            print(f"✍️  Style Fingerprint: v{len(versions)} (last updated {active.get('created_at', 'unknown')[:10]})")
            feedback_count = active.get("feedback_count", 0)
            if feedback_count:
                print(f"   Feedback applied: {feedback_count} corrections")
        else:
            print("✍️  Style Fingerprint: None yet")
        print()

    # Posts
    posts_db_path = MEMORY_DIR / "posts.db"
    if posts_db_path.exists():
        conn = sqlite3.connect(posts_db_path)
        total = conn.execute("SELECT COUNT(*) FROM posts").fetchone()[0]
        published = conn.execute("SELECT COUNT(*) FROM posts WHERE published=1").fetchone()[0]
        pending_feedback = conn.execute(
            "SELECT COUNT(*) FROM posts WHERE rating IS NULL"
        ).fetchone()[0]
        conn.close()
        print(f"📝 Posts: {total} written, {published} published, {pending_feedback} awaiting feedback")

    # Audits
    audits_db_path = MEMORY_DIR / "audits.db"
    if audits_db_path.exists():
        conn = sqlite3.connect(audits_db_path)
        total = conn.execute("SELECT COUNT(*) FROM audits").fetchone()[0]
        latest = conn.execute(
            "SELECT platform, created_at FROM audits ORDER BY created_at DESC LIMIT 1"
        ).fetchone()
        conn.close()
        if latest:
            print(f"📊 Audits: {total} total — last: {latest[0]} on {latest[1][:10]}")
        else:
            print(f"📊 Audits: {total} total")

    # Community opt-in
    if profiles_path.exists():
        opt_in = profile.get("community_opt_in")
        if opt_in is None:
            print("\n💡 Tip: You haven't decided on community insights sharing yet.")
            print("   Say 'tell me about community insights' to learn more.")
        elif opt_in:
            print("\n🌐 Community insights: Opted in ✓")

    print("\n✅ Memory loaded. Ready to go.\n")


if __name__ == "__main__":
    load_memory()
