#!/usr/bin/env python3
"""
Mimiq Memory — Save an audit result
Usage: python3 save_audit.py --platform linkedin --data '<audit JSON>'
"""

import sqlite3
import argparse
import uuid
import json
from datetime import datetime, timezone
from pathlib import Path

MEMORY_DIR = Path.home() / ".claude" / "mimiq-memory"


def save_audit():
    parser = argparse.ArgumentParser()
    parser.add_argument("--platform", required=True)
    parser.add_argument("--data", required=True)
    parser.add_argument("--top-posts", default="")
    parser.add_argument("--best-times", default="")
    parser.add_argument("--topic-clusters", default="")
    args = parser.parse_args()

    audit_id = str(uuid.uuid4())[:8]
    now = datetime.now(timezone.utc).isoformat()

    conn = sqlite3.connect(MEMORY_DIR / "audits.db")
    conn.execute(
        """INSERT INTO audits
           (id, platform, data, top_posts, best_times, topic_clusters, created_at)
           VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (audit_id, args.platform, args.data,
         args.top_posts, args.best_times, args.topic_clusters, now)
    )
    conn.commit()
    conn.close()

    print(f"✅ Audit saved (id: {audit_id})")
    print(f"   Platform: {args.platform}")
    print(f"\n💬 Give feedback: python3 save_feedback.py --type audit --id {audit_id} --notes \"your notes\"")


if __name__ == "__main__":
    save_audit()
