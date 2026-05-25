---
name: voice-capture
description: >
  Builds a reusable Style Fingerprint of a person's writing voice by scraping public social
  profiles via Apify actors and conducting a dynamic interview. ALWAYS trigger before writing any
  social media post or content "in someone's voice." Trigger on: "write like me", "sound like me",
  "in my voice", "match my tone", "write how I write", "that doesn't sound like me", "make it more
  me", "capture my style", "learn my style", "ghostwrite for me", "write my LinkedIn post", "write
  my tweets", sharing a social profile URL to write content, pasting sample posts and asking for
  more like them, or any request mimicking personal writing style. Also trigger when the user seems
  unhappy with Claude's writing — missing fingerprint is usually why. Do NOT skip this just because
  the user gave an inline sample; this skill builds a richer, persistent fingerprint.
---

# Voice Capture Skill

Build a precise, reusable **Style Fingerprint** for a user so Claude can ghostwrite content that
sounds exactly like them.

---

## Required Apify Actors

Before scraping, confirm the user has connected Apify and has the following actors available.
Each actor must be enabled in their Apify account. Direct the user to the Apify Store links below
if any are missing.

| Platform   | Actor ID                          | Apify Store |
|------------|-----------------------------------|-------------|
| X/Twitter  | `apidojo/twitter-scraper-lite`    | [Link](https://apify.com/apidojo/twitter-scraper-lite) |
| Reddit     | `trudax/reddit-scraper`           | [Link](https://apify.com/trudax/reddit-scraper) |
| Instagram  | `apify/instagram-scraper`         | [Link](https://apify.com/apify/instagram-scraper) |
| Facebook   | `apify/facebook-posts-scraper`    | [Link](https://apify.com/apify/facebook-posts-scraper) |
| LinkedIn   | `apimaestro/linkedin-profile-detail` | [Link](https://apify.com/apimaestro/linkedin-profile-detail) |
| Medium     | Web fetch (no actor needed)       | — |
| Substack   | Web fetch (no actor needed)       | — |

> Medium and Substack are publicly accessible — use `web_fetch` directly on the profile/archive
> URL. No Apify actor required.

If the user hasn't connected Apify or is missing an actor, skip that platform and fall back to
manual paste (Step 3).

---

## Step 1 — Identify Platforms

Ask the user which platforms they're active on and collect their handle for each.

---

## Step 2 — Scrape via Apify

For each platform where the user has provided a handle and the actor is available, trigger the
appropriate Apify actor via the Apify MCP tool.

**What to extract per post:**
- Full post text / caption / comment body
- Approximate length
- Formatting patterns (lists, questions, em dashes, etc.)

Aim for **15–30 posts minimum** across all platforms for a reliable fingerprint.

### Platform scraping targets:

**X/Twitter** (`apidojo/twitter-scraper-lite`):
- Input: `https://x.com/{username}`
- Extract: tweet text, timestamp, likes, retweets

**Reddit** (`trudax/reddit-scraper`):
- Input: `https://www.reddit.com/user/{username}/submitted/`
- Extract: post title, body text, upvotes, comments, subreddit

**Instagram** (`apify/instagram-scraper`):
- Input: Instagram username or profile URL
- Extract: caption text, likes, comments, timestamp

**Facebook** (`apify/facebook-posts-scraper`):
- Input: public page or profile URL
- Extract: post text, reactions, comments, timestamp

**LinkedIn** (`apimaestro/linkedin-profile-detail`):
- Input: LinkedIn profile URL
- Extract: posts, articles, engagement data

**Medium** (web_fetch):
- URL: `https://medium.com/@{username}`
- Extract: article titles, clap counts, article body

**Substack** (web_fetch):
- URL: `https://{publication}.substack.com/`
- Extract: post titles, content, like counts

If any actor call fails or returns empty results, skip that platform silently and move to Step 3.

---

## Step 3 — Request Manual Samples (Fallback)

For any platform where scraping failed or the actor is unavailable:

> "Could you paste 5–10 of your posts from [platform]? Any mix of short and long ones works best.
> Raw text is fine."

Accept whatever they provide. Even 3 posts is enough to start.

---

## Step 4 — Dynamic Style Interview

Once you have scraped/pasted content, conduct a **dynamic interview** to fill gaps.

Start with these core questions, then follow up based on answers:

1. **Tone** — "How would you describe your writing style in 3 words?"
2. **Audience** — "Who do you primarily write for?"
3. **Purpose** — "What do you want people to feel or do after reading your posts?"
4. **Pet phrases** — "Any words or expressions you use a lot?"
5. **What to avoid** — "Anything you'd never say or a tone you'd never want?"
6. **Post structure** — "How do you typically open and close posts?"

**Dynamic follow-up rules:**
- If they say "casual" → ask about emoji and slang usage
- If they say "professional" → ask if they inject humor or personal stories
- If they mention a niche → ask about jargon comfort level
- If answers are vague → ask them to react to two contrasting example sentences

---

## Step 5 — Build the Style Fingerprint

Synthesize scraped content + interview into a structured **Style Fingerprint document**:

```
## [Name]'s Style Fingerprint

### Voice & Tone
- Overall tone: [e.g., conversational, authoritative, witty]
- Energy level: [calm / punchy]
- Humor: [none / dry / self-deprecating / frequent]
- Warmth: [distant / neutral / warm / very personal]

### Sentence & Structure Patterns
- Average sentence length: [short / medium / long / mixed]
- Paragraph length: [1-liner / medium / long-form]
- Signature openings: [e.g., starts with a question, bold claim, story]
- Signature closings: [e.g., CTA, reflection, one-liner]
- List usage: [never / occasionally / frequent]
- Rhetorical questions: [never / sometimes / often]

### Vocabulary
- Complexity: [plain / moderate / technical]
- Pet phrases/words: [list them]
- Jargon comfort: [avoids / selective / freely]
- Emoji usage: [none / occasional / frequent]

### What They NEVER Do
- [e.g., never uses exclamation points]

### Platform-Specific Notes
- LinkedIn: [formality, length, CTA style]
- X/Twitter: [hook style, thread vs single]
- Instagram: [caption style, hashtag usage]

### Sample Phrases (verbatim)
- "[phrase 1]"
- "[phrase 2]"

### Ghost-writing Rules
1. [Specific rule]
2. [Another rule]
```

---

## Step 6 — Confirm & Save

Present the fingerprint and ask:
> "Does this feel accurate? Anything off or missing?"

Incorporate corrections, then save via mimiq-memory:
```bash
python3 ~/.claude/skills/mimiq-memory/scripts/save_fingerprint.py --data '<fingerprint JSON>'
```

---

## Quality Bar

A good fingerprint should make it impossible to tell ghostwritten posts from real ones.
If you're not confident it achieves this, ask more questions before finishing.
