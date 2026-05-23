#!/usr/bin/env python3
"""
Mimiq Memory — Save end-of-session snapshot
Usage: python3 save_session.py
"""

import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

MEMORY_DIR = Path.home() / ".claude" / "mimiq-memory"


def save_session():
    now = datetime.now(timezone.utc).isoformat()
    summary = {"saved_at": now, "pending_feedback": []}

    # Check for unrated posts
    posts_db = MEMORY_DIR / "posts.db"
    if posts_db.exists():
        conn = sqlite3.connect(posts_db)
        unrated = conn.execute(
            "SELECT id, platform, topic FROM posts WHERE rating IS NULL ORDER BY created_at DESC LIMIT 5"
        ).fetchall()
        conn.close()
        for row in unrated:
            summary["pending_feedback"].append({
                "type": "post", "id": row[0], "platform": row[1], "topic": row[2]
            })

    # Save session log
    sessions_path = MEMORY_DIR / "sessions.json"
    sessions = json.loads(sessions_path.read_text()) if sessions_path.exists() else {"sessions": []}
    sessions["sessions"].append(summary)
    sessions_path.write_text(json.dumps(sessions, indent=2))

    print(f"✅ Session saved — {now[:10]}")

    if summary["pending_feedback"]:
        print(f"\n⏳ {len(summary['pending_feedback'])} post(s) awaiting feedback:")
        for item in summary["pending_feedback"]:
            print(f"   [{item['id']}] {item['platform']} — {item['topic'] or 'unspecified'}")
        print("\nRate them next session with:")
        print("  python3 save_feedback.py --type post --id <id> --rating <1-3> --notes \"your notes\"")
    else:
        print("   No pending feedback. All caught up!")


if __name__ == "__main__":
    save_session()
