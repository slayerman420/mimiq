---
name: content-audit
description: >
  Analyzes a user's social media posts to surface top-performing content, winning topics, best
  formats, and optimal posting times — using Apify actors for scraping public engagement data,
  falling back to manual input when actors are unavailable. ALWAYS trigger on: "what's been
  working for me", "what should I post about", "what are my best posts", "what topics get
  engagement", "when should I post", "analyze my content", "audit my social media", "what kind
  of posts do well for me", "I want to double down on what works", "show me my top performing
  content", "what do my followers respond to", sharing a social profile URL and asking what's
  working, or any question about past post performance or building a data-driven content calendar.
  Do NOT trigger for generic social media best practices with no reference to the user's own
  content — that's web search, not an audit.
---

# Content Audit Skill

Identify what content has worked best for the user so future posts double down on winning
topics, formats, and timing.

---

## Required Apify Actors

Confirm the user has Apify connected and the following actors available before scraping.
Each actor bills independently — point the user to the Store links if any are missing.

| Platform   | Actor ID                          | Data Available                      | Apify Store |
|------------|-----------------------------------|-------------------------------------|-------------|
| X/Twitter  | `apidojo/tweet-scraper`           | Likes, retweets, replies, timestamp | [Link](https://apify.com/apidojo/tweet-scraper) |
| Reddit     | `trudax/reddit-scraper`           | Upvotes, comments, timestamp        | [Link](https://apify.com/trudax/reddit-scraper) |
| Instagram  | `apify/instagram-scraper`         | Likes, comments, timestamp          | [Link](https://apify.com/apify/instagram-scraper) |
| Facebook   | `apify/facebook-posts-scraper`    | Reactions, comments, shares         | [Link](https://apify.com/apify/facebook-posts-scraper) |
| LinkedIn   | `harvestapi/linkedin-profile-scraper` | Posts, reactions (limited)       | [Link](https://apify.com/harvestapi/linkedin-profile-scraper) |
| Medium     | Web fetch (no actor needed)       | Claps, responses                    | — |
| Substack   | Web fetch (no actor needed)       | Likes, comments                     | — |

> Medium and Substack are publicly accessible — use `web_fetch` on the archive URL directly.

---

## Step 1 — Identify Platforms to Audit

Ask which platforms to audit and collect handles for each.

---

## Step 2 — Scrape Engagement Data via Apify

Trigger each platform's actor in parallel where possible. For each post, extract:
- Post text (title or first line as identifier)
- Engagement numbers: likes / upvotes / claps / comments / shares / retweets
- Date and time posted
- Post format: long-form / short take / list / question / story / thread

**Minimum target:** 20–30 posts per platform.

### Scraping targets per platform:

**X/Twitter** (`apidojo/tweet-scraper`):
- Input: user profile URL `https://x.com/{username}`
- Sort by: most liked / most retweeted
- Extract: text, likes, retweets, replies, timestamp

**Reddit** (`trudax/reddit-scraper`):
- Input: `https://www.reddit.com/user/{username}/submitted/?sort=top`
- Extract: title, body, upvotes, comments, subreddit, timestamp

**Instagram** (`apify/instagram-scraper`):
- Input: username or profile URL
- Extract: caption, likes, comments, timestamp

**Facebook** (`apify/facebook-posts-scraper`):
- Input: public page or profile URL
- Extract: text, reactions, comments, shares, timestamp

**LinkedIn** (`harvestapi/linkedin-profile-scraper`):
- Input: profile URL
- Extract: posts, reactions (note: LinkedIn limits public engagement data)

**Medium** (web_fetch):
- URL: `https://medium.com/@{username}`
- Extract: article titles, clap counts, response counts

**Substack** (web_fetch):
- URL: author archive URL
- Extract: post titles, like counts, comment counts

If any actor fails or returns empty, skip and move to manual input for that platform.

---

## Step 3 — Manual Input for Failed / Closed Platforms

For any platform where scraping failed:

> "For [platform], could you share your top 5–10 posts with the most engagement?
> Paste the post text and give me rough numbers — even ballpark figures work."

---

## Step 4 — Rank and Cluster Posts

Sort all posts by engagement. Identify the **Top 10 Posts** overall, noting:
- Platform, topic, format, engagement numbers, date + day + time

Then cluster into **Topic Buckets**:
- Group posts by theme (e.g., "career advice", "industry hot takes", "personal stories")
- For each cluster: post count, average engagement, highest single post engagement

---

## Step 5 — Timing Analysis

From posts with timestamps:
- **Best days of week** (rank Mon–Sun by average engagement)
- **Best time of day** (morning / midday / evening / night)
- **Posting frequency patterns** (consistent weeks vs sporadic)

---

## Step 6 — Generate the Audit Report

```
## [Name]'s Content Audit Report
Platforms audited: [list]
Total posts analyzed: [n]

### 🏆 Top 10 Posts
1. [Platform] — "[Post snippet]" — [engagement] — [date]
...

### 📦 Topic Clusters (ranked by avg engagement)
1. [Cluster name] — [n posts] — avg [x] engagements
...

### 📅 Best Times to Post (from your data)
- Best days: [e.g., Tuesday, Thursday]
- Best times: [e.g., 8–10am, 6–8pm]

### 💡 Key Patterns
- [Insight 1]
- [Insight 2]

### ⚠️ What's Not Working
- [Underperforming topic or format]
```

---

## Step 7 — Save and Hand Off

Save via mimiq-memory:
```bash
python3 ~/.claude/skills/mimiq-memory/scripts/save_audit.py \
  --platform "[platform]" \
  --data '<audit JSON>' \
  --best-times "[summary]" \
  --topic-clusters "[summary]"
```

Then ask:
> "Does this match your experience? Anything missing?"
