#!/usr/bin/env python3
"""
Mimiq Memory — Database Initializer
Creates all required databases and JSON files at ~/.claude/mimiq-memory/
"""

import os
import json
import sqlite3
from pathlib import Path

MEMORY_DIR = Path.home() / ".claude" / "mimiq-memory"


def init():
    MEMORY_DIR.mkdir(parents=True, exist_ok=True)

    # --- profiles.json ---
    profiles_path = MEMORY_DIR / "profiles.json"
    if not profiles_path.exists():
        profiles_path.write_text(json.dumps({
            "name": None,
            "platforms": {},
            "community_opt_in": None,
            "created_at": None
        }, indent=2))

    # --- fingerprints.json ---
    fingerprints_path = MEMORY_DIR / "fingerprints.json"
    if not fingerprints_path.exists():
        fingerprints_path.write_text(json.dumps({
            "versions": [],
            "active_id": None
        }, indent=2))

    # --- shared_patterns.json ---
    patterns_path = MEMORY_DIR / "shared_patterns.json"
    if not patterns_path.exists():
        patterns_path.write_text(json.dumps({
            "patterns": [],
            "last_updated": None
        }, indent=2))

    # --- posts.db ---
    posts_db = sqlite3.connect(MEMORY_DIR / "posts.db")
    posts_db.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id          TEXT PRIMARY KEY,
            platform    TEXT NOT NULL,
            topic       TEXT,
            content     TEXT NOT NULL,
            rating      INTEGER,
            notes       TEXT,
            published   INTEGER DEFAULT 0,
            created_at  TEXT NOT NULL,
            updated_at  TEXT
        )
    """)
    posts_db.execute("""
        CREATE TABLE IF NOT EXISTS post_feedback (
            id          TEXT PRIMARY KEY,
            post_id     TEXT NOT NULL,
            rating      INTEGER,
            notes       TEXT,
            created_at  TEXT NOT NULL,
            FOREIGN KEY (post_id) REFERENCES posts(id)
        )
    """)
    posts_db.commit()
    posts_db.close()

    # --- audits.db ---
    audits_db = sqlite3.connect(MEMORY_DIR / "audits.db")
    audits_db.execute("""
        CREATE TABLE IF NOT EXISTS audits (
            id              TEXT PRIMARY KEY,
            platform        TEXT NOT NULL,
            data            TEXT NOT NULL,
            top_posts       TEXT,
            best_times      TEXT,
            topic_clusters  TEXT,
            created_at      TEXT NOT NULL
        )
    """)
    audits_db.execute("""
        CREATE TABLE IF NOT EXISTS audit_feedback (
            id          TEXT PRIMARY KEY,
            audit_id    TEXT NOT NULL,
            notes       TEXT,
            created_at  TEXT NOT NULL,
            FOREIGN KEY (audit_id) REFERENCES audits(id)
        )
    """)
    audits_db.commit()
    audits_db.close()

    print(f"✅ Mimiq memory initialized at {MEMORY_DIR}")
    print("   Files created:")
    for f in sorted(MEMORY_DIR.iterdir()):
        print(f"   - {f.name}")


if __name__ == "__main__":
    init()
