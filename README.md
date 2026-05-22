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

---

## How It Works

```
You → /social-suite → voice-capture → content-audit → post-strategist → ready to publish
```

**voice-capture** scrapes your public profiles (Medium, Substack, Reddit, X) via Firecrawl,
then conducts a dynamic interview to build a precise Style Fingerprint. Falls back to manual
paste for closed platforms (LinkedIn, Facebook, Instagram).

**content-audit** pulls public engagement data to find your top posts, winning topics, and
best times to publish. Manual input fallback for closed platforms.

**post-strategist** ghostwrites complete posts using your fingerprint. Offers two timing modes:
your personal historical best times, and platform research-backed best times.

---

## Supported Platforms

| Platform | Voice Capture | Engagement Data |
|---|---|---|
| Medium | ✅ Auto (Firecrawl) | ✅ Auto |
| Substack | ✅ Auto (Firecrawl) | ✅ Auto |
| Reddit | ✅ Auto (Firecrawl) | ✅ Auto |
| X / Twitter | ⚠️ Partial | ⚠️ Partial |
| LinkedIn | 📋 Manual paste | 📋 Manual paste |
| Facebook | 📋 Manual paste | 📋 Manual paste |
| Instagram | 📋 Manual paste | 📋 Manual paste |

---

## Requirements

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) **or** Claude.ai (Pro)
- [Firecrawl MCP](https://firecrawl.dev) — for automatic profile scraping (optional but recommended)
- [SerpAPI MCP](https://serpapi.com) — for supplementary search (optional)

---

## Installation

### One-Command Install (Claude Code + Chat + Cowork)

```bash
curl -fsSL https://raw.githubusercontent.com/slayerman420/mimiq/main/install.sh | bash
```

This installs all four skills globally to `~/.claude/skills/` — making them available in
Claude Code, Claude.ai Chat, and Cowork automatically.

### Manual Install

```bash
git clone https://github.com/slayerman420/mimiq.git
cd mimiq
./install.sh
```

### Claude.ai Chat / Cowork (no terminal)

1. Download the `.skill` files from the [`dist/`](dist/) folder
2. Go to **Settings → Skills → Personal Skills → +**
3. Upload each `.skill` file

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
│   └── post-strategist/SKILL.md
└── dist/                          # Packaged .skill files for Claude.ai upload
    ├── social-suite.skill
    ├── voice-capture.skill
    ├── content-audit.skill
    └── post-strategist.skill
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
