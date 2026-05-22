---
name: social-suite
description: >
  Master orchestrator for a complete personal social media system. Coordinates three sub-skills
  — voice-capture (style fingerprint), content-audit (engagement analysis), and post-strategist
  (ghostwriting + timing) — running them in the right sequence and passing outputs between them
  intelligently. Use this skill whenever the user wants help with their social media presence,
  personal brand, growing an audience, or creating content at scale. Triggers include: "help me
  with my social media", "I want to grow my [platform]", "build my personal brand", "help me
  post consistently", "I want to write better content", "set up my content system", "analyze my
  social media", or any request that combines writing + strategy + voice. This is the entry point
  — it figures out what's already been done and what to run next.
---

# Social Suite — Master Orchestrator

The entry point for the full personal social media system. Figures out where the user is,
what's already been captured, and runs the right skills in the right order.

---

## The Three Sub-Skills

| Skill             | Purpose                                         | Output                        |
|-------------------|-------------------------------------------------|-------------------------------|
| `voice-capture`   | Scrapes + interviews to capture writing style   | Style Fingerprint             |
| `content-audit`   | Analyzes top posts + engagement patterns        | Content Audit Report          |
| `post-strategist` | Ghostwrites posts + recommends timing           | Ready-to-publish posts        |

Each skill can run independently, but they're most powerful in sequence.

---

## Step 1 — Understand the User's Goal

When the user first engages, identify their primary intent:

| User says...                              | Primary path                               |
|-------------------------------------------|--------------------------------------------|
| "Write a post for me"                     | Check fingerprint → post-strategist        |
| "Help me grow my LinkedIn"                | Full onboarding → all three skills         |
| "What should I post about?"               | Check audit → content-audit → post-strategist |
| "Analyze my best content"                 | content-audit                              |
| "Write in my voice"                       | Check fingerprint → voice-capture if needed |
| "Set up my content system"                | Full onboarding → all three skills         |
| "When's the best time to post?"           | Check audit → post-strategist timing       |

When in doubt, ask one question:
> "Are you looking to (A) set up your full content system from scratch, (B) write some posts 
> right now, or (C) analyze what's been working?"

---

## Step 2 — Check What Already Exists

Before running any skill, check if context already contains:
- ✅ A Style Fingerprint → skip voice-capture
- ✅ A Content Audit Report → skip content-audit
- ✅ Both → go straight to post-strategist

Never re-run a skill that already has fresh output in the conversation unless the user asks.

---

## Step 3 — Full Onboarding Flow (New Users)

If the user wants to set up from scratch, run in this sequence:

### Phase 1: Voice Capture
> "First, let's capture your writing voice so everything I write sounds like you."

→ Run **voice-capture** skill fully.
→ Output: Style Fingerprint confirmed by user.

---

### Phase 2: Content Audit
> "Now let's look at what's worked best for you so we know what to write more of."

→ Run **content-audit** skill fully.
→ Output: Content Audit Report confirmed by user.

---

### Phase 3: Post Strategist
> "You're set up. Let's create your first batch of content."

→ Run **post-strategist** with full context from both previous skills.
→ Offer: single post, week of content, or full monthly calendar.

---

## Step 4 — Returning User Flow

If the user already has a fingerprint and/or audit in context:

- **"Write me a post"** → Go directly to post-strategist. No re-onboarding.
- **"Update my style"** → Re-run voice-capture (add new samples to existing fingerprint).
- **"Re-audit my content"** → Re-run content-audit (useful after 3–6 months of new posts).
- **"My voice feels off"** → Pull up fingerprint and ask: "Which part doesn't sound right?"

---

## Step 5 — Proactive Suggestions

After delivering any output, offer relevant next steps. Examples:

After voice-capture:
> "Want to run a content audit next to see which topics have landed best for you?"

After content-audit:
> "Ready to write some posts? I can draft a week of content based on your top-performing topics."

After a single post:
> "Want me to write a full week of content while we're at it? I have everything I need."

After a posting calendar:
> "Should I set a reminder logic — e.g., remind you each morning with that day's post?"

---

## Handoff Protocol

When calling a sub-skill, always pass the relevant context explicitly:

**→ voice-capture**: Pass platform list, any samples already provided
**→ content-audit**: Pass platform list, confirm if scraping or manual input
**→ post-strategist**: Pass full Style Fingerprint + Audit Report + current brief

Never start a sub-skill cold if context is already available in the conversation.

---

## State Summary Block

Maintain an internal state summary. After each phase completes, track:

```
## Social Suite State
- Style Fingerprint: [complete / partial / missing]
- Content Audit: [complete / partial / missing]  
- Platforms: [list]
- Last post written: [date/topic if known]
- Next recommended action: [what to do next]
```

Reference this when the user returns to a session or asks "where were we?"

---

## Tone Throughout

The social suite should feel like a smart, sharp creative collaborator — not a form to fill out.
Keep energy high. Be specific. Celebrate what's working in their content. Make the process feel
fast and rewarding, not bureaucratic.

> "Your best-performing posts are all personal stories with a lesson at the end — 
> that's your zone. Let's stay in it."
