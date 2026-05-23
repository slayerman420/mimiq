#!/usr/bin/env python3
"""
Mimiq Memory — Query audit history
Usage: python3 query_audits.py [--latest] [--platform linkedin]
"""

import sqlite3
import argparse
from pathlib import Path

MEMORY_DIR = Path.home() / ".claude" / "mimiq-memory"


def query_audits():
    parser = argparse.ArgumentParser()
    parser.add_argument("--latest", action="store_true")
    parser.add_argument("--platform", default=None)
    parser.add_argument("--limit", type=int, default=5)
    args = parser.parse_args()

    conn = sqlite3.connect(MEMORY_DIR / "audits.db")

    query = "SELECT id, platform, best_times, topic_clusters, created_at FROM audits WHERE 1=1"
    params = []

    if args.platform:
        query += " AND platform=?"
        params.append(args.platform)

    query += " ORDER BY created_at DESC"

    if args.latest:
        query += " LIMIT 1"
    else:
        query += f" LIMIT {args.limit}"

    rows = conn.execute(query, params).fetchall()
    conn.close()

    if not rows:
        print("No audits found.")
        return

    print(f"📊 Audits ({len(rows)} results)\n")
    for row in rows:
        id_, platform, best_times, topic_clusters, created_at = row
        print(f"  [{id_}] {platform.upper()} — {created_at[:10]}")
        if best_times:
            print(f"  Best times: {best_times}")
        if topic_clusters:
            print(f"  Top topics: {topic_clusters}")
        print()


if __name__ == "__main__":
    query_audits()
