# SEO Plan — Outrank [gangacounty.co.in](https://www.gangacounty.co.in/)

**Project site:** [https://gangacounty.com](https://gangacounty.com) (GitHub Pages custom domain → `docs/`)  
**Primary competitor:** [https://www.gangacounty.co.in/](https://www.gangacounty.co.in/)  
**Goal:** Rank #1 (or above the competitor) for brand + plot-intent keywords in Google India.

**Success metric (90 days):** Appear in top 3 for at least 5 of the Priority keywords below, and above `gangacounty.co.in` for `"plots in Ganga County"` / `"Ganga County plots"`.

**Keyword source of truth:** [SEO keyword sheet](https://docs.google.com/spreadsheets/d/1KoiBeWd-RjhfRpT4wGce355i8lTR_7Pmhz7GJ4padKg/edit?usp=sharing) (linked from `SEO_Work.md`). Backlink tracker: [SEO / backlink sheet](https://docs.google.com/spreadsheets/d/11DiXj6yrf2xWbxux662UIOAvFoc__1_w86eJQjBiZ2c/edit?usp=sharing).

---

## Current gaps (audit of this codebase)

| Area | Current state | Impact |
|------|---------------|--------|
| Domain / canonical | **Done** — live at `https://gangacounty.com`; canonicals + `site-config.js` updated (Phase 0) | Official commercial domain is set |
| `robots.txt` | **Done** — `docs/robots.txt` | Crawlable |
| `sitemap.xml` | **Done** — `docs/sitemap.xml` | Ready for GSC submit |
| Structured data | **Done** — homepage JSON-LD + inner BreadcrumbList | Validate in Rich Results Test after deploy |
| Open Graph image | **Done** — `og:image` + Twitter cards sitewide | Social / SERP previews improved |
| Titles / H1 | **Partially done** — one homepage H1; unique H1s on inner pages; pricing duplicate title fixed | Body copy / title rewrite still Phase 3 |
| Image SEO | Generic alts (`about image`, `Brand Logo`, `blog grid`) | Lost image + on-page relevance |
| Indexing setup | No Search Console / Analytics evidence in repo | No measurement or indexing control |
| Authority | Competing with `.co.in` brand domain + Atomoney / portals | Need content + backlinks + local signals |
| Content depth | Thin unique copy vs competitor + Atomoney pages | Competitor wins on content + age |

**Competitor reality check:** [gangacounty.co.in](https://www.gangacounty.co.in/) already owns brand queries and has a custom domain, deep project copy, brochure/video, and related pages (e.g. Atom City Centre). Other strong SERP players: [atomoney.com/ganga-county](https://atomoney.com/ganga-county/), [ganga-county.in](https://ganga-county.in/), listing sites like SmartBrickz. Winning requires **technical fixes + unique content + local/brand authority**, not meta tags alone.

---

## Target keywords

Keywords below are taken from the **gangacounty keywords** sheet in `SEO_Work.md` / [keyword spreadsheet](https://docs.google.com/spreadsheets/d/1KoiBeWd-RjhfRpT4wGce355i8lTR_7Pmhz7GJ4padKg/edit?usp=sharing), plus a few brand variants needed to beat the competitor.

### Priority (must win) — from keyword sheet + brand SERP

| Keyword | Intent | Target page |
|---------|--------|-------------|
| ganga county residential plots | Brand + residential | `index.html` |
| ganga county residential plots garhmukteshwar | Brand + location | `index.html` / `overview.html` |
| ganga county plot project | Brand | `overview.html` |
| ganga county approved plots | Trust / approval | `overview.html` |
| ganga county commercial plots | Commercial | new commercial page / `index.html` |
| ganga county commercial property | Commercial | new commercial page |
| ganga county plot price | Commercial / price | `pricing.html` |
| ganga county price list | Commercial / price | `pricing.html` |
| buy plots in ganga county | Transactional | `index.html` / `contact.html` |
| invest in ganga county | Investment | `overview.html` |
| plots in Ganga County | Brand SERP (beat competitor) | `index.html` |
| Ganga County plots | Brand SERP (beat competitor) | `index.html` |
| Ganga County Garhmukteshwar | Brand + location | `index.html` / `overview.html` |

### Secondary (sheet + supporting)

| Keyword | Target page |
|---------|-------------|
| Real estate in Ganga county | `overview.html` |
| properties in ganga county | `index.html` |
| real estate investment in ganga county | `overview.html` |
| residential plot in ganga county | `pricing.html` |
| Commercial plot in ganga county | commercial page |
| ganga county shops | commercial / Atom City Centre page |
| Residential plots in garhmukteshwar | `index.html` / `pricing.html` |
| commercial plot in garhmukteshwar | commercial page |
| plot near garhmukteshwar | `location.html` |
| commercial property in garhmukteshwar | commercial page |
| villas in garhmukteshwar | `pricing.html` |
| property investment in Garhmukteshwar | `overview.html` |
| buy plots in Garhmukteshwar | `index.html` / `contact.html` |
| land for sale in Garhmukteshwar | `pricing.html` |
| real estate project in Garhmukteshwar | `overview.html` |
| Ganga County master plan | `master-plan.html` |
| Ganga County amenities | `amenities.html` |
| Atom City Centre Garhmukteshwar | commercial page |
| plots near Ganga Expressway | `location.html` |

### Supporting long-tail (blog / FAQs)

- Is Ganga County RERA / government approved? → **Yes** (confirm exact approval docs on page)
- Ganga County plot sizes 150 / 225 / 300 / 500 sq yd
- Ganga County vs other projects in Garhmukteshwar
- Distance from Delhi NCR / NH-9 / Brij Ghat
- Down payment plan Ganga County plots

### Off-page work already tracked (`SEO_Work.md`)

Continue / improve quality of placements logged in the [backlink sheet](https://docs.google.com/spreadsheets/d/11DiXj6yrf2xWbxux662UIOAvFoc__1_w86eJQjBiZ2c/edit?usp=sharing) and related blog docs. Prefer links that use Priority keywords as anchor text pointing to `https://gangacounty.com/` (not the competitor domain).

---

## Phase 0 — Foundations (Week 1) — **COMPLETED**

Production domain is mapped: **https://gangacounty.com**

### To-do

- [x] **Decide and set the live production domain** → `https://gangacounty.com` (GitHub Pages custom domain)
- [x] **Point DNS** to GitHub Pages
- [x] **Enable HTTPS** on `https://gangacounty.com`
- [x] Update `docs/site-config.js` → `siteUrl: "https://gangacounty.com"`
- [x] Replace every placeholder canonical / `og:url` across HTML files with `https://gangacounty.com/...`
  - Pages updated: `index.html`, `overview.html`, `pricing.html`, `highlights.html`, `amenities.html`, `master-plan.html`, `location.html`, `gallery.html`, `contact.html`
- [x] Consistent primary brand name: `author` + `og:site_name` set to **Ganga County**
- [ ] Confirm this site is the **official** project URL vs Atomoney / `gangacounty.co.in` (business decision — if same owner, plan 301s)
  gangacounty.com is actual owner's website. gangacounty.co.in is broker's website

### Action items completed

1. Ran `python3 scripts/set-site-url.py https://gangacounty.com`
2. Normalized `author` / `og:site_name` to `Ganga County`

**Exit criteria:** Live HTTPS domain; all canonicals match `https://gangacounty.com`; no `YOUR_USERNAME` left in HTML. ✅

---

## Phase 1 — Technical SEO (Week 1–2)

### To-do

- [x] Create `docs/robots.txt` with sitemap pointing to `https://gangacounty.com/sitemap.xml`
- [x] Create `docs/sitemap.xml` listing all indexable pages with `lastmod` (excludes `thank-you.html`)
- [x] Add **JSON-LD** on homepage (`Organization`, `RealEstateListing`, `Place`, `WebSite`)
- [x] Add `BreadcrumbList` JSON-LD on inner pages
- [x] Add `og:image` + `twitter:card` on all indexable pages
- [x] Fix **duplicate `<title>`** on `pricing.html` (+ broken `og:description` quote)
- [x] Reduce homepage to **one H1** (extra slider titles → `.hero-slide-title`)
- [x] Add unique keyword-aligned H1 per page
- [ ] Compress images (WebP where possible); add width/height to reduce CLS.
- [ ] Lazy-load below-fold images; keep LCP image eager.
- [ ] Audit mobile performance (PageSpeed Insights / CrUX): target LCP &lt; 2.5s, INP &lt; 200ms, CLS &lt; 0.1.
- [x] Internal links already use root-relative / same-folder paths (`pricing.html`, etc.)
- [x] Skip `hreflang` until Hindi pages exist
- [x] `thank-you.html` already `noindex`

### Action items

1. Dev implemented robots, sitemap, schema, OG, H1/title fixes.  
2. Validate schema: [Google Rich Results Test](https://search.google.com/test/rich-results).  
3. Run PageSpeed on mobile; fix top 3 issues (usually images, unused JS, font load).  
4. Submit sitemap in Google Search Console (Phase 2).

**Exit criteria:** Sitemap live; robots correct; schema validates; one H1 per page; no duplicate titles. *(code complete — submit in GSC after deploy)*

---

## Phase 2 — Search Console, Analytics & indexing (Week 2)

### To-do

- [ ] Create **Google Search Console** property for `gangacounty.com` (Domain property preferred).
- [ ] Verify DNS / HTML file as required.
- [ ] Submit `https://gangacounty.com/sitemap.xml`.
- [ ] Request indexing for homepage + pricing + location + overview.
- [ ] Create **Google Analytics 4** (or equivalent) + link to Search Console.
- [ ] Set up **Bing Webmaster Tools** and submit the same sitemap.
- [ ] Monitor Coverage / Page indexing for soft-404s, redirects, excluded pages.
- [ ] Track ranking weekly for Priority keywords (Ahrefs / SEMrush / free SERP checks + GSC Queries).

### Action items

1. Marketing/owner owns GSC + GA4 accounts.  
2. Dev adds GA4 snippet (or GTM) sitewide.  
3. After deploy, use URL Inspection → Request indexing on money pages.

**Exit criteria:** Domain verified; sitemap processed; homepage “URL is on Google”.

---

## Phase 3 — On-page SEO (Week 2–4)

Rewrite and differentiate — do **not** copy [gangacounty.co.in](https://www.gangacounty.co.in/) verbatim (duplicate content will lose).

Map **sheet keywords** into titles, H1s, first paragraphs, and internal anchors.

### Homepage (`index.html`)

- [ ] Title (~55–60 chars), example:  
  `Ganga County Residential Plots Garhmukteshwar | 150–500 Sq.Yd.`
- [ ] Meta description (~150–160 chars) including price cue + location + CTA; weave in “buy plots in Ganga County” / “approved plots”.
- [ ] First visible paragraph must include: **Ganga County**, **residential plots**, **Garhmukteshwar**, plot sizes, starting price.
- [ ] Clear sections with H2s: Why Ganga County, Plot sizes & pricing, Location advantages, Amenities, Master plan, FAQs.
- [ ] Visible NAP: address + phone `+91-7303806469` in text (not only images).
- [ ] CTA buttons as real links/text (crawlable), not JS-only.

### Page-level briefs

| Page | Primary keyword(s) from sheet | Content to-do |
|------|-------------------------------|---------------|
| `overview.html` | ganga county plot project, approved plots, invest in ganga county, real estate project in Garhmukteshwar | Unique overview, approvals, township size, USP vs competitors |
| `pricing.html` | ganga county plot price, ganga county price list, residential plot in ganga county | Table: size → starting price / “on request”; payment plan; EMI/loan note if true |
| `location.html` | plot near garhmukteshwar, plots near Ganga Expressway | Distances (Railway, Brij Ghat, Expressway, NH-9), embedded map, landmarks |
| `amenities.html` | Ganga County amenities | Clubhouse, parks, security — descriptive copy, not icon-only |
| `master-plan.html` | Ganga County master plan | Layout explanation + downloadable plan (PDF with keyword filename) |
| `highlights.html` | ganga county residential plots | Bullet USPs expanded into short paragraphs |
| `gallery.html` | Ganga County project photos / properties in ganga county | Descriptive alts; captions with location/project name |
| `contact.html` | buy plots in ganga county / buy plots in Garhmukteshwar | Form + phone + WhatsApp + map; schema `ContactPage` |
| **New commercial page** | ganga county commercial plots, commercial property, ganga county shops, commercial plot in garhmukteshwar | Atom City Centre / shops — dedicated URL |

### Image SEO to-do

- [ ] Rename key files meaningfully where practical (`ganga-county-plots-garhmukteshwar.webp`).
- [ ] Replace generic `alt` with descriptive alts, e.g. `Ganga County residential plots in Garhmukteshwar`.
- [ ] Logo alt: `Ganga County` (not `Brand Logo`).

### Internal linking to-do

- [ ] From homepage, link to pricing, location, master plan with keyword-rich anchors (`Ganga County plot price list`, `location in Garhmukteshwar`).
- [ ] Footer link hub: Overview · Pricing · Location · Amenities · Contact.
- [ ] Add breadcrumb UI + BreadcrumbList schema on inner pages.

**Exit criteria:** Every money page has unique title, description, H1, 300+ words of useful unique copy, and keyword-aligned internal links.

---

## Phase 4 — Content that beats the competitor (Week 3–8)

Competitor wins partly on content age and coverage. Outrank with **fresh, deeper, more specific** assets.

### To-do — new pages / sections

- [ ] **FAQ page or homepage FAQ** (8–12 questions) → `FAQPage` schema.
- [ ] **Plot size landing sections** (or anchors): 150 / 225 / 300 / 500 sq.yd. who each size suits.
- [ ] **Commercial / Atom City Centre** dedicated page targeting sheet keywords: commercial plots, shops, commercial property in Garhmukteshwar.
- [ ] **Brochure landing** with PDF, short summary, and lead form (indexable HTML page, not PDF-only).
- [ ] **Hindi page** (`/hi/` or similar) for local search intent — optional but high-ROI in UP.
- [ ] **Blog / News** (even 4–6 posts) — align with existing blog drafts in `SEO_Work.md`:
  - Garhmukteshwar development / MahaYojana 2031
  - Why invest in plots near Ganga Expressway / land for sale in Garhmukteshwar
  - Site visit checklist for Ganga County
  - Price & size guide 2026 (`ganga county plot price` / `price list`)

### Content quality rules

- Unique paragraphs; cite real facts (approvals, sizes, distances).
- Update `lastmod` / visible “Updated: Month Year” on pricing & overview.
- Avoid doorway spam pages; each URL must answer a clear intent.

**Exit criteria:** ≥3 new high-intent pages live; FAQ schema valid; pricing page is the best SERP answer for price queries.

---

## Phase 5 — Local & brand authority (Week 2–10)

Brand SERPs for “Ganga County plots” are won by **entity consistency**, not only on-page SEO.

### To-do

- [ ] Google Business Profile (if sales office / site office exists) — categories: Real estate developer / Housing complex. Website field = `https://gangacounty.com`
- [ ] Consistent NAP across site, GBP, Justdial, Sulekha, 99acres, Magicbricks, Housing.com listings.
- [ ] Claim/optimize listings on major property portals with link back to **https://gangacounty.com**
- [ ] YouTube: upload walkthrough with title `Ganga County Plots Garhmukteshwar | Site Tour` + description link to `https://gangacounty.com`
- [ ] Embed that video on homepage (competitor already uses video heavily).
- [ ] Encourage branded searches: ads, WhatsApp status, brochure QR → `https://gangacounty.com` (not competitor).
- [ ] Earn / upgrade 5–10 quality backlinks (see `SEO_Work.md` tracker):
  - Developer parent site (Atomoney or owner site) → follow link to `https://gangacounty.com` as official project URL
  - Local news / PR on Garhmukteshwar development
  - Broker partner pages
  - Higher-quality citations than pastebin-style placements where possible
- [ ] If `gangacounty.co.in` is **your** old site: 301 redirect it to `https://gangacounty.com` (fastest way to win). If it is **not** yours: compete via content + GBP + portals + parent-brand links; do not copy or attack.

### Action items

1. Owner clarifies relationship to gangacounty.co.in / Atomoney (critical strategy fork).  
2. If same owner → consolidate domains with 301s.  
3. If competitor/third party → aggressive differentiation + portal + parent-brand SEO.

**Exit criteria:** Branded query pack shows `gangacounty.com`; Knowledge/local signals point to your URL.

---

## Phase 6 — Conversion SEO (ongoing)

Ranking without leads is incomplete.

### To-do

- [ ] Click-to-call and WhatsApp links with tracked UTM parameters.
- [ ] Thank-you page conversion event in GA4.
- [ ] Ensure contact forms work (`site-config.js` Web3Forms key — still placeholder).
- [ ] Keep popup from blocking crawlable main content; ensure primary copy exists in HTML without depending on the popup.
- [ ] Add privacy/disclaimer pages and link in footer (trust + AdSense/ads compliance if used).

---

## 30 / 60 / 90 day checklist

### Day 0–30

- [x] Production domain live + HTTPS (`https://gangacounty.com`)
- [x] Canonicals / `siteUrl` updated to production domain
- [x] robots / sitemap  
- [ ] GSC + GA4 + Bing  
- [x] H1/title/schema / OG fixes (perf still open)  
- [ ] Homepage + pricing + location copy upgrade (sheet keywords)  
- [ ] Parent brand link (if available)  

### Day 31–60

- [ ] FAQ + brochure + commercial page (sheet commercial keywords)  
- [ ] Image alts + Core Web Vitals pass on mobile  
- [ ] Portal listings + GBP  
- [ ] 2–3 blog/news articles  
- [ ] Video embedded  

### Day 61–90

- [ ] Hindi page (optional)  
- [ ] Backlink push (PR / partners) — improve quality vs current tracker  
- [ ] Refresh titles based on GSC query data  
- [ ] Compare SERP positions vs gangacounty.co.in weekly; double-down on queries where you rank 4–10  

---

## Weekly ops ritual

| Day | Action |
|-----|--------|
| Mon | Check GSC: impressions, queries, indexing errors |
| Wed | Publish or update one content asset |
| Fri | SERP check Priority keywords (incognito / VPN India) vs competitor |
| Month-end | Update pricing/overview “last updated”; resubmit changed URLs; sync keyword sheet rankings |

---

## Implementation order for this repo (dev backlog)

1. ~~Replace placeholder domain in all HTML + `site-config.js`~~ ✅ (`https://gangacounty.com`)  
2. ~~Add `robots.txt` + `sitemap.xml`~~ ✅  
3. ~~Fix `pricing.html` double title; homepage multiple H1s~~ ✅  
4. ~~Add JSON-LD + `og:image` sitewide~~ ✅  
5. Rewrite meta titles/descriptions to Priority keywords from sheet  
6. Unique body copy + FAQs  
7. Image alt pass  
8. GA4 + GSC verification file  
9. New pages: FAQ, commercial/Atom City Centre, brochure  
10. Performance pass (images/JS) — WebP, lazy-load, PageSpeed

---

## Realistic note

Outranking [gangacounty.co.in](https://www.gangacounty.co.in/) for **brand keywords** is fastest if you **own that domain** and 301 it to `https://gangacounty.com`, or if this site is promoted as the official URL by the developer. If that domain belongs to someone else, expect a **multi-month** fight focused on unique content, local listings, parent-brand authority, and technical excellence — not meta keywords alone (Google largely ignores the `keywords` meta tag).

---

## Owners

| Workstream | Suggested owner |
|------------|-----------------|
| Domain / DNS / hosting | Project owner |
| HTML / schema / sitemap | Dev |
| Copy / FAQs / blog | Content + sales (facts) |
| GSC / GA4 / rankings | Marketing |
| GBP / portals / backlinks | Marketing + partnerships |
| Legal: which site is official | Business owner (decide before heavy SEO spend) |

---

*Document version: 2026-07-15 (rev 3) — domain `https://gangacounty.com`; keywords from SEO_Work.md sheet; Phase 0 + Phase 1 (code) executed.*
