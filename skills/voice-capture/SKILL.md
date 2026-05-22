---
name: voice-capture
description: >
  Builds a reusable Style Fingerprint of a person's writing voice by scraping public social
  profiles via Firecrawl and conducting a dynamic interview. ALWAYS trigger before writing any
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

## Step 1 — Identify Platforms

Ask the user which platforms they're active on. Supported:

| Platform   | Scrapable? | Method                          |
|------------|------------|---------------------------------|
| Medium     | ✅ Yes     | Firecrawl                       |
| Substack   | ✅ Yes     | Firecrawl                       |
| Reddit     | ✅ Yes     | Firecrawl                       |
| X/Twitter  | ⚠️ Partial | Firecrawl (public profiles only)|
| LinkedIn   | ❌ No      | Manual paste                    |
| Facebook   | ❌ No      | Manual paste                    |
| Instagram  | ❌ No      | Manual paste (captions)         |

---

## Step 2 — Scrape Open Platforms

For each scrapable platform, use Firecrawl to pull the user's public posts.

**Scraping targets:**
- Medium: `https://medium.com/@{username}`
- Substack: `https://{publication}.substack.com/` or author archive
- Reddit: `https://www.reddit.com/user/{username}/submitted/`
- X/Twitter: `https://twitter.com/{username}` (public only)

**What to extract per post:**
- Full post text / caption / comment body
- Approximate length
- Any notable formatting patterns (lists, questions, em dashes, etc.)

Aim for **15–30 posts minimum** across platforms for a reliable fingerprint.
If Firecrawl fails or returns blocked/empty content, skip silently and move to Step 3.

---

## Step 3 — Request Manual Samples (Closed Platforms)

For LinkedIn, Facebook, Instagram — or if scraping failed — ask the user:

> "Could you paste 5–10 of your posts from [platform]? Any mix of short and long ones works best.
> Don't worry about formatting — raw text is fine."

Accept whatever they provide. Even 3 posts is enough to start.

---

## Step 4 — Dynamic Style Interview

Once you have scraped/pasted content, conduct a **dynamic interview** to fill gaps.

Start with these core questions, then follow up based on answers:

1. **Tone** — "How would you describe your writing style in 3 words? (e.g., direct, warm, technical)"
2. **Audience** — "Who do you primarily write for?"
3. **Purpose** — "What do you want people to feel or do after reading your posts?"
4. **Pet phrases** — "Are there any words, phrases, or expressions you use a lot?"
5. **What to avoid** — "Is there anything you'd never say or a tone you'd never want?"
6. **Post structure** — "Do you tend to open with a hook, a question, a story? How do you usually end?"

**Dynamic follow-up rules:**
- If they say "casual" → ask about emoji and slang usage
- If they say "professional" → ask if they ever inject humor or personal stories
- If they mention a niche → ask about jargon comfort level
- If answers are vague → ask them to react to two contrasting example sentences ("Which sounds more like you?")

Keep going until you have confident signal on all fingerprint dimensions below.

---

## Step 5 — Build the Style Fingerprint

Synthesize scraped content + interview into a structured **Style Fingerprint document**.

```
## [Name]'s Style Fingerprint

### Voice & Tone
- Overall tone: [e.g., conversational, authoritative, witty]
- Energy level: [e.g., calm and measured / punchy and fast]
- Humor: [none / dry / self-deprecating / frequent]
- Warmth: [distant / neutral / warm / very personal]

### Sentence & Structure Patterns
- Average sentence length: [short / medium / long / mixed]
- Paragraph length: [1-liner punches / medium blocks / long-form]
- Signature openings: [e.g., starts with a question, a bold claim, a story]
- Signature closings: [e.g., ends with a CTA, a reflection, a one-liner]
- List usage: [never / occasionally / frequent]
- Rhetorical questions: [never / sometimes / often]

### Vocabulary
- Complexity: [plain language / moderate / technical]
- Pet phrases/words: [list them]
- Industry jargon comfort: [avoids / uses selectively / uses freely]
- Emoji usage: [none / occasional / frequent — which ones?]

### What They NEVER Do
- [e.g., never uses exclamation points, never writes in first person plural, never uses corporate speak]

### Platform-Specific Notes
- LinkedIn: [any differences in formality, length, CTA style]
- X/Twitter: [hook style, thread vs single post preference]
- Instagram: [caption style, hashtag usage]
- [etc.]

### Sample Phrases (verbatim from their writing)
- "[phrase 1]"
- "[phrase 2]"
- "[phrase 3]"

### Ghost-writing Rules
1. [Specific rule derived from their style]
2. [Another specific rule]
3. [etc.]
```

---

## Step 6 — Confirm & Save

Present the fingerprint to the user and ask:
> "Does this feel accurate? Anything that's off or missing?"

Incorporate any corrections. Then tell the user:
> "Your style fingerprint is ready. Claude will use this whenever writing content for you.
> You can also reference it by asking me to 'write in my voice.'"

Store or reference the fingerprint in any follow-up ghostwriting session.

---

## Quality Bar

A good fingerprint should allow a third party to read two posts — one real, one ghostwritten — 
and be unable to tell which is which. If you're not confident the fingerprint achieves this, 
ask more questions before finishing.
