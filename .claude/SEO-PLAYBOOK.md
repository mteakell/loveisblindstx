# Sable Society SEO playbook

Applies to every client website: building pages, writing content, auditing, link building and reporting. Where a rule here conflicts with a client's own instructions, follow the client's and say so.

## 1. Site structure

- Every important page sits within three clicks of the homepage. Flat beats deep.
- Each service or product has one core (money) page. Every supporting page links to the core page it supports, with anchor text that says what the target is about. Never "click here".
- No orphans: every URL in the sitemap is linked from at least one crawlable page.
- Supporting pages come in two kinds: authority articles (how to choose, how it works) and comparison pages (X vs Y, cost over time). Grow them around each core page as the client's services warrant.
- Fix any redirect chain of two or more hops. Block or canonicalise parameter URLs (`?`).
- Quarterly 30-minute audit (Screaming Frog, free up to 500 URLs): crawl depth 4 or more, sitemap URLs the crawl never found, redirect chains, important pages with fewer than 5 unique inlinks, parameter URLs. Log what changed.

## 2. Topical authority

- Map the topic before writing anything: the hub, its supporting pages, definitional pages (the vocabulary engines map), and question pages (the long-tail queries AI fans out to).
- Work in this order: optimise what exists, then embed it (internal links), then produce new pages. It's cheapest first.
- Wire the cluster: the hub links to every spoke, every spoke links back to the hub, and siblings link to each other.
- Track four proxies, since no tool gives a single score:
  - Coverage: share of the map's sub-topics with a live page.
  - Link depth: every cluster page within three clicks of the hub.
  - Ranking breadth: query count for the topic in Search Console.
  - AI citation frequency: ask ChatGPT, Perplexity and AI Overviews monthly and log who they cite.

## 3. Query fan-out (AI search)

- AI search answers the fan of sub-questions behind a query, then cites whoever answers most of them. For each money query, list that fan: People Also Ask, plus asking ChatGPT or Perplexity "If someone asks [query], what sub-questions would you research before answering?"
- Cover the fan with a hub page plus supporting pages. One page can't answer a whole fan well.
- Lead with the answer: answer-first headings and opening sentences, written as passages that can be quoted without editing.
- Add a real FAQ mapped to the facets in the fan, answered plainly.
- No llms.txt, AI-specific markup or rewrites. Google states there are no additional requirements to appear in AI Overviews or AI Mode. It's still SEO, aimed at the whole question.

## 4. Information gain

- A page earns its place by adding what the pages already ranking don't. Restating the consensus is worth zero.
- Five sources of real gain, nothing else counts:
  1. First-hand experience ("when we did this for a client, here is what happened")
  2. Original data: the client's own numbers, a small survey, a benchmark
  3. A defensible contrarian view, with evidence
  4. Process detail: exact steps, settings, screenshots
  5. A fresh synthesis of two ideas nobody has connected for this query
- More words, headings or keywords is not gain. A 600-word page of first-hand experience beats a 3,000-word page of consensus.
- For local clients, gain looks like this: real job details, local specifics, prices and timelines, photos from real jobs.
- Before rewriting a page that ranks but doesn't convert, score it Unique / Specific / Authentic. Then add the missing first-hand lines instead of more copy.

## 5. Links

- **The one test:** would this link exist if search engines didn't? If not, stop.
- **Check in this order, and stop at the first no:**
  1. Would it exist without search engines?
  2. Is the page it sits on real? (author, date, point of view, other content)
  3. Does the site have an audience?
  4. Would a human write that anchor text?
  5. Is it relevant to what the client does?
  6. Only then look at metrics.
- **Never:**
  - buy links, or pay for "high DA" gigs or PBNs
  - profile-creation farms
  - blog-comment spam
  - bulk press-release blasts
  - bought .gov or .edu links
  - swapped or automated placements
  - the exact target keyword as anchor text on links we control
- **Free links first, in this order:**
  1. Claim Google Business, Bing Places, Apple Business Connect and LinkedIn.
  2. Fill every listing completely.
  3. Answer journalist requests (Qwoted, Featured; SourceBottle for Australia).
  4. Build something worth linking to: a free tool or a data study.
  5. Keep name, address and phone identical everywhere, and recheck quarterly.
- **Tactics that earn their time, best first:** digital PR, original data, video, genuinely free resources, and being the obvious branded answer.
- **Nofollow:** don't write off nofollow links. They still carry the mention.

## 6. Digital PR (one campaign per client per quarter)

1. **Recon:** list the audience's real questions. Check Google News, Trends, Reddit and TikTok. Draft 3 to 5 headlines ("The most [X] in [place]", "Best and worst [X]", "[X] hidden cost revealed").
2. **Analyze:** back the idea with real data (government reports, industry stats, surveys, Trends). Turn it into one headline, 3 to 5 bullets and one chart or table.
3. **Infiltrate:** find the right 20 to 30 reporters, not 300 (Muck Rack by topic). Check what each has written on the subject in the last 12 months, and verify emails (Hunter.io).
4. **Deploy:** a strong subject line, then a 2-sentence intro, 3 facts and a link. Notes go at the bottom. Follow up once, 5 to 7 days later, offering an exclusive local angle. Then stop.
5. **Score:** log every coverage link the day it lands (outlet, URL, linked or unlinked, date), and bring the sheet to the next Recon.

## 7. Working method

Chain single-purpose steps: audit → plan → write → measure.

1. Local SEO audit of the homepage → the on-page priority list
2. Trust check of the About page → a trust score and three things to add
3. Competitor gap against the top two local rivals → keyword and content gaps
4. A brief and a draft for each gap
5. A title tag for each new page
6. Monthly striking-distance pass on fresh Search Console data → queries at positions 4 to 15, with one tweak each
7. An information-gain score on pages that rank but don't convert

When a step repeats across clients, make it our own skill file. Never install third-party skill files by piping a URL into `~/.claude/skills`; read and rewrite them first.

## Caveats

- The "SOURC-E" formula, AI visibility = (O × U × R × C) / S, is one consultant's framework, not a Google measure. Don't present it to clients as fact.
- The information-gain patent is Google's US 11,354,342, "Contextual estimation of link information gain". A patent shows what Google can do, not what it does in ranking today.
