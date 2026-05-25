# 🪞 Mimiq — Claude Skills for Social Media

Mimiq builds your personal social media system — capturing your writing voice, auditing your
best content, and ghostwriting posts that sound exactly like you.

Built by [@slayerman420](https://github.com/slayerman420)

---

## What It Does

| Skill | Purpose |
|---|---|
| `social-suite` | Master orchestrator — start here |
| `voice-capture` | Scrapes your profiles + interviews you to build a Style Fingerprint |
| `content-audit` | Finds your top-performing topics, formats, and best posting times |
| `post-strategist` | Ghostwrites full posts in your voice + recommends when to publish |
| `mimiq-memory` | Persistent memory, feedback system, multi-profile identity, community insights |

---

## How It Works

```
You → /social-suite → voice-capture → content-audit → post-strategist → ready to publish
                            ↓                ↓                ↓
                       mimiq-memory ←————————————————————————— saves everything
```

**voice-capture** scrapes your public profiles (Medium, Substack, Reddit, X) via Firecrawl,
then conducts a dynamic interview to build a precise Style Fingerprint. Falls back to manual
paste for closed platforms (LinkedIn, Facebook, Instagram).

**content-audit** pulls public engagement data to find your top posts, winning topics, and
best times to publish. Manual input fallback for closed platforms.

**post-strategist** ghostwrites complete posts using your fingerprint. Offers two timing modes:
your personal historical best times, and platform research-backed best times.

**mimiq-memory** runs at the start and end of every session. Stores all scrapes, fingerprints,
audits, and ghostwritten posts in a local database at `~/.claude/mimiq-memory/`. Links multiple
social handles to one identity. Lets you rate every post (perfect / close / off), correct audits,
and give feedback that improves your fingerprint over time. Includes an opt-in community insights
layer that surfaces anonymized patterns from other Mimiq users.

---

## Supported Platforms

| Platform   | Voice Capture                    | Engagement Data                  |
|------------|----------------------------------|----------------------------------|
| X/Twitter  | ✅ Apify (`apidojo/twitter-scraper-lite`) | ✅ Apify (`apidojo/tweet-scraper`) |
| Reddit     | ✅ Apify (`trudax/reddit-scraper`)| ✅ Apify (`trudax/reddit-scraper`)|
| Instagram  | ✅ Apify (`apify/instagram-scraper`) | ✅ Apify (`apify/instagram-scraper`) |
| Facebook   | ✅ Apify (`apify/facebook-posts-scraper`) | ✅ Apify (`apify/facebook-posts-scraper`) |
| LinkedIn   | ⚠️ Apify (`harvestapi/linkedin-profile-scraper`) | ⚠️ Limited (manual fallback) |
| Medium     | ✅ Web fetch (no actor needed)   | ✅ Web fetch                     |
| Substack   | ✅ Web fetch (no actor needed)   | ✅ Web fetch                     |

⚠️ = Actor available but platform limits public data. Manual paste fallback applies.

---

## Requirements

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) **or** Claude.ai (Pro)
- [Apify MCP](https://apify.com) connected to Claude — for scraping all platforms via Actors
- An Apify account with the required Actors installed (see table below)

> Mimiq works without Apify, but you will need to paste content manually for all platforms.

### Required Apify Actors

Each platform uses a specific Apify Actor. Install them from the Apify Store before running
voice-capture or content-audit. One Apify account runs all actors — they bill independently.

| Platform   | Actor ID                               | Used For                        |
|------------|----------------------------------------|---------------------------------|
| X/Twitter  | `apidojo/twitter-scraper-lite`         | Voice capture                   |
| X/Twitter  | `apidojo/tweet-scraper`                | Engagement audit                |
| Reddit     | `trudax/reddit-scraper`                | Voice capture + audit           |
| Instagram  | `apify/instagram-scraper`              | Voice capture + audit           |
| Facebook   | `apify/facebook-posts-scraper`         | Voice capture + audit           |
| LinkedIn   | `harvestapi/linkedin-profile-scraper`   | Voice capture + audit           |
| Medium     | *(web fetch — no actor needed)*        | Voice capture + audit           |
| Substack   | *(web fetch — no actor needed)*        | Voice capture + audit           |

Browse and install actors at **[apify.com/store](https://apify.com/store)**. Search by actor ID.
LinkedIn and Facebook public engagement data is limited — expect manual input fallback for those.

---

## Installation

### Claude Code (CLI) — One-Command Install

```bash
curl -fsSL https://raw.githubusercontent.com/slayerman420/mimiq/main/install.sh | bash
```

This installs all four skills to `~/.claude/skills/` and makes them available in every
Claude Code session.

Or manually:

```bash
git clone https://github.com/slayerman420/mimiq.git
cd mimiq
./install.sh
```

---

### Claude.ai Chat / Cowork — Manual Upload Required

> ⚠️ **There is no auto-installer for Chat or Cowork.** These are cloud-based and can't read
> from your computer's filesystem, so skills must be uploaded manually through the UI.
> This is a Claude platform limitation, not specific to Mimiq.

1. Download all four `.skill` files from the [`dist/`](dist/) folder:
   - [social-suite.skill](dist/social-suite.skill)
   - [voice-capture.skill](dist/voice-capture.skill)
   - [content-audit.skill](dist/content-audit.skill)
   - [post-strategist.skill](dist/post-strategist.skill)
2. Open Claude → **Settings → Skills → Personal Skills**
3. Click **+** and upload each `.skill` file one by one
4. All four should appear under Personal Skills with the toggle turned on

> 💡 If you're a Claude Code user too, the CLI install above is completely separate — you'll
> need to do both if you want Mimiq everywhere.

---

## Usage

### Claude Code

```
/social-suite          Full setup — start here
/voice-capture         Capture your writing style
/content-audit         Analyze your best content
/post-strategist       Ghostwrite posts in your voice
```

### Claude.ai Chat / Cowork

Skills trigger automatically. Just say:

> "Help me set up my social media system"
> "Write a LinkedIn post in my voice"
> "What are my best performing topics?"
> "Draft a week of content for me"

---

## Uninstall

```bash
./uninstall.sh
```

Or manually:
```bash
rm -rf ~/.claude/skills/social-suite
rm -rf ~/.claude/skills/voice-capture
rm -rf ~/.claude/skills/content-audit
rm -rf ~/.claude/skills/post-strategist
```

---

## File Structure

```
mimiq/
├── install.sh                     # One-command installer
├── uninstall.sh                   # Clean uninstaller
├── README.md
├── LICENSE
├── CHANGELOG.md
├── skills/                        # Skill source files
│   ├── social-suite/SKILL.md
│   ├── voice-capture/SKILL.md
│   ├── content-audit/SKILL.md
│   ├── post-strategist/SKILL.md
│   └── mimiq-memory/
│       ├── SKILL.md
│       ├── references/schema.md
│       └── scripts/               # 13 Python scripts for memory, feedback, queries
└── dist/                          # Packaged .skill files for Claude.ai upload
    ├── social-suite.skill
    ├── voice-capture.skill
    ├── content-audit.skill
    ├── post-strategist.skill
    └── mimiq-memory.skill
```

---

## Contributing

Open an issue before submitting a PR for major changes.

Ideas for future skills:
- `hashtag-strategist` — optimal hashtags per platform
- `repurpose-engine` — one post → all platforms
- `engagement-tracker` — track performance over time

---

## License

[CC BY-NC 4.0](LICENSE) — Free to use and modify. Not for commercial use. Credit required.

© 2026 slayerman420
