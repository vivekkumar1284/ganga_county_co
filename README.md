# Ganga County — Static Website Clone

Exact visual/content clone of [gangacounty.org.in](https://gangacounty.org.in/), converted to **static HTML** so it can run on **GitHub Pages** (and other free static hosts) with the same look and feel.

## What's included

- All main pages: Home, Overview, Pricing, Highlights, Amenities, Gallery, Location, Master Plan, Contact
- Original images, logos, icons, brochure PDFs
- Same phone / WhatsApp number (`+91-9650655124`)
- Same Maps embed and WhatsApp chat widget
- Contact forms via [Web3Forms](https://web3forms.com) (free; no PHP required)

Published site files live in the [`docs/`](docs/) folder (GitHub Pages `/docs` source).

## Before you go live (required)

### 1. Web3Forms access key (lead emails)

1. Sign up at [https://web3forms.com](https://web3forms.com)
2. Create a form and enter the **email where leads should arrive**
3. Copy your **Access Key**
4. Open [`docs/site-config.js`](docs/site-config.js) and set:

```js
web3formsAccessKey: "paste-your-key-here",
```

### 2. Site URL (SEO / thank-you redirect)

Set your live URL in [`docs/site-config.js`](docs/site-config.js):

```js
siteUrl: "https://YOUR_USERNAME.github.io/ganga_county",
```

Also update canonical/OG tags in the HTML files:

```bash
python3 scripts/set-site-url.py https://YOUR_USERNAME.github.io/ganga_county
# or for a custom domain:
python3 scripts/set-site-url.py https://www.yourdomain.com
```

### 3. Confirm rights

Only publish if you have permission to use this brand’s content, images, and phone number on your domain.

## Deploy to GitHub Pages (recommended)

1. Create a GitHub repository and push this project
2. In the repo: **Settings → Pages**
3. **Source:** Deploy from a branch
4. **Branch:** `main` (or `master`), folder: **`/docs`**
5. Save — site will be at `https://YOUR_USERNAME.github.io/REPO_NAME/`
6. Run `python3 scripts/set-site-url.py` with that URL, commit, and push again

### Custom domain on GitHub Pages

1. In Pages settings, add your custom domain
2. Create [`docs/CNAME`](docs/CNAME) containing only your domain, e.g.:

```text
www.yourdomain.com
```

3. Point DNS:
   - **Apex domain:** GitHub’s A records, or
   - **www:** CNAME → `YOUR_USERNAME.github.io`
4. Run `python3 scripts/set-site-url.py https://www.yourdomain.com` and push

## Other free hosting options

| Host | Notes |
|---|---|
| **Cloudflare Pages** | Free CDN; upload/`docs` as project output; great with custom domains |
| **Netlify** | Drag-and-drop `docs/`; optional Netlify Forms instead of Web3Forms |
| **Vercel** | Import repo; set output/root to `docs` |
| **Firebase Hosting** | Free Spark plan; deploy `docs` folder |

These all serve static files the same way — **look and feel stay identical**.

## Local preview

```bash
cd docs
python3 -m http.server 8080
```

Open [http://localhost:8080](http://localhost:8080)

## Project layout

```text
docs/                 ← publish this folder
  index.html
  overview.html
  ...
  thank-you.html
  site-config.js      ← access key + site URL
  site-init.js
  assets/             ← images, CSS, JS, PDFs
scripts/
  set-site-url.py     ← update canonical/OG URLs
plan.md
requirements.md
```

## Notes

- Original site used PHP only for page names and form handling; visuals do not need PHP
- Google Tag Manager from the source site was removed (add your own analytics ID if needed)
- Font Awesome kit CDN + local solid webfont are used for icons (same as usable live behavior)
