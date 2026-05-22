---
name: post-strategist
description: >
  Ghostwrites full social media posts in the user's exact voice and recommends optimal posting
  times, using the user's style fingerprint (from voice-capture) and content audit (from
  content-audit). Offers two timing modes: personal best times (based on the user's own
  historical data) and research-backed best times (platform-wide data). Use this skill whenever
  the user wants to create posts, write content for social media, asks "write a post for me",
  "draft something for LinkedIn/X/Instagram", "what should I post today", "write this in my
  voice", "create content for [platform]", or wants a posting schedule. If no style fingerprint
  exists, trigger voice-capture first. If no content audit exists, offer to run content-audit
  first or proceed without it.
---

# Post Strategist Skill

Ghostwrite posts that sound exactly like the user and tell them the best time to publish them.

---

## Prerequisites Check

Before writing, verify what context you have:

| Context Needed         | If Available          | If Missing                                      |
|------------------------|-----------------------|-------------------------------------------------|
| Style Fingerprint      | Use it directly       | Ask user to run voice-capture first (required)  |
| Content Audit Report   | Use it for topics     | Ask if they want to run content-audit, or proceed without|
| Target platform        | Use platform rules    | Ask user which platform(s) to write for         |
| Topic / brief          | Use it                | Ask: "What do you want this post to be about?"  |

Never ghostwrite without a style fingerprint. Everything else is optional but improves output.

---

## Step 1 — Get the Brief

Ask the user (or infer from context):

1. **Platform** — LinkedIn / X / Instagram / Facebook / Reddit / Medium / Substack?
2. **Topic** — What is the post about? (Can be a vague idea — "something about leadership" is fine)
3. **Goal** — Inform / inspire / promote / entertain / spark debate?
4. **Length preference** — Short (under 100 words) / medium / long-form? Or match their typical style?
5. **Any must-include elements?** — A specific link, CTA, event, announcement?

If they're vague, suggest topics from their **top-performing clusters** in the audit report.

---

## Step 2 — Ghostwrite the Post

Apply the style fingerprint strictly. Checklist before writing:

- [ ] Tone matches their fingerprint (casual/formal/witty/warm/etc.)
- [ ] Sentence length matches their pattern
- [ ] Opens the way they typically open (hook, question, story, bold claim)
- [ ] Closes the way they typically close (CTA, reflection, one-liner)
- [ ] Vocabulary matches — their words, not generic words
- [ ] Emoji usage matches their pattern (frequency + which ones)
- [ ] No phrases or patterns in their "NEVER DO" list
- [ ] Platform-appropriate format (e.g., LinkedIn ≠ Twitter ≠ Instagram)

**Platform-specific formatting rules:**

### LinkedIn
- Optimal length: 150–300 words for engagement; long-form (600–1200w) for thought leadership
- Line breaks after every 1–2 sentences (LinkedIn compresses walls of text)
- Open with a hook line that stands alone (visible before "see more")
- Hashtags: 3–5 max, at the end
- CTAs work well ("What do you think?" / "Drop your experience below")

### X / Twitter
- Single tweet: under 280 chars
- Thread: number tweets (1/ 2/ 3/) if multi-part
- Hook tweet must be punchy — no fluff
- No hashtags unless trending/niche; 0–2 max
- Conversational, not corporate

### Instagram
- Caption length: 125–150 chars for casual; up to 2,200 for storytelling
- First line must hook before truncation
- Hashtags: 5–15 in first comment or end of caption
- Emojis used as line breaks or accents (if their fingerprint supports this)
- CTA: "Save this", "Tag someone", "Comment below"

### Facebook
- Conversational, personal tone performs best
- Medium length: 40–80 words for engagement; longer for personal stories
- Questions drive comments
- Avoid links in the post body (reduces reach); put in comments

### Reddit
- Match subreddit culture precisely (ask which subreddit if relevant)
- Title is critical — front-load the value
- Body: be genuine, don't sound promotional
- No self-promotion unless in designated threads

### Medium / Substack
- Long-form: 800–2,500 words typical
- Headline is everything — make it specific and compelling
- Use subheadings every 200–300 words
- End with a clear takeaway or reflection

---

## Step 3 — Provide Two Timing Options

Always offer both options. Present them clearly:

### Option A: Your Personal Best Times
*(From content audit — only available if audit was run)*

> Based on your past posts, your best engagement times are:
> - **[Platform]**: [Day] at [Time] — your posts average [x]% more engagement
> - [etc.]

If no audit data is available: "Run content-audit to unlock your personal timing data."

### Option B: Platform Research Best Times
*(Use web_search to fetch current platform-specific best time data if needed)*

General research-backed guidelines (always search for latest data before presenting):

| Platform  | Best Days          | Best Times (local)         |
|-----------|--------------------|----------------------------|
| LinkedIn  | Tue, Wed, Thu      | 8–10am, 12pm, 5–6pm        |
| X/Twitter | Mon–Thu            | 8am, 12pm, 5pm             |
| Instagram | Mon, Wed, Fri      | 11am–1pm, 7–9pm            |
| Facebook  | Tue–Thu            | 1–4pm                      |
| Reddit    | Mon–Fri            | 9am–12pm (varies by sub)   |

Always note: *"These are averages across millions of accounts. Your personal data (Option A) 
is more reliable for your specific audience."*

---

## Step 4 — Deliver Output

Present the ghostwritten post clearly, then the timing recommendations:

```
---
✍️ YOUR POST ([Platform])
---

[Full post text, formatted for the platform]

---
📅 WHEN TO POST
---

Option A — Your Data: [Timing from audit]
Option B — Platform Research: [Day] at [Time] ([source/rationale])

💡 Recommendation: [Which option to choose and why, given their situation]

---
```

---

## Step 5 — Iterate

Ask: "How does this feel? Too formal / too casual / not quite your voice?"

Apply fingerprint corrections dynamically. If they say it's off, ask:
- "Which part doesn't sound like you?"
- "Can you show me a sentence you'd rewrite?"

Update the style fingerprint notes if a consistent pattern emerges from corrections.

---

## Batch Mode

If the user wants multiple posts at once (e.g., "write a week of content"):

1. Confirm platforms, topics, and posting frequency
2. Suggest a content mix based on their top-performing clusters
3. Draft all posts
4. Provide a full posting calendar with timing for each

Format as a table:

| Day       | Platform  | Topic/Angle         | Post Snippet          | Recommended Time |
|-----------|-----------|---------------------|-----------------------|------------------|
| Monday    | LinkedIn  | [topic]             | [first line...]       | 8:30am           |
| Tuesday   | X         | [topic]             | [first line...]       | 12:00pm          |
| ...       | ...       | ...                 | ...                   | ...              |
