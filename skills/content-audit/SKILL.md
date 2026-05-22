---
name: content-audit
description: >
  Analyzes a user's social media posts to surface top-performing content, winning topics, best
  formats, and optimal posting times — using Firecrawl for public engagement data, falling back
  to manual input for closed platforms. ALWAYS trigger on: "what's been working for me", "what
  should I post about", "what are my best posts", "what topics get engagement", "when should I
  post", "analyze my content", "audit my social media", "what kind of posts do well for me",
  "I want to double down on what works", "show me my top performing content", "what do my
  followers respond to", sharing a social profile URL and asking what's working, or any question
  about past post performance or building a data-driven content calendar. Do NOT trigger for
  generic social media best practices with no reference to the user's own content — that's web
  search, not an audit.
---

# Content Audit Skill

Identify what content has worked best for the user, so future posts double down on winning 
topics, formats, and timing.

---

## Step 1 — Identify Platforms to Audit

Ask which platforms to audit. Note the data availability per platform:

| Platform   | Engagement Data Available?         | Method              |
|------------|------------------------------------|---------------------|
| Reddit     | ✅ Upvotes, comments (public)      | Firecrawl           |
| Medium     | ✅ Claps, responses (public)       | Firecrawl           |
| Substack   | ✅ Likes, comments (public)        | Firecrawl           |
| X/Twitter  | ⚠️ Likes/reposts (partial/public) | Firecrawl           |
| LinkedIn   | ❌ Reactions hidden behind login   | Manual input        |
| Facebook   | ❌ Behind login                    | Manual input        |
| Instagram  | ❌ Behind login                    | Manual input        |

---

## Step 2 — Scrape Open Platforms

Use Firecrawl to scrape the user's profile pages on open platforms.

**For each post, extract:**
- Post title or first line (as identifier)
- Full or truncated body text
- Engagement numbers: upvotes/likes/claps/comments/shares/reposts
- Date posted (if visible)
- Post format: long-form essay / short take / list / question / story / thread

**Scraping targets:**
- Reddit: `https://www.reddit.com/user/{username}/submitted/?sort=top`
- Medium: `https://medium.com/@{username}` (look for clap counts)
- Substack: Author's archive page
- X/Twitter: `https://twitter.com/{username}` (public profile)

Attempt to collect **at least 20–30 posts** per platform where possible.
If Firecrawl is blocked or returns empty results, skip and move to manual input for that platform.

---

## Step 3 — Manual Input for Closed Platforms

For LinkedIn, Facebook, Instagram (or any failed scrape), ask:

> "For [platform], could you share your top 5–10 posts that got the most engagement?
> Just paste the post text and tell me roughly how many likes/comments/shares each got.
> Even ballpark numbers are fine — 'a lot', 'a little', '200 likes' all work."

Accept whatever level of detail they provide.

---

## Step 4 — Rank and Cluster Posts

Once data is collected, sort all posts by engagement score (normalize across platforms if needed).

**Identify the Top 10 Posts overall**, noting:
- Platform
- Topic / subject matter
- Format (list, story, hot take, question, etc.)
- Engagement numbers
- Date + day of week + approximate time (if available)

Then cluster posts into **Topic Buckets** — groups of posts that share a theme:

Example clusters:
- "Career advice / lessons learned"
- "Industry commentary / hot takes"
- "Personal stories / vulnerability"
- "How-to / tactical tips"
- "Humor / observations"

For each cluster, calculate:
- Number of posts in cluster
- Average engagement per post in cluster
- Highest single post engagement in cluster

---

## Step 5 — Timing Analysis

From posts where date/time is available:

- **Best days of week** (rank Mon–Sun by average engagement)
- **Best time of day** (if timestamp data is available — group into morning / midday / evening / night)
- **Posting frequency patterns** (did consistent posting weeks outperform sporadic ones?)

If timestamps are unavailable, note this and defer to platform research in post-strategist.

---

## Step 6 — Generate the Audit Report

Output a structured **Content Audit Report**:

```
## [Name]'s Content Audit Report
Generated: [date]
Platforms audited: [list]
Total posts analyzed: [n]

---

### 🏆 Top 10 Posts
1. [Platform] — "[Post snippet]" — [engagement] — [date if known]
2. ...

---

### 📦 Topic Clusters (ranked by avg engagement)
1. **[Cluster name]** — [n posts] — avg [x] engagements — best: [top post snippet]
2. ...

---

### 📅 Best Times to Post (from your data)
- Best days: [e.g., Tuesday, Thursday]
- Best times: [e.g., 8–10am, 6–8pm]
- Note: [any caveats about data availability]

---

### 💡 Key Patterns Observed
- [Insight 1: e.g., "Posts with personal stories get 3x more comments than tips"]
- [Insight 2: e.g., "Questions outperform statements on LinkedIn"]
- [Insight 3: e.g., "Your shortest posts (under 100 words) consistently outperform long ones on X"]

---

### ⚠️ What's Not Working
- [Topic or format that underperforms]
- [Platform where engagement is consistently low]
```

---

## Step 7 — Confirm & Hand Off

Present the report and ask:
> "Does this match your experience? Any posts you'd add or context I should know?"

Incorporate corrections. Then note:
> "This audit is ready for the post-strategist, which will use these patterns to help you
> plan and write future content."
