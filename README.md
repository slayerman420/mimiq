# 🪞 Mimiq — Claude Skills for Social Media

Mimiq builds your personal social media system — capturing your writing voice, auditing your
best content, and ghostwriting posts that sound exactly like you.

Built by [@slayerman420](https://github.com/slayerman420)

---

## What It Does

| Skill | Purpose |
|---|---|
| `social-suite` | Master orchestrator — runs everything in the right order |
| `voice-capture` | Scrapes your public profiles + interviews you to build a Style Fingerprint |
| `content-audit` | Analyzes your top posts to find winning topics, formats, and posting times |
| `post-strategist` | Ghostwrites full posts in your voice + recommends when to publish |

---

## How It Works

```
You → social-suite → voice-capture → content-audit → post-strategist → posts ready to publish
```

**voice-capture** tries to scrape your public profiles automatically (Medium, Substack, Reddit,
X/Twitter) via Firecrawl. For closed platforms (LinkedIn, Facebook, Instagram), it falls back to
a dynamic interview and lets you paste samples manually.

**content-audit** pulls public engagement data (upvotes, claps, likes) from open platforms.
For closed platforms, you provide your top posts and rough engagement numbers.

**post-strategist** writes complete, ready-to-publish posts using your style fingerprint. It
offers two timing options: your personal best times (from your audit data) and platform
research-backed best times.

---

## Supported Platforms

| Platform | Voice Capture | Engagement Scraping |
|---|---|---|
| Medium | ✅ Auto (Firecrawl) | ✅ Auto |
| Substack | ✅ Auto (Firecrawl) | ✅ Auto |
| Reddit | ✅ Auto (Firecrawl) | ✅ Auto |
| X / Twitter | ⚠️ Partial (public profiles) | ⚠️ Partial |
| LinkedIn | 📋 Manual paste | 📋 Manual paste |
| Facebook | 📋 Manual paste | 📋 Manual paste |
| Instagram | 📋 Manual paste | 📋 Manual paste |

---

## Requirements

- A [Claude.ai](https://claude.ai) account (Pro recommended) **or** Claude Code (CLI)
- [Firecrawl MCP](https://firecrawl.dev) connected to Claude — for automatic profile scraping
- [SerpAPI MCP](https://serpapi.com) connected to Claude — optional, improves search results

> Mimiq works without Firecrawl/SerpAPI, but you'll need to paste content manually for all
> platforms.

---

## Installation

### Claude.ai (Web / Mobile / Desktop)

Install `social-suite` first — it orchestrates the other three automatically.

1. Download [`dist/social-suite.skill`](dist/social-suite.skill)
2. Open [Claude.ai](https://claude.ai) → Settings → Skills
3. Drag and drop the `.skill` file to install
4. Repeat for the remaining three skills

Install individually if you only need specific functionality:
- [`dist/voice-capture.skill`](dist/voice-capture.skill)
- [`dist/content-audit.skill`](dist/content-audit.skill)
- [`dist/post-strategist.skill`](dist/post-strategist.skill)

---

### Claude Code (CLI)

**Option A — Clone the full repo (all 4 skills at once)**

```bash
git clone https://github.com/slayerman420/mimiq.git ~/.claude/skills/mimiq
```

**Option B — Install individual skills**

```bash
# social-suite (recommended first)
mkdir -p ~/.claude/skills/social-suite
curl -o ~/.claude/skills/social-suite/SKILL.md \
  https://raw.githubusercontent.com/slayerman420/mimiq/main/skills/social-suite/SKILL.md

# voice-capture
mkdir -p ~/.claude/skills/voice-capture
curl -o ~/.claude/skills/voice-capture/SKILL.md \
  https://raw.githubusercontent.com/slayerman420/mimiq/main/skills/voice-capture/SKILL.md

# content-audit
mkdir -p ~/.claude/skills/content-audit
curl -o ~/.claude/skills/content-audit/SKILL.md \
  https://raw.githubusercontent.com/slayerman420/mimiq/main/skills/content-audit/SKILL.md

# post-strategist
mkdir -p ~/.claude/skills/post-strategist
curl -o ~/.claude/skills/post-strategist/SKILL.md \
  https://raw.githubusercontent.com/slayerman420/mimiq/main/skills/post-strategist/SKILL.md
```

After installing, restart Claude Code. Then verify with:

```bash
ls ~/.claude/skills/
```

You can invoke skills directly with `/social-suite`, `/voice-capture`, etc., or just describe
what you want and Claude will load the right skill automatically.

**Option C — Project-level install (team use)**

If you want Mimiq available to everyone on a shared codebase:

```bash
# From your project root
git clone https://github.com/slayerman420/mimiq.git .claude/skills/mimiq
```

Then commit `.claude/skills/` to your repo so every team member gets it automatically.

---

## Usage

### Full Setup (recommended for first-time users)

Say any of the following to Claude:

> "Help me set up my social media system"
> "I want to build my personal brand on LinkedIn"
> "Set up Mimiq from scratch"

`social-suite` will guide you through the full flow automatically.

### Quick Actions (once set up)

| What you want | What to say |
|---|---|
| Write a post | "Write me a LinkedIn post about [topic]" |
| Week of content | "Draft a week of content for me" |
| Audit your posts | "Analyze my best content" |
| Update your voice | "Update my writing style" |
| Best time to post | "When should I post today?" |

---

## File Structure

```
mimiq/
├── README.md
├── LICENSE
├── CHANGELOG.md
├── skills/                        # Source SKILL.md files (human-readable)
│   ├── social-suite/SKILL.md      # Master orchestrator
│   ├── voice-capture/SKILL.md     # Style fingerprinting
│   ├── content-audit/SKILL.md     # Engagement analysis
│   └── post-strategist/SKILL.md   # Ghostwriting + timing
└── dist/                          # Packaged .skill files for Claude.ai drag-and-drop
    ├── social-suite.skill
    ├── voice-capture.skill
    ├── content-audit.skill
    └── post-strategist.skill
```

---

## Contributing

Contributions welcome. Please open an issue before submitting a PR for major changes.

Ideas for future Mimiq skills:
- `hashtag-strategist` — researches optimal hashtags per platform
- `repurpose-engine` — converts one post into versions for all platforms
- `engagement-tracker` — tracks post performance over time

---

## License

[CC BY-NC 4.0](LICENSE) — Free to use and modify. Not for commercial use. Credit required.

© 2026 slayerman420
