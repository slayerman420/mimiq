# Mimiq Memory — Database Schema

## profiles.json
```json
{
  "name": "string",
  "platforms": {
    "linkedin": "handle",
    "twitter": "handle",
    "reddit": "handle",
    "medium": "handle",
    "substack": "handle",
    "instagram": "handle",
    "facebook": "handle"
  },
  "community_opt_in": true | false | null,
  "created_at": "ISO8601",
  "updated_at": "ISO8601"
}
```

## fingerprints.json
```json
{
  "active_id": "abc12345",
  "versions": [
    {
      "id": "abc12345",
      "version": 1,
      "data": { ... fingerprint object ... },
      "feedback_count": 3,
      "feedback_deltas": [
        { "id": "fb001", "notes": "never use rhetorical questions", "created_at": "ISO8601" }
      ],
      "created_at": "ISO8601"
    }
  ]
}
```

## posts.db
| Column | Type | Notes |
|---|---|---|
| id | TEXT PK | Short UUID |
| platform | TEXT | linkedin, twitter, etc. |
| topic | TEXT | Brief topic description |
| content | TEXT | Full post text |
| rating | INTEGER | 1=perfect, 2=close, 3=off |
| notes | TEXT | Feedback notes |
| published | INTEGER | 0=draft, 1=published |
| created_at | TEXT | ISO8601 |
| updated_at | TEXT | ISO8601 |

## post_feedback
| Column | Type | Notes |
|---|---|---|
| id | TEXT PK | |
| post_id | TEXT FK | References posts.id |
| rating | INTEGER | 1-3 |
| notes | TEXT | |
| created_at | TEXT | ISO8601 |

## audits.db
| Column | Type | Notes |
|---|---|---|
| id | TEXT PK | Short UUID |
| platform | TEXT | Platform audited |
| data | TEXT | Full audit JSON |
| top_posts | TEXT | Summary of top posts |
| best_times | TEXT | Best posting times |
| topic_clusters | TEXT | Topic cluster summary |
| created_at | TEXT | ISO8601 |

## audit_feedback
| Column | Type | Notes |
|---|---|---|
| id | TEXT PK | |
| audit_id | TEXT FK | References audits.id |
| notes | TEXT | |
| created_at | TEXT | ISO8601 |

## shared_patterns.json
```json
{
  "patterns": [
    {
      "insight": "string",
      "platform": "string",
      "confidence": "high | medium | low",
      "sample_size": "n=127 users"
    }
  ],
  "last_updated": "ISO8601"
}
```
