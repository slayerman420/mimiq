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

This is the recommended way to install Mimiq.

1. Download all four `.skill` files from the [`dist/`](dist/) folder
2. Open [Claude.ai](https://claude.ai) → Settings → Skills
3. Drag and drop each `.skill` file to install
4. All four skills must be installed for the full system to work

Install individually if you only need specific functionality:
- [`dist/social-suite.skill`](dist/social-suite.skill) — orchestrator (install this first)
- [`dist/voice-capture.skill`](dist/voice-capture.skill) — style fingerprinting
- [`dist/content-audit.skill`](dist/content-audit.skill) — engagement analysis
- [`dist/post-strategist.skill`](dist/post-strategist.skill) — ghostwriting + timing

---

### Claude Code (CLI)

Skills in Claude Code live inside your **project directory** under `.claude/skills/`.

**Option A — Clone the full repo into your project**

```bash
# From your project root
git clone https://github.com/slayerman420/mimiq.git .claude/skills/mimiq
```

**Option B — Copy only the SKILL.md files you need**

```bash
# Create the skills directory in your project
mkdir -p .claude/skills/social-suite
mkdir -p .claude/skills/voice-capture
mkdir -p .claude/skills/content-audit
mkdir -p .claude/skills/post-strategist

# Copy each skill
curl -o .claude/skills/social-suite/SKILL.md \
  https://raw.githubusercontent.com/slayerman420/mimiq/main/skills/social-suite/SKILL.md

curl -o .claude/skills/voice-capture/SKILL.md \
  https://raw.githubusercontent.com/slayerman420/mimiq/main/skills/voice-capture/SKILL.md

curl -o .claude/skills/content-audit/SKILL.md \
  https://raw.githubusercontent.com/slayerman420/mimiq/main/skills/content-audit/SKILL.md

curl -o .claude/skills/post-strategist/SKILL.md \
  https://raw.githubusercontent.com/slayerman420/mimiq/main/skills/post-strategist/SKILL.md
```

**Option C — Team/shared project install**

Commit the `.claude/skills/` directory to your repo so every team member gets Mimiq automatically when they clone the project.

```bash
git add .claude/skills/
git commit -m "Add Mimiq skills"
```

> **Note:** Skills in Claude Code are project-scoped, not global. You need to install them
> inside each project where you want to use them.

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
└── dist/                          # Packaged .skill files for Claude.ai
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
