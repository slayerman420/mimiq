#!/usr/bin/env python3
"""
Mimiq Memory — Log a ghostwritten post
Usage: python3 save_post.py --platform linkedin --topic "product launch" --content "Post text here"
"""

import sqlite3
import argparse
import uuid
from datetime import datetime, timezone
from pathlib import Path

MEMORY_DIR = Path.home() / ".claude" / "mimiq-memory"


def save_post():
    parser = argparse.ArgumentParser()
    parser.add_argument("--platform", required=True)
    parser.add_argument("--topic", default="")
    parser.add_argument("--content", required=True)
    args = parser.parse_args()

    post_id = str(uuid.uuid4())[:8]
    now = datetime.now(timezone.utc).isoformat()

    conn = sqlite3.connect(MEMORY_DIR / "posts.db")
    conn.execute(
        "INSERT INTO posts (id, platform, topic, content, created_at) VALUES (?, ?, ?, ?, ?)",
        (post_id, args.platform, args.topic, args.content, now)
    )
    conn.commit()
    conn.close()

    print(f"✅ Post saved (id: {post_id})")
    print(f"   Platform: {args.platform}")
    print(f"   Topic: {args.topic or 'unspecified'}")
    print(f"   Preview: {args.content[:80]}...")
    print(f"\n💬 Rate this post: python3 save_feedback.py --type post --id {post_id} --rating <1-3> --notes \"your notes\"")


if __name__ == "__main__":
    save_post()
