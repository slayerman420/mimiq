#!/usr/bin/env python3
"""
Mimiq Memory — Query post history
Usage: python3 query_posts.py [--limit 10] [--rating 1] [--platform linkedin] [--published]
"""

import sqlite3
import argparse
from pathlib import Path

MEMORY_DIR = Path.home() / ".claude" / "mimiq-memory"

RATING_LABELS = {1: "✅ Perfect", 2: "🟡 Close", 3: "❌ Off", None: "⏳ Unrated"}


def query_posts():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--rating", type=int, choices=[1, 2, 3], default=None)
    parser.add_argument("--platform", default=None)
    parser.add_argument("--published", action="store_true")
    parser.add_argument("--latest", action="store_true")
    args = parser.parse_args()

    conn = sqlite3.connect(MEMORY_DIR / "posts.db")

    query = "SELECT id, platform, topic, content, rating, notes, published, created_at FROM posts WHERE 1=1"
    params = []

    if args.rating:
        query += " AND rating=?"
        params.append(args.rating)
    if args.platform:
        query += " AND platform=?"
        params.append(args.platform)
    if args.published:
        query += " AND published=1"
    if args.latest:
        query += " ORDER BY created_at DESC LIMIT 1"
    else:
        query += " ORDER BY created_at DESC LIMIT ?"
        params.append(args.limit)

    rows = conn.execute(query, params).fetchall()
    conn.close()

    if not rows:
        print("No posts found.")
        return

    print(f"📝 Posts ({len(rows)} results)\n")
    for row in rows:
        id_, platform, topic, content, rating, notes, published, created_at = row
        print(f"  [{id_}] {platform.upper()} — {created_at[:10]}")
        print(f"  Topic: {topic or 'unspecified'}")
        print(f"  Rating: {RATING_LABELS.get(rating, '⏳ Unrated')}")
        if notes:
            print(f"  Notes: {notes}")
        print(f"  Published: {'Yes' if published else 'No'}")
        print(f"  Preview: {content[:100]}...")
        print()


if __name__ == "__main__":
    query_posts()
