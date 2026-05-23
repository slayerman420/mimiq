#!/usr/bin/env python3
"""
Mimiq Memory — Save feedback on a post, audit, or fingerprint
Usage: python3 save_feedback.py --type post --id <id> --rating 1 --notes "loved it"
       python3 save_feedback.py --type audit --id <id> --notes "missed substack"
       python3 save_feedback.py --type fingerprint --id <id> --notes "I never use rhetorical questions"
"""

import sqlite3
import argparse
import uuid
import json
from datetime import datetime, timezone
from pathlib import Path

MEMORY_DIR = Path.home() / ".claude" / "mimiq-memory"


def save_feedback():
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", required=True, choices=["post", "audit", "fingerprint"])
    parser.add_argument("--id", required=True)
    parser.add_argument("--rating", type=int, choices=[1, 2, 3], default=None,
                        help="1=perfect, 2=close, 3=off")
    parser.add_argument("--notes", default="")
    args = parser.parse_args()

    now = datetime.now(timezone.utc).isoformat()
    feedback_id = str(uuid.uuid4())[:8]

    RATING_LABELS = {1: "✅ Sounds exactly like me", 2: "🟡 Pretty close", 3: "❌ Off"}

    if args.type == "post":
        conn = sqlite3.connect(MEMORY_DIR / "posts.db")
        # Update post rating
        if args.rating:
            conn.execute("UPDATE posts SET rating=?, notes=?, updated_at=? WHERE id=?",
                         (args.rating, args.notes, now, args.id))
        # Log feedback entry
        conn.execute(
            "INSERT INTO post_feedback (id, post_id, rating, notes, created_at) VALUES (?, ?, ?, ?, ?)",
            (feedback_id, args.id, args.rating, args.notes, now)
        )
        conn.commit()
        conn.close()
        rating_label = RATING_LABELS.get(args.rating, "")
        print(f"✅ Post feedback saved (post: {args.id})")
        if args.rating:
            print(f"   Rating: {args.rating} — {rating_label}")
        if args.notes:
            print(f"   Notes: {args.notes}")

    elif args.type == "audit":
        conn = sqlite3.connect(MEMORY_DIR / "audits.db")
        conn.execute(
            "INSERT INTO audit_feedback (id, audit_id, notes, created_at) VALUES (?, ?, ?, ?)",
            (feedback_id, args.id, args.notes, now)
        )
        conn.commit()
        conn.close()
        print(f"✅ Audit feedback saved (audit: {args.id})")
        if args.notes:
            print(f"   Notes: {args.notes}")

    elif args.type == "fingerprint":
        fp_path = MEMORY_DIR / "fingerprints.json"
        if not fp_path.exists():
            print("❌ No fingerprint found.")
            return

        fp_store = json.loads(fp_path.read_text())
        active_id = fp_store.get("active_id")
        target_id = args.id if args.id != "active" else active_id

        for version in fp_store["versions"]:
            if version["id"] == target_id:
                version["feedback_count"] = version.get("feedback_count", 0) + 1
                version["feedback_deltas"].append({
                    "id": feedback_id,
                    "notes": args.notes,
                    "created_at": now
                })
                break

        fp_path.write_text(json.dumps(fp_store, indent=2))
        print(f"✅ Fingerprint feedback saved — style rules will be updated")
        if args.notes:
            print(f"   Correction: {args.notes}")


if __name__ == "__main__":
    save_feedback()
