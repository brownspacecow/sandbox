# AGENTS.md

This file guides the daily content updates to this repository so they stay
readable and consistent in style. It is read by the automation agent that
produces each daily-content post.

## Scope

The daily-content posts live in `_posts/` and are rendered by the Jekyll
site at `brownspacecow.github.io/sandbox`. Each post covers one day of
fantasy football, Siouxland & Iowa news, and a short "More for Greg"
section.

## Post format

Every post is a Markdown file in `_posts/` named `YYYY-MM-DD-slug.md`
with Jekyll front matter:

```yaml
---
layout: default
title: "Daily Content for Greg – YYYY-MM-DD (Week N)"
date: YYYY-MM-DD
excerpt: One-sentence summary of the day's content.
---
```

Required sections, in this order:

1. `## Summary` — one short paragraph.
2. `## Fantasy Football (Week N)` — bullet items, each with a source link.
3. `## Around Siouxland & Iowa` — bullet items, each with a source link.
4. `## More for Greg` — bullet items, each with a source link. Omit the
   whole section when nothing is verifiable.
5. `## Sources` — one bullet per source URL, in the order first cited.
6. A closing line: `[&larr; Back to homepage]({{ '/' | relative_url }})`

## Style rules

- Use sentence case for section titles.
- Use bullet items (`•`), not `-` or `*`.
- Each bullet names what happened, why it matters, and ends with the
  source in brackets: `[Source Name](url)`.
- Do not publish unverified information. If a source is JS-heavy,
  paywalled, or otherwise inaccessible, omit that section rather than
  guessing.
- Keep the tone plain and direct. Avoid hype, speculation, and
  first-person language.
- The excerpt should be a single sentence, no longer than about 30 words.

## How a post is produced

1. The agent reads the issue it is implementing and gathers the day's
   content itself from primary sources.
2. It writes the post into `_posts/` following the format above.
3. It commits the post on its working branch and opens a pull request.
4. The post must render under Jekyll; check that the front matter is
   valid and every relative URL uses `{{ '/' | relative_url }}`.
