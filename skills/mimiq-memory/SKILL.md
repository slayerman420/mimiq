---
name: mimiq-memory
description: >
  Persistent memory and feedback system for Mimiq. Stores all scrapes, style fingerprints,
  audits, ghostwritten posts, and user feedback in a local database at ~/.claude/mimiq-memory/.
  Links multiple social media profiles to a single user identity. ALWAYS trigger this skill at
  the START of every Mimiq session to load existing memory, and at the END of every session to
  save new data. Trigger on: "remember this", "save my fingerprint", "log this post", "show my
  history", "what did you find last time", "rate this post", "give feedback", "what posts have
  I written", "show my past audits", "update my profile", "which profiles are mine", "link my
  accounts", "show community insights", "opt into sharing", or any reference to past Mimiq
  sessions. Also trigger automatically after voice-capture, content-audit, or post-strategist
  completes — always save results without being asked.
---

# Mimiq Memory

Persistent memory, multi-profile identity, and feedback system for Mimiq.
All data is stored locally at `~/.claude/mimiq-memory/` — never sent anywhere.

---

## Database Structure

```
~/.claude/mimiq-memory/
├── profiles.json          # User identity + platform map
├── fingerprints.json      # Style fingerprint versions + feedback deltas
├── posts.db               # Every post written, rated, published
├── audits.db              # Every audit run + corrections
└── shared_patterns.json   # Opt-in community intelligence (anonymized)
```

All reads/writes go through the scripts in this skill's `scripts/` directory.
Always run `python3 scripts/init_db.py` first to ensure the database exists.

---

## Step 1 — Session Start: Load Memory

At the start of any Mimiq session, run:

```bash
python3 ~/.claude/skills/mimiq-memory/scripts/load_memory.py
```

This returns:
- The user's profile map (all linked platforms + handles)
- The latest style fingerprint
- Summary of past audits
- Any pending feedback requests

If no memory exists yet, initialize with:
```bash
python3 ~/.claude/skills/mimiq-memory/scripts/init_db.py
```

Then prompt the user to set up their profile (see Step 2).

---

## Step 2 — Profile Setup (First Time)

If no profile exists, ask:

> "Let's set up your Mimiq profile. What's your name or handle?
> And which platforms are you on? I'll link them all to one identity."

Collect:
- Display name / preferred handle
- Platform handles (LinkedIn, X, Reddit, Medium, Substack, Instagram, Facebook)

Save with:
```bash
python3 ~/.claude/skills/mimiq-memory/scripts/save_profile.py \
  --name "Salman" \
  --linkedin "m-salman-shahid" \
  --twitter "slayerman420" \
  --reddit "slayerman420" \
  --medium "msalman"
```

**Multi-profile linking:** If the user mentions a new handle during any session, run:
```bash
python3 ~/.claude/skills/mimiq-memory/scripts/link_platform.py \
  --platform "substack" \
  --handle "salman-writes"
```

Mimiq will automatically treat all linked handles as the same person across all skills.

---

## Step 3 — Auto-Save After Each Skill

After any Mimiq skill completes, save the output automatically:

### After voice-capture:
```bash
python3 ~/.claude/skills/mimiq-memory/scripts/save_fingerprint.py \
  --data '<fingerprint JSON>'
```

### After content-audit:
```bash
python3 ~/.claude/skills/mimiq-memory/scripts/save_audit.py \
  --platform "linkedin" \
  --data '<audit JSON>'
```

### After post-strategist writes a post:
```bash
python3 ~/.claude/skills/mimiq-memory/scripts/save_post.py \
  --platform "linkedin" \
  --topic "product launch" \
  --content '<post text>'
```

Each saved item gets a unique ID that can be used for feedback later.

---

## Step 4 — Feedback System

### Post Feedback
After every ghostwritten post, ask:

> "How did this feel? (1) Sounds exactly like me  (2) Pretty close  (3) Off — here's why: ___"

Save feedback with:
```bash
python3 ~/.claude/skills/mimiq-memory/scripts/save_feedback.py \
  --type post \
  --id <post_id> \
  --rating <1-3> \
  --notes "too formal in the opening"
```

### Audit Feedback
After every audit, ask:

> "Does this audit feel accurate? Anything missing or wrong?"

Save with:
```bash
python3 ~/.claude/skills/mimiq-memory/scripts/save_feedback.py \
  --type audit \
  --id <audit_id> \
  --notes "missed my Substack — handle is different"
```

### Fingerprint Feedback
If the user says "that doesn't sound like me" at any point:

```bash
python3 ~/.claude/skills/mimiq-memory/scripts/save_feedback.py \
  --type fingerprint \
  --id <fingerprint_id> \
  --notes "I never use rhetorical questions"
```

Fingerprint feedback automatically updates the active fingerprint rules.

---

## Step 5 — Memory Queries

Users can query their history at any time:

| User says | Action |
|---|---|
| "Show my past posts" | Run `query_posts.py --limit 10` |
| "What did my last audit say?" | Run `query_audits.py --latest` |
| "Show posts I rated highly" | Run `query_posts.py --rating 1` |
| "What feedback have I given?" | Run `query_feedback.py` |
| "What's in my fingerprint?" | Run `query_fingerprint.py` |
| "Show all my linked profiles" | Run `query_profile.py` |
| "What posts did I actually publish?" | Run `query_posts.py --published true` |

---

## Step 6 — Community Intelligence (Opt-In)

Ask the user once:

> "Would you like to contribute anonymized patterns to the Mimiq community?
> This helps surface insights like 'posts under 100 words get 3x more engagement on LinkedIn'
> — validated across real users. Your personal data is never shared, only aggregated patterns.
> (Yes / No / Ask me later)"

If yes, save opted-in status and begin contributing anonymized engagement patterns after audits.

View community insights:
```bash
python3 ~/.claude/skills/mimiq-memory/scripts/community_insights.py
```

This surfaces patterns like:
- "LinkedIn posts published Tuesday 8–10am average 40% more engagement (n=127 users)"
- "Posts with personal stories get 2.8x more comments than tips-only posts (n=89 users)"

---

## Step 7 — Session End: Save State

At the end of every session, run:
```bash
python3 ~/.claude/skills/mimiq-memory/scripts/save_session.py
```

This snapshots the current fingerprint version, logs what was done, and flags any pending
feedback items for the next session.

---

## Reference Files

- `references/schema.md` — Full database schema for all tables
- `scripts/init_db.py` — Initialize database
- `scripts/load_memory.py` — Load full memory state
- `scripts/save_profile.py` — Save/update user profile
- `scripts/link_platform.py` — Link new platform handle to existing profile
- `scripts/save_fingerprint.py` — Save new fingerprint version
- `scripts/save_audit.py` — Save audit result
- `scripts/save_post.py` — Log a ghostwritten post
- `scripts/save_feedback.py` — Save feedback on any item
- `scripts/save_session.py` — Save end-of-session snapshot
- `scripts/query_posts.py` — Query post history
- `scripts/query_audits.py` — Query audit history
- `scripts/query_feedback.py` — Query feedback history
- `scripts/query_fingerprint.py` — Query current fingerprint
- `scripts/query_profile.py` — Query user profile
- `scripts/community_insights.py` — Show community patterns
