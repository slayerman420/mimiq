# Mimiq — Changelog

All notable changes to this project will be documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [1.2.0] — 2026-05-25

### Changed
- Replaced Firecrawl and SerpAPI with **Apify** across all scraping tasks
- `voice-capture` now uses platform-specific Apify actors for all 7 platforms
- `content-audit` now uses Apify actors for engagement data scraping
- Updated supported platforms table — Instagram, Facebook, X/Twitter now fully supported via Apify
- Added required Apify actors table to README with actor IDs and Store links

### Actors Required
| Platform | Actor ID |
|---|---|
| X/Twitter (voice) | `apidojo/twitter-scraper-lite` |
| X/Twitter (audit) | `apidojo/tweet-scraper` |
| Reddit | `trudax/reddit-scraper` |
| Instagram | `apify/instagram-scraper` |
| Facebook | `apify/facebook-posts-scraper` |
| LinkedIn | `harvestapi/linkedin-profile-scraper` |
| Medium/Substack | *(web fetch — no actor needed)* |

---

## [1.1.0] — 2026-05-23

### Added
- `mimiq-memory` — persistent memory module for Claude Code
  - Local SQLite + JSON database at `~/.claude/mimiq-memory/`
  - Multi-profile identity: links all your social handles to one user profile
  - Auto-saves every fingerprint, audit, and ghostwritten post with a unique ID
  - Feedback system: rate posts (1=perfect / 2=close / 3=off), correct audits, fix fingerprint rules
  - 13 Python scripts: init, load, save, query, and community modules
  - Community insights layer: opt-in anonymized patterns from other Mimiq users
  - Session snapshots: flags pending feedback items at end of every session
- `install.sh` now installs all 5 skills including `mimiq-memory`

---

## [1.0.0] — 2026-05-22

### Added
- `social-suite` — master orchestrator skill coordinating the full system
- `voice-capture` — style fingerprinting via Firecrawl scraping + dynamic interview
- `content-audit` — engagement analysis across open and closed platforms
- `post-strategist` — ghostwriting with dual timing recommendations (personal + research-backed)
- Support for Medium, Substack, Reddit, X/Twitter (auto-scrape)
- Support for LinkedIn, Facebook, Instagram (manual input fallback)
- Firecrawl integration for profile and post scraping
- SerpAPI integration for supplementary search
- Batch content mode (week/month of posts at once)
- Two posting time options: personal historical data vs platform research
