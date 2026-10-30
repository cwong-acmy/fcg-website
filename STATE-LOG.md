# STATE-LOG — FCG Website

## 2026-10-30 (evening) — Ad Studio export now waits for every brand font VERIFIED

- **Changed:** `fontsOk()` loads and checks Inter 300 to 600 and Caveat. Caveat is used only on the Guide kraft cover and loaded lazily, so an export straight after switching to it could catch a fallback face. Found while building the Accomy and Runway studios (same fix there).
- **Verified:** full suite on the change, then live: 202 of 202 exports, layout identical to the previous live version, real Export click saved a 1080×1080 PNG, 0 outside requests, 0 page errors. Redeployed; live byte-identical.

### Learnings

- **Problem:** porting the studio fixes to Accomy and Runway showed layout differences that were not real, and one change that was not harmless.
- **Approach:** (1) Compared every template's text boxes against the original file, not just export sizes. (2) For each difference, re-measured that one template after fonts and images had fully loaded: Desk note (Caveat) and Character side (line art) were identical, so the gaps were measure-too-early. (3) Turned the font finding into a fix: the export check now loads every brand font, not just the body face.
- **Judgment calls:** Dropped the global `overflow-wrap:break-word` for the new studios: it splits words that already overflow a narrow box (Accomy's 8ch kraft card). Kept it on FCG, where the full comparison showed no such case. Did NOT take the taken `runway-ad-studio.vercel.app` name as an error to fight; added a clear free domain instead.
- **Rule:** Before calling a layout difference real, re-measure after every font and image has loaded.

## 2026-10-30 (later) — Ad Studio: long text wraps, Enter makes line breaks VERIFIED

- **Problem (Alfred):** a headline with no spaces ran off the canvas or under the guide card.
- **Fix:** headline, claim, cover, closing and question are now multi-line boxes; Enter becomes a `<br>` in every field except the ones templates split into rows (items, speakers, POV). `.ad` uses `overflow-wrap:break-word`; `anywhere` switches on only when a field (not legal) holds 20+ characters with no space. A global `anywhere` was tried first and rejected: it squeezed Award/Badge 4:5 (orphan full stop) and split Big number 4:3 ("201 / 3").
- **Verified:** the reported string on Guide Cover and Cover bleed 4:5 stays inside the canvas; Enter gives one `<br>`. Pixel comparison of all 202 combinations with default copy, old live vs new: 182 identical, the 20 Gradient/Soft field covers differ by the same amount as the live site against itself (grain noise, 4.3). Deployed; live byte-identical to `ad-studio/index.html`; the reported case re-checked on the live URL.

## 2026-10-30 — FCG Ad Studio standalone on Vercel VERIFIED

- **Built:** `ad-studio/` from `02.FCG/03.Brand Assets/06.Ad Templates/fcg-ad-studio.html`. Fonts (Inter 300 to 600, Caveat 600 from @fontsource 5.3.0), modern-screenshot 4.7.0 and the 31 Calendly reference frames ship in the folder; no Google Fonts or CDN. Export swapped from html2canvas to modern-screenshot (browser renderer, real shadows), blocked with a message if Inter has not loaded, and downloads the PNG directly (was a right-click popup). Autosave to localStorage, Reset template, Copy link (one template, no photos; link input validated against known templates/options).
- **Deployed:** new work-team project `fcg-ad-studio` (`prj_LYlxK7G0PUu8eP3Aalo7sOG9PqA2`), CLI, not git-connected. https://fcg-ad-studio.vercel.app public 200, byte-identical to `ad-studio/index.html`.
- **Verified on the live site (Chrome for Testing, front tab):** Export button saved a 1080×1080 PNG; 202 of 202 template/layout/size exports at the right size and not blank; 0 outside requests; 0 page errors. Locally: autosave survives reload, share link restores in a clean browser, hostile link (HTML in a field, non-image data URL, unknown template) rendered as text or dropped, Reset restores defaults, no sideways scroll at 375 px. First export about 70 ms visible (16 s seen only in a hidden pane, timer throttling).
- **Docs:** studio link swapped to the Vercel URL in the design bible, visual reference kit, Buzz handover, FCG-DESIGN, brand kit, Developer Platform system and film contract, plus the 7 matching wiki pages (patched in place).
- **Open:** not pushed (this branch is the Developer Platform's production branch, so a push redeploys it). The 02.FCG single-file studio is now the older copy. The site is public, including the Calendly reference frames.

### Learnings

- **Problem:** browser tests of the studio showed 6 wrong-size exports and a 16 s first export, neither of which was real.
- **Approach:** (1) Compared each bad PNG with the on-screen frame: they matched, so the exporter was faithful and the state was stale. (2) Found the first test, which had timed out, still running in the page and changing settings. Reloaded, re-ran: 202 of 202. (3) Re-timed in a front tab of Chrome for Testing: first export 71 ms, so the 16 s was the hidden pane throttling timers.
- **Judgment calls:** Did NOT add caching or warm-up code for a slowness that only exists in a hidden pane. Did NOT trust any timing from the hidden built-in pane.
- **Rule:** Reload the page after any timed-out browser script, and take timings only from a visible tab.

## 2026-10-28 ~10:15 UTC — Search Console: property added, BLOCKED on DNS record

- Search Console (crystal.wong@fusionconnectgroup.com): Domain property `fusionconnectgroup.com` added, unverified. DNS is at GoDaddy (ns63/ns64.domaincontrol.com; existing TXT is only the Outlook SPF). Did not use Google's "sign in to GoDaddy" flow (needs FCG's GoDaddy login + OAuth grant). TXT to add at the apex: `google-site-verification=h6q4K8DAr0PecM8EyXmac6yN89PmyarrfBQdmDuR5kA` (also in 1Password item `f6gg3fs3vj3baggj42j5qiwzym`, field "Search Console DNS TXT"). After it resolves: Search Console → Verify, then link to GA4 property 561108472 and submit `https://www.fusionconnectgroup.com/sitemap.xml`. Fallback after launch: URL-prefix property verified through GA4/GTM, no DNS needed.
- Google flagged an "Important account alert" on the FCG Google login; left for Crystal.

## 2026-10-28 ~10:00 UTC — FCG GA4 + Tag Manager set up; all analytics committed (not pushed)

- Google, as crystal.wong@fusionconnectgroup.com: GA account "FCG" 413727466, property "Fusion Connect Group" 561108472 (created by Crystal at sign-in); web stream "FCG Website" 16219846406 for www.fusionconnectgroup.com, enhanced measurement on, **G-QM59ND5BC3**. Tag Manager account "FCG" 6400643995 (country left at default United States, no FCG HQ source found; editable in GTM Admin), container 284017516 **GTM-MKFC3SDS**; tag "GA4 - FCG Website" on Initialization - All Pages; published version 2 (public gtm.js serves version 2 with G-QM59ND5BC3). GTM terms + GDPR Data Processing Terms accepted; "share data anonymously" left off. User-provided data collection not enabled by me; its GA setting page did not open, so its state is UNVERIFIED.
- 1Password LLM Automations `f6gg3fs3vj3baggj42j5qiwzym` "Google Analytics + Tag Manager - FCG Website" (read back OK).
- Commit `943e966` on codex/blog: `_shell/posthog.html` renamed `_shell/analytics.html` with PostHog + GTM loaders (live domain only); `GTM_ID` in build-site.py; successful demo booking also pushes `generate_lead` to dataLayer (as accomy LP pages). 21 pages carry both; `--check` OK; form tests 7/7. Runtime on a local copy (gate bypassed): GTM-MKFC3SDS loaded and sent `g/collect?tid=G-QM59ND5BC3`; PostHog loaded. Skipped vs accomy: Google Ads + Meta pixel tags (no FCG ads), GTM noscript iframe.
- **Pushed** codex/blog `00a297d..943e966` (Crystal approved; main untouched). Build site Action `40666504687` success, no rebuild commit. Vercel preview VERIFIED: 21/21 pages carry PostHog `phc_zUEd…` + GTM-MKFC3SDS + the live-domain gate; fcg-blog.js has the new events; unknown path returns 404 page with the snippet. Staging not re-checked (does not auto-sync; Lucas to pull). Next: after launch, check GA Realtime and PostHog for first live visits; add Search Console.

## 2026-10-28 09:30 UTC — FCG PostHog live in code; GA/GTM waiting on FCG Google sign-in

- Decision (Crystal): FCG gets its own analytics accounts under crystal.wong@fusionconnectgroup.com, not Accomy's (Accomy PostHog free plan is capped at one project; Accomy GA blocks property creation for her login).
- PostHog: Crystal signed up; org "Fusion Connect Group" `01a181d3-f505-0000-69cb-dd2737f6fdc2`, US cloud. Project 693521 renamed "FCG Website"; session replay, heatmaps, autocapture on; UTC (as Accomy); authorized URLs www + apex. Token in 1Password LLM Automations item `6imlb6rlovq3d4gg5jd66zdl4u` "PostHog - FCG Website project token" (read back OK).
- Commit `773fb5c` on codex/blog (local, ahead 2 with `6c21fdb`): `POSTHOG_KEY` set; 21 pages carry the snippet; `--check` OK, form tests 7/7. Ingestion VERIFIED: test event `fcg_setup_test` from a local copy (snippet run without the domain gate) landed in project 693521 at 2026-10-28T09:27:32Z with locale en. On the real pages tracking still only runs on fusionconnectgroup.com.
- Next: Crystal signs in to Google as the FCG email; then FCG GA4 account/property/web stream + FCG GTM account/container with GA4 tag, publish, save IDs to 1Password, add GTM to the build, push on approval.

## 2026-10-28 — Analytics parity with accomy.com (PostHog), waiting on FCG key

- accomy.com today: PostHog on every page (project 511406, US cloud, `defaults: 2025-05-24`, `person_profiles: identified_only`, `locale` super property; replay/heatmaps are project toggles), events `lead_submitted {form}`, `lead_submit_failed`, `newsletter_subscribed`; GTM `GTM-NB2SMNHL` only on `/lp/*` ad landing pages; no cookie banner.
- Decision (Crystal): separate "FCG Website" project in the same Accomy PostHog organisation. GTM skipped until FCG runs ads.
- Commit `6c21fdb` on codex/blog, **local, not pushed**: `_shell/posthog.html` (accomy snippet, runs only on fusionconnectgroup.com) injected into every page via a BUILD:ANALYTICS region; form events in `assets/js/fcg-blog.js`. `POSTHOG_KEY` in `tools/build-site.py` is empty, so nothing loads yet. Checks: build `--check` OK, form tests 7/7, fake-key dry run put the snippet on 21 pages, loader ran in the browser (loaded, api_host us.i.posthog.com, locale en), gated off on localhost.
- **2026-10-28 ~09:20 UTC, Crystal signed in (crystal.wong@accomy.com) in the built-in browser. BLOCKED twice:** (1) PostHog org "Accomy" has one project, "Default project" 511406, shared by accomy.com, Salta and COS; creating "FCG Website" returned 403 "maximum limit of allowed projects for your current plan". (2) GA account "Accomy" (a349619002, property p482616162): Create → Property is disabled for this login (account-level role too low); creating a new GA *account* is allowed. accomy.com GTM container `GTM-NB2SMNHL` (named travel.accomy.com) loads GA4 `G-60NPV3PTS8`, Google Ads `AW-16938812305` conversion, conversion linker, Meta pixel. Nothing created, nothing saved to 1Password.
- **Earlier blocker:** LLM Automations has no Accomy PostHog personal API key (only the public SMEP/accomy.com token and Larry's separate account), and the browser is not signed in, so the project must be created by Crystal. Next: set the key, rebuild, push; verify first events after the live domain serves the new build (staging is gated off by design).

## 2026-10-28 — Blog "Coming soon" until first real post (Crystal)

- Commit `00a297d` on codex/blog, **pushed 08:30 UTC** (Crystal approved; main untouched). Build site Action run `40657336945` success, no rebuild commit. Vercel preview `dpl_DPPk5gjrP9Ztpr7g2ykGvypPcw3R` VERIFIED: blog.html shows Coming soon, homepage 0 cards, pages identical to the commit apart from Vercel's feedback script. **Staging NOT updated** as of 08:36 UTC (still Last-Modified 06:35): staging does not auto-pull on push; ask Lucas how/when it syncs. `build-site.py` lists only published posts; with none, blog.html shows a Coming soon panel (subscribe kept), the home and product strips are empty, and the filter buttons are hidden. Draft pages still build (noindex) for review by direct URL. Checked: `--check` OK, form tests 7/7, local preview screenshot; publishing one post in a scratchpad copy restored cards, sitemap and RSS.
- Pages CMS fields vs design: all 14 fields are used by the build/templates; gaps: no separate SEO title/description, no cover alt text, no updated date, editors must include the main topic in Filter topics.

## 2026-10-28 08:20 UTC — Staging retest after Lucas's nginx proxy: VERIFIED

- **Forms through www-staging (real page, built-in browser):** `contact.html?product=atlas` pre-selected Atlas; `POST /api/book-demo 200`, thank-you panel shown. Blog subscribe `200`, "Thanks, you are subscribed." Supabase `fcg_website.leads` `f3ec9d62-8587-4296-bb76-84e4f158a110`, `subscribers` `31b197fa-ba04-4102-8ffb-6979bd99883a`; Feishu Base demo `reczz28SlJl4nXmP`, subscribers `reczz28SlK9plOkT` (Supabase ids match); 2 cards in the FCG leads group (`om_x100b612f4cc830a0c1375a72694415c`, `om_x100b612f4db5a8b8cf04f23e5117ee8`). Test tag `STAGING-TEST-10280819`, rows left in place. Read back with the Cosmo bot via the API (Lark MCP was disconnected).
- **Staging = codex/blog @ e2d2a72** (index, blog, contact, 404, JS, CSS, robots, sitemap byte-identical). Every response has `X-Robots-Tag: noindex`; real 404s; internal files (md, tools, _shell, db, api source, blog/posts JSON, .git) now 404; favicon, skip link, phone-menu label OK; no sideways scroll at 375; no console errors. 7 posts, all `draft: true`. Last 3 Build site Actions green.
- **Still open for launch:** real articles replace placeholders; Pages CMS access for Marketing + one real save test (filename, image path, rich-text HTML); how production nginx picks up new commits after a CMS save (staging's update method unknown); production env vars on Vercel; Vercel firewall rate limit; double opt-in; Supabase free-plan pause risk; do not push `main` until Marketing confirms.

## 2026-10-28 — 404 page + staging form 404s (Lucas Li, Feishu)

- **404:** added `404.html` (shared nav/footer via `tools/build-site.py`, `<base href="/">` so it styles at any missing path, noindex, excluded from sitemap). Checked locally at `/404.html` and a nested path: CSS, links, images resolve from root. Commit `e2d2a72` on codex/blog, pushed; preview `dpl_AXDAZsXoiGfEYBw64rU63kpnatnx` READY. nginx still needs `error_page 404 /404.html;` and the homepage catch-all removed (their ops).
- **Staging forms 404:** `api/` is Vercel Functions; nginx cannot run them. The codex/blog preview already exists with all 9 env vars (Preview target), and `accomy-projects` Supabase is ACTIVE_HEALTHY (2026-10-28). Blocker: project SSO protection (`all_except_custom_domains`) 302s every preview request to Vercel login, so an nginx proxy would fail. Handover §8.4 now has the proxy snippet with an `x-vercel-protection-bypass` header.
- **Bypass secret created 2026-10-28** (Crystal approved): Protection Bypass for Automation on fcg-website, stored in 1Password LLM Automations item `ybsp4ahj5xx35jrowdfoipr6vm`. Verified on the codex/blog alias: no header 302, with header GET /api/subscribe 405, unknown path 404 with the new page, POST /api/subscribe 200 `{"ok":true}`; Supabase `fcg_website.subscribers` row `cb126ada-106c-43c3-8e0b-65c214fd49ff` (bypass-test-1793169482@accomy.com, test row, left in place). Lark mirror is best-effort and was not read back.
- **Open:** Crystal sends the secret to FCG ops privately; they add the proxy; then re-test through their staging host. Behind a proxy all visitors share nginx's IP, so the 8/10-min rate limit is shared on staging.

## 2026-10-26 (late) — SEO/GEO audit against the vault playbooks (assessment only, nothing changed)

- Source checklist: FCG Vault `10 - Reviews & Learnings/08 - SEO.md` + wiki concepts (aeo, geo-passage-citability, long-tail-first, reddit-as-llm-citation, falsifiable-seo, aeo-8-week-warmup).
- **Live www.fusionconnectgroup.com is no longer Wix:** nginx serving an older static build (Last-Modified 2026-07-20). Every unknown path returns the homepage with 200, including `/robots.txt`, `/sitemap.xml`, `/about.html`, `/blog.html` (soft-404 catch-all). About, AI Booking Tool, Corporate Booking Tool and Payment are live only as `*_crystal-denzel-edit.html`, and the homepage links to those names. Apex and www both answer 200 (no redirect, no canonical).
- Core pages (live and codex/blog): 0/11 meta description, canonical, OG or JSON-LD; homepage has 2 H1s; 0 question-form H2s; "Fusion Connect Group" only on About. No analytics on any page. Homepage CLS 0.25 in a throttled mobile test. Tailwind Play CDN in production.
- Fine: static HTML, AI crawlers (GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot) get 200.
- Web search: "Fusion Connect Group" returns other companies; only hit is the BTS exhibitor page (listed under Accomy Singapore). Category queries do not surface FCG.
- Not checked: Search Console / Bing indexing (no access), PageSpeed API (daily quota hit), backlinks, live LLM answers.
- **Fixed (code side), commit `7cc8a7e` on codex/blog, **pushed 2026-10-26**; Action run 40291163159 success; preview `dpl_FUns2bxxiNRAXsoZrBsLSPdKfV58` READY and shows the new titles, canonicals and JSON-LD:** `_shell/seo.json` (Crystal-approved titles/descriptions) → BUILD:SEO region with canonical, OG and JSON-LD @graph (Organization "Fusion Connect Group", WebSite, SoftwareApplication x7, Service for payment); homepage second H1 → H2 (identical render). Open: official sameAs profile URLs (none found by search), footer "© FCG Group" legal naming, server-side items for tech.

## 2026-10-26 — Staging review of the blog (www-staging.fusionconnectgroup.com)

- Staging serves `codex/blog` @ 4c2130a byte-for-byte (checked index, blog, posts.json, feed, a post, CSS/JS). Host is nginx, not Vercel, so `.vercelignore` does nothing there.
- Works: Blog in nav + footer + phone menu, blog index, filters (?topic=, aria-pressed, live count), post pages, related reading, honest subscribe message, dark mode, no sideways scroll at 375, no console errors on blog pages.
- Fix before launch: internal files are public on staging (HANDOVER-BLOG.md with Crystal's email, AGENTS.md, README.md, tools/build-site.py, _shell/, blog/_post.html, components.html, nav-preview.html); footer copyright contrast 2.59 light / 2.48 dark (needs 4.5); LIVE.NETWORK tag 4.42; phone theme toggle has no label; no skip link; no favicon; no robots/sitemap; staging not noindexed (canonical points to www, which mitigates).
- Marketing self-publishing: NOT possible yet. Every edit to posts.json needs `build-site.py` to regenerate HTML, and staging has no build step. Pages CMS supports JSON + list fields, but the wrapped `{"posts":[...]}` shape is unconfirmed; needs a short spike plus a GitHub Action that runs the build on each commit.
- Next: send the review to the tech team; decide CMS + build pipeline.

### Build (same day) — commit `6bb9c84` on `codex/blog`, local only, NOT pushed
- Decided: **Pages CMS, no Contentful** for FCG (static site; free; Contentful free tier = 1 space/org, no roles, would need a fetch-at-build pipeline).
- Posts are now `blog/posts/<slug>.json` (posts.json removed); `.pages.yml`; `.github/workflows/build-site.yml` rebuilds + commits on push.
- `contact.html` book-a-demo form + real newsletter submit; `api/` endpoints ported from accomy.com (Supabase `fcg_website` first, then Lark). SQL in `db/` NOT applied; no env vars, Base tables or chat set up.
- A11y/SEO fixes in; axe 0 violations on blog, post, contact at 1440 and 375. `node --test tools/test-forms.js` 7/7; `build-site.py --check` 0. Independent security review: no critical/high; code-side mediums/lows fixed, the rest are in HANDOVER section 8.
- Open: push `codex/blog` (makes a Vercel preview only), tech items in HANDOVER section 8, which Lark chat gets FCG demo cards, Supabase project choice (free plan pauses).
- **Pushed** `codex/blog` @ `6bb9c84` (2026-10-26). Action "Build site" run 40287686097 success (nothing to rebuild). Vercel `fcg-website` preview success; `fcg-open-developer-platform` status fails on this and the previous commit (pre-existing, unrelated).
- **Lark created by Cosmo bot, verified by API readback:** Base "FCG – Website leads" `J7e4b3B09abc15sRlkZcFfXZnNt` (https://tianxiafangcang.feishu.cn/base/J7e4b3B09abc15sRlkZcFfXZnNt), Crystal full access; tables Demo requests `tbl6Wn4lZGX5xLIz`, Newsletter subscribers `tbl9GhYKsc9KAnsi` (fields MATCH code); group "FCG – Website leads" `oc_19a595c1c738ef92834c345bd52cc26e`, Crystal owner, only human member. The empty default table 数据表 was left in place (not deleted).
- **E2E test (Lark half):** real api/ handlers, Supabase stubbed: 200/200, 1 row per table + 2 cards tagged TEST-074702, `<at id=all>` did not mention anyone. Test rows left in the Base, safe to delete. Supabase half BLOCKED until a project is chosen and the SQL applied. These ids are kept here, not in HANDOVER-BLOG.md, because staging currently serves that file publicly.
- **Supabase (Crystal: use accomy-projects):** `iedubjxycyvqptkcezlp` was ACTIVE_HEALTHY. Applied `db/fcg-website-leads.sql` → schema `fcg_website` (tables leads, subscribers; unique `subscribers_email_key`; anon/authenticated 0 grants); appended `fcg_website` to PostgREST exposed schemas (existing list kept). Per-app sb_secret key `fcg_website` (key id 885989e7-2263-4e15-9b1b-3f0b262a792f) stored in 1Password LLM Automations item `i42o67nitkfxgasb2gwbaho3tu` (credential + SUPABASE_URL fields).
- **Real E2E (2026-10-26 07:50 UTC):** real handlers + real Supabase + real Lark: demo 200 (PG `d3ca9d65…` = Base row), subscribe 200 (PG `57c86422…`, `1cc90079…` = Base rows), repeat sign-up 200 with no new row/card, 5 cards total, `<at id=all>` no mention. Test rows tagged TEST-0747xx/0750xx remain in PG and Base. Not yet tested through a deployed URL: Vercel env vars not set.
- Local commits `20561ce` (timeouts 5s/8s + vercel.json maxDuration 30; a real run took ~4s) and `f25ccdd` (docs), NOT pushed.
- **Preview VERIFIED (2026-10-26 08:02 UTC):** 9 form env vars set on Vercel `fcg-website` **Preview only** (production has none). Pushed `f25ccdd`; deploy `dpl_8BjcLsJJqsJ7rt3iJF4YJW6WRHNY` READY (preview) at fcg-website-git-codex-blog-crystalwong-accomycoms-projects.vercel.app. Real browser submissions (Crystal signed in to Vercel in Chrome for Testing): `POST /api/book-demo 200`, `POST /api/subscribe 200`; PG leads `ca0a00bf-c585-4db6-970f-dbd232888f32` and subscribers `39965731-b8d4-4e77-ac9f-5fb1f43d14bc` match their Base rows' Supabase id; 2 cards in the FCG group. Test tag PREVIEW-080220. Production env vars still to set at launch.
- ⚠ During setup, `GET /v1/projects/{ref}/postgrest` printed the project's legacy `jwt_secret` into the local session transcript (not sent anywhere else). Crystal to decide on rotating it.
- Learning: a "generated file" marker string that also appears in the template's own comment makes a marker-based cleanup delete the template. Exclude source files by name, not by content.

## 2026-10-21 (final) — Blog ported to codex/drafts, pushed as codex/blog

### What changed

- **Ported, not copied.** The blog work was redone on `origin/codex/drafts` (890d1dc), the version
  fcg-website-one.vercel.app serves. It lives in branch **`codex/blog`**, commit **`ff08801`**, pushed
  to origin. The worktree is at `.claude/worktrees/codex-blog`.
- **Uses the drafts conventions.** `_shell/nav.html` and `_shell/footer.html` are the build source; no
  `partials/` folder. `_shell` had drifted from the live pages, so it was refreshed from them first
  (4.35M+, Atlas, programmes). The pages' hand-built nav and footer are wrapped once in
  `SHARED:NAV` / `SHARED:FOOTER` markers.
- **Page structure on drafts:**
  - nav reads Products · Network · Developer · About · Blog
  - the phone menu has Products, Network and Company groups
  - "Related reading" sits above the Closing CTA on 9 product pages (addn, agreeease, ai-booking-tool,
    atlas, corporate-booking-tool, developer, flink, glink, payment)
  - "Latest from the blog" sits above the footer on index
  - about gets the nav/footer only
- **Posts remapped to current pages.** CTAs reuse the nav's own descriptors. Three placeholder images
  that don't exist on drafts were swapped for existing Atlas/AgreeEase imagery, and the build now
  fails on a missing image.
- **`HANDOVER-BLOG.md`** is updated for drafts (file list, markers, `_shell`, deploy note) and committed
  on the branch. It is excluded from deploys via `.vercelignore`.

### Verified

- `build-site.py --check` exits 0.
- All 11 pages are byte-identical to codex/drafts outside the shared regions plus one CSS link
  (checked with a script).
- Preview at 1440 and 375: no sideways scroll and no failed resource loads on blog, a post, payment
  and glink. The phone menu opens with 11 links.
- **Not deployed.** Production deploys by Vercel CLI from the codex/drafts working tree.

**Vercel topology (API, 2026-10-21):** project `fcg-website` (prj_bIBO2PVjRM052GwQXYZN0ZxoPCWB) is
Git-connected with **productionBranch = `main`**.
- **Production today** is a CLI deploy of `codex/drafts` (2026-08-26). `main` is still May V8.
- **Pushing `main` deploys production**, and would replace the June/August site with whatever is on
  `main`. Treat it as a deploy.
- **The push of `codex/blog` made a preview deployment:** fcg-website-f5tuhdsv1-crystalwong-accomycoms-projects.vercel.app.
  It returns 302 to the Vercel login (deployment protection), so viewers need team access.

### Blockers / next actions

- The tech team reviews `codex/blog`, merges it into `codex/drafts`, then deploys, and replies in the
  group chat on the CMS choice.
- **Done 2026-10-21:**
  - The 2 unpushed drafts commits were rebuilt as one clean commit, `a03ab11`, pushed to
    `origin/codex/drafts` (STATE-LOG, AGENTS.md preview rule, reference/DESIGN.md path). The six
    gitlinks were dropped. Backup of the old tip: local branch `backup/codex-drafts-pre-clean-20261021`
    (0435e10).
  - The superseded first attempt was cleared from this checkout: page/theme/DESIGN.md edits reverted,
    and its blog/partials/tools/js/css files plus the old handover doc removed. The workspace preview
    entry `fcg-blog-mirror` was removed and its server stopped.
  - `.impeccable/` (the critique archive) was left in place.
- The handover doc on `codex/blog` (`faa3ad8`) now warns that pushing `main` deploys production.
- Vercel API after the pushes: all new deployments are previews (target none). The live
  `/blog.html` still returns 404, so production is unchanged.
- `codex/blog` is one commit behind `codex/drafts` (`a03ab11` only touches docs). The merge should be
  clean.

### Learnings

**Problem.** A whole feature was built on the wrong branch's copy of a site.

**Approach.**
1. Find the live version: `git log --all -- <pages>`, `git branch --contains`, and curl the deployed
   URL for a page that exists on only one branch.
2. Make a worktree from the remote branch.
3. Port the reusable parts.
4. Re-derive the shared nav from the live pages, not the stale `_shell`.
5. Prove the page bodies are untouched with a strip-and-compare script.

**Judgment calls, what was NOT done and why:**
- Did not build on local `codex/drafts`: its 2 unpushed commits are WIP gitlinks.
- Did not merge into `codex/drafts` or deploy: the team reviews first, and production is a CLI deploy.
- Did not delete the first attempt: it needs Crystal's approval.

**Reusable rule.** Before editing a multi-branch site, confirm which branch the deployed URL serves.
The checked-out branch is not evidence.

## 2026-10-21 (later) — Blog wired through the whole site (WIP, uncommitted)

### What changed

All six critique actions ran (layout, shape, adapt, harden, typeset, polish).

- **One nav and footer for the site.** `partials/nav.html` and `partials/footer.html` are now the
  source. `python3 tools/build-site.py` copies them into the 11 live pages and the blog. Blog sits in
  the nav after About and in the footer's Company column. `index-variation-1.html` and `components.html`
  are skipped (archived variant and design reference).
- **Working phone menu on every page.** The hamburger used to jump to `#capabilities`. It now opens a
  drawer (`assets/js/fcg-nav.js`). Esc and link taps close it; the current page is underlined in orange.
- **Blog from one data file.** `blog/posts.json` drives:
  - the index cards
  - the "Latest from the blog" strip on index.html
  - "Related reading" on each product page (topped up to 3 with the latest posts)
  - one page per post, built from `blog/_post.html`
  - `blog/feed.xml`
- **Article page:**
  - breadcrumb, title, dek and byline
  - hero image and a 680px reading column
  - a dark product call-to-action card
  - "Keep reading" related posts
  - canonical, OG and BlogPosting JSON-LD
  - noindex plus a visible draft note while `draft: true`
- **Blog index:**
  - eyebrow removed
  - topic filter is shareable via `?topic=`, with a live "Showing N posts" count
  - chips are 44px tall, with a fade cue on phones
  - one link per card (stretched-link pattern)
  - reduced-motion guard
  - the subscribe form says it isn't connected instead of faking success
  - the pager was removed (one page of posts)
- **Contrast and tokens:**
  - card meta uses `--fcg-muted` (5.8:1)
  - the email placeholder was fixed
  - the LIVE.NETWORK badge uses `--fcg-live-text` (#c2410c) in light mode on every page
  - footer text is 12px instead of 10.4px
  - DESIGN.md now notes that Inter is the real meta font (JetBrains Mono is never loaded)
- **Leaner blog.html.** It is 1,627 lines shorter. Its head CSS moved to `assets/css/fcg-chrome.css`
  and `assets/css/fcg-blog.css`.
- **Nav copy unified.** The AI Booking Tool descriptor on `ai-booking-tool.html` was the one page that
  differed; it now matches the other ten.

### Verified (local preview at 1440 and 375, light and dark)

- `build-site.py --check` exits 0 after a build.
- The impeccable detector shows 0 low-contrast findings on blog.html (it was 8).
- No console errors, and no page-level sideways scroll on the blog, a post, index or agreeease.
- The menu opens and closes, and `?topic=engineering` shows 2 posts.
- An independent code review found 3 issues, all fixed: `{{` in post text crashed the build, removed
  posts left orphan pages, and drafts leaked into the RSS feed. Each fix was re-tested on a temp copy.

**Wrong base found (2026-10-21):** the blog work was built on the May 12 "Full Website V8" pages,
which are on `main` and `portal-redesign-direction-b`. The current marketing site is `codex/drafts`.
It has June to August commits, a new 4-item nav, a light footer and a different page set (payment,
glink, flink, developer, addn; no api-access or whitelabel). fcg-website-one.vercel.app serves the
`codex/drafts` version: `api-access.html` and `blog.html` return 404 there. The blog needs porting
onto `codex/drafts` before any commit, and HANDOVER-BLOG.md's page list must be updated to match.

### Blockers / next actions

- **Commit branch:** Crystal to choose; `codex/drafts` was proposed. Commit only these files:
  - the 11 pages, `blog.html` and `blog/`
  - `partials/`, `tools/`, `assets/js/`
  - the 3 CSS files
  - DESIGN.md and STATE-LOG.md

  Leave out the unrelated portal and `__pycache__` changes in the tree.
- **Real posts:** replace the placeholders in `blog/posts.json`, set `draft: false` and a `date`, then
  rebuild.
- **Handover:** `HANDOVER-BLOG.md` (Simplified Chinese) is for the Chinese tech team. It covers the changes,
  the build, the post fields and a checklist. It asks 10 questions on how posts get uploaded, and
  recommends a Git-based CMS for the team to decide on (Pages CMS preferred; Decap, Tina and
  Sanity/Contentful compared). Crystal has the real post content ready. Fill in the reply channel in
  section 7 before sending.
- **Subscribe:** choose an email provider and wire it in `assets/js/fcg-blog.js`.
- **Domain:** `SITE` in `tools/build-site.py` assumes https://www.fusionconnectgroup.com for
  canonical/OG/RSS. Confirm it at launch.
- **Shared head CSS:** other pages still carry their own inline copy of the nav CSS. Only the blog pages
  use `fcg-chrome.css`.

### Learnings

**Problem.** Add a blog link and a phone menu to 12 hand-copied static pages without a framework, and keep them in sync.

**Approach.**
1. Hash each page's nav and footer to find the canonical copy and the outliers.
2. Make the canonical copy a partial.
3. Use a stdlib script that rewrites only the regions between existing marker comments.
4. Drive the blog cards, strips, post pages and feed from one JSON file.
5. Add a `--check` mode so drift is detectable.

**Judgment calls, what was NOT done and why:**
- No JavaScript include (no fetch of partials): it would break no-JS, SEO and the first paint.
- No static site generator: there is too little content to justify one, and Vercel serves the folder as-is.
- The other pages' inline head CSS was left alone: rewriting it is a larger, riskier change than the
  request covered.
- Drafts got noindex rather than invented dates.

**Reusable rule.** To share chrome across a static site, hash the copies first, then sync from one
partial between markers with a `--check` mode. Don't move rendering to the client.

## 2026-10-21 — Blog page (WIP, uncommitted)

### What changed

New `blog.html` at the repo root: a Cloudflare-blog-style layout in FCG styling. Large heading and
intro, email subscribe field, topic filter buttons, one featured post, a 3-column card grid and a
pager. The nav, footer, theme toggle and script are copied from `about.html`, so they match exactly.
The page's own nav and footer link to Blog.

### Decisions

- **All posts are labelled placeholders.** Titles, excerpts and dates say "Placeholder", so no
  FCG articles were invented.
- **Built in this repo, not on the live site.** fusionconnectgroup.com runs on Wix (DNS only on
  Cloudflare), so the page can't be pushed there from here.
- **Not committed.** The checkout is on `portal-redesign-direction-b`, which auto-deploys the Open
  Developer Platform and already has unrelated changed screenshots. The marketing site's branch
  is `codex/drafts`.

### Verified (local preview only)

Light and dark mode both render. At 375px the grid is one column with no sideways scroll. The
Engineering filter shows its 2 posts. No console errors. Preview: `fcg-blog-mirror` in the
workspace `.claude/launch.json`, serving a copy of the page from the session scratchpad.

Follow-up: the page opens in light mode, as the code already defaulted to light (the dark view came from a
saved test toggle in the preview, now cleared). Card footers now wrap, so the topic label stays inside
narrow cards.

### Critique (/impeccable, same day)

Score 18/36 (Acceptable). The two P0s: the blog has no inbound links, and there is no article template
(every card links to `#`). The P1s: the phone menu is broken site-wide (the hamburger links to
`#capabilities` on index, about, api-access and blog), and canonical/OG/RSS/schema are missing.
The P2: faint meta text (3.9:1), orange-on-light text (2.6:1), and JetBrains Mono that is never loaded
(the theme forces Inter with !important). Snapshot: `.impeccable/critique/2026-10-21T09-10-17Z__blog-html.md`.

**Crystal's decisions:** fix all the issues; Blog goes top-level in the nav after About; the blog
launches with the redesign, not on Wix.

### Blockers / next actions

- Crystal to choose the commit branch (`codex/drafts` was proposed).
- Add a Blog link to every other page's nav and footer.
- Replace the placeholder posts with real content.
- Connect the subscribe form; it currently only changes its button text.
- Wix question settled: the blog launches with the redesign.
- Action order: shared nav/footer + Blog everywhere, then the article template, then the phone menu, then SEO basics, then contrast/fonts, then polish.

## 2026-09-08 (session 5) — Open Developer Platform everywhere

### What changed

The rename now covers the whole portal, not just the header: hero `h1`, all sixteen page `<title>`s,
the meta descriptions and the footer brand line. No built page in any locale contains the old name.

**The nav lockup went back to one text node.** Instead of a `<br>`, a 128px cap on `.brand-sub` lets
each language break where it wants: `OPEN DEVELOPER` measures 123px and the full string 191px, so
English wraps as `OPEN DEVELOPER` / `PLATFORM`, while `开放平台` / `開放平台` fits on one line. Neither
language needs a translation of the bare word "Open", which the `<br>` version had forced.

Twenty-six translation keys the rename orphaned were removed. Both tables hold the same 841 keys.

### Decisions

- **Measure, then cap.** The break point is a measured number, not a guess: any cap between 123px and
  191px produces the requested split, and 128px leaves a little headroom without admitting a third word.
- **The Chinese hero is unchanged by the rename.** `FCG Open Developer` maps to `FCG` and the
  heading-scoped `h:Platform` override still supplies `开放平台`, so the hero reads `FCG` / `开放平台`
  exactly as before.
- **Derived the new translations rather than retyping them.** Every renamed string is an old one with
  "Open " inserted and the same Chinese value, so the new keys were generated from the old table and
  the old keys deleted. Two strings needed a human decision: `Open Developer Platform` → `开放平台`
  and `FCG Open Developer` → `FCG`.

### Verified

`verify-pages.js`: 0 failing checks out of 48, in each of the three locales. Header still flush to the
content column at 1440 / 1366 / 1280 / 1180 / 1100 / 1024. Live after the push of `dcb5673`
(deployment READY from `source: git`, four seconds later): the English header serves
`Open Developer Platform`, zh-Hant serves `開放平台`, the hero serves `FCG Open Developer<br>Platform`,
`/sandbox.html` titles as `Sandbox Environment — FCG Open Developer Platform`, and the old name
appears zero times on the live homepage.

### Learnings

**Problem.** Roll a name change through generated pages and two translation tables without hand-editing
forty strings or leaving the tables holding both spellings.

**Approach.** Rename in the source of truth (one `str.replace` in `pages_content.py`, three literals in
the donor), let the build's missing-string report enumerate the fallout, then derive each new Chinese
value from the old key rather than retyping it — the mapping is "same string with a word inserted", so
the translation is unchanged. Finish by deleting the keys that are no longer extracted from any page.

**Judgment calls — what was NOT done, and why.**
- Did not keep the `<br>` from the previous pass. It forced every locale into the same break and made
  the bare word "Open" a translatable string that Chinese has no use for.
- Did not guess the wrap width. Two measurements settled it; a `ch` or `em` cap would drift with the font.
- Did not leave the orphaned keys in place. They are harmless to the build but leave two spellings of
  every page title for the next person to choose between.
- Did not touch the marketing site at the repo root. Its header carries no `brand-sub` lockup, and the
  rename request was about the portal.

**Reusable rule.** For a rename across generated output, edit the source, let the build's own failure
list the consequences, and derive the new translations from the old ones by transformation. Then sweep
the keys nothing extracts any more, or the table grows a second copy of itself every rename.

## 2026-09-08 (session 4) — Header lockup renamed, on two lines

### What changed

The header brand lockup reads **Open Developer Platform** on every page, on two lines: `OPEN` above
`DEVELOPER PLATFORM`. The brand link's `aria-label` follows the new name.

One extra word does not fit on one line. The header already sat flush against the 1200px content
column with zero slack, so a third word would have pushed it past the column again and scrolled the
document sideways below ~1230px. Breaking after the qualifier keeps `DEVELOPER PLATFORM` as the
longest line, so the brand column keeps its exact width and the header still aligns from 1180px up.

### Decisions

- **One text node per line, not a CSS wrap.** Natural wrapping at any width that fits
  `DEVELOPER PLATFORM` breaks as `OPEN DEVELOPER` / `PLATFORM`, which splits the noun phrase. An
  explicit `<br>` gives the reading order the label wants.
- **Each locale sets its own break.** `开放平台` / `開放平台` already carries "open", so a literal
  translation of `Open` would have read "Open Open Platform". The first line takes `开发者` /
  `開發者` instead, so Chinese reads Developer / Open Platform on two lines.
- `.brand-div` grew from 20px to 27px so the rule spans a two-line label rather than half of it.
- Mobile is unchanged: `.brand-div` and `.brand-sub` are already hidden under 640px.

### Left alone deliberately

The request was the header. Three other places still carry the old name, and changing them is a
naming decision rather than a layout one:

- The homepage hero `h1`: `FCG Developer<br>Platform`.
- Every page `<title>`: `… — FCG Developer Platform` (index.html's own title is already
  `Open Developer Platform`, so the set is already inconsistent).
- The footer brand line: "The FCG Developer Platform: standardised APIs and flexible SDKs…".

### Verified

`verify-pages.js`: 0 failing checks out of 48, in each of the three locales. Header sits flush to the
content column at 1440 / 1366 / 1280 / 1180 / 1100 / 1024, no document overflow at any of them.
Live on the production URL after the push of `0a4d5be`: the English header serves
`Open<br>Developer Platform` and zh-Hant serves `開發者<br>開放平台`, deployment READY from
`source: git` five seconds after the push.

### Learnings

**Problem.** Add a word to a header lockup that had no horizontal room left, without breaking the
Chinese editions.

**Approach.** Check the constraint before the copy: the header's right edge was already flush with
the content column, so this was a layout problem wearing a copy request. Break the label into two
lines at the qualifier, then confirm the longest line is unchanged — that is what keeps the column
width, and therefore the alignment, intact. Verify at every breakpoint, not just the design width.

**Judgment calls — what was NOT done, and why.**
- Did not let CSS choose the break. The only widths that fit `DEVELOPER PLATFORM` also fit
  `OPEN DEVELOPER`, so natural wrapping splits the noun phrase every time.
- Did not translate `Open` literally. Chinese already says "open platform"; a literal line would
  have doubled the word.
- Did not shrink the nav type further to fit one line. It is already at 13px, down from 13.5px
  earlier today, and a fourth reduction would be paying for a line break with legibility.
- Did not rename the hero h1, the page titles or the footer line. The ask was the header, and those
  are a naming call for Crystal.

**Reusable rule.** When a copy change lands in fixed chrome, measure the chrome first. If the
element is already flush to its column, the change is a layout task, and the test of a two-line fix
is whether the longest line stayed the same.

## 2026-09-08 (session 3) — The marketing globe, and the portal deployed

### What changed

**Coverage Map runs the marketing site's Cobe globe.** The hand-drawn SVG wireframe is gone.
`pages_content.py` reads the inlined Cobe IIFE out of the repo-root
[index.html](index.html) at build time rather than copying it, so the portal and fcg.com cannot
drift. Same fourteen cities, same `#F97316` markers, configured for the portal's light palette
(`dark:0`, `--card` glow, `mapBrightness:2`).

**Deployed to production** — [fcg-open-developer-platform.vercel.app](https://fcg-open-developer-platform.vercel.app).
All 48 pages live, both Chinese locales included.

### Decisions

- **Route arcs dropped.** On the marketing site they are labelled flight routes (`BKK → LHR`),
  which say nothing about hotel coverage; unlabelled they would be pure decoration.
- **Labels on the eight larger markers only**, positioned on whichever side of the sphere the point
  sits so no per-city offsets are needed, with a front-most-first collision pass. The marketing
  site's fourteen hand-tuned labels turn into a smudge at 460px.
- **Label threshold raised to `z > 0.32`.** At the marketing site's 0.18 a label appears while still
  3px blurred and reads as a smear against the panel edge.
- **`.vercelignore` added** to the variant folder. Without it a static deploy would serve
  `build-pages.py`, `pages_content.py` and the translation tables off the public URL.
- **Account map corrected.** `~/.claude/project-accounts.md` had no row for this project.

### The hosting picture, established by API

Two Vercel projects on work team `team_SyKixqrcZUCIGFNYQC13rwVl`:

- `fcg-website` (`prj_bIBO2PVjRM052GwQXYZN0ZxoPCWB`) — Git-connected to `cwong-acmy/fcg-website`,
  production branch `main`.
- `fcg-open-developer-platform` (`prj_dhe1toSi7yeTJOKGuUsOwKWqhUuG`) — **no Git connection at all.**
  CLI-deployed only. Its previous and only deployment was `source: cli` at 13:59 on 8 September,
  which is why the live URL showed the pre-mega nav and 404'd on the four new pages while the
  branch had been pushed for hours. **Pushing to GitHub does not update this URL.**

### Verified against the real destination

On `https://fcg-open-developer-platform.vercel.app`, not localhost: `/`, `/sandbox.html`,
`/request-trace.html`, `/coverage-map.html`, `/hotel-mapping.html`, `/zh-Hant/coverage-map.html`
and `/zh-Hans/sandbox.html` all return 200. `/build-pages.py`, `/pages_content.py` and `/i18n.py`
return 404, so the ignore file holds. The live coverage page reports `globeOpacity: 1` with labels
rendering and no page errors. Deployment `dpl_9kUm1CQCoGSvrqgJHm2nBeiGc18P`, from commit `6d819bd`.

`verify-pages.js` locally: 0 failing checks out of 48, in each of the three locales.

### Git connection (added same session)

`fcg-open-developer-platform` is now connected to `cwong-acmy/fcg-website`, root directory
`open-portal-redesign/variant-b-impeccable`, **production branch `portal-redesign-direction-b`** —
not `main`, because `main` has no `open-portal-redesign/` directory at all (it is at
`6999dd1 Checkpoint: Full Website V8`, the marketing site only). A production build from `main`
would have had no root directory to build.

Two API notes worth keeping. `PATCH /v9/projects/{id}` rejects both `link` and `productionBranch`
as unknown properties; the production branch is set by **`PATCH /v1/projects/{id}/branch`** with
`{"branch": "..."}`. And `POST /v9/projects/{id}/link` accepts a `productionBranch` field but
silently ignores it — it returned `main` after being asked for the branch.

`vercel.json` was added alongside `.vercelignore`: the ignore file only governs what the CLI
uploads, so once the project builds from GitHub the Python generator needed a route-level 404 too.

**When this branch merges to `main`, the production branch setting must move with it**, or the live
URL silently freezes at the last commit to the old branch.

Proven end to end: the push of `54bd2d8` at 07:20:48Z produced a `source: git` production deployment
at 07:20:52Z, branch `portal-redesign-direction-b`, state READY. On the live URL afterwards, all seven
sampled pages return 200 across the three locales, and `/build-pages.py`, `/pages_content.py`,
`/i18n_zh_hans.py`, `/__pycache__/...` and `/vercel.json` all return 404.

### Blockers / next actions

- `open-portal-redesign/shots/b-pages` still holds 45MB of regenerated PNGs, uncommitted.

### Learnings

**Problem.** "Use the globe from the FCG website" on a page in a sibling build, and work out why a
Vercel URL that certainly exists was serving a version from before the day's work.

**Approach.** For the globe: find the real implementation rather than reproducing its look — it was
an inlined Cobe IIFE in the marketing `index.html`. Read it at build time so there is one copy, and
re-tune only what the new context changes (palette, size, label density). For the URL: ask the
provider API which project serves it, then read `link` and the deployment `source` rather than
assuming a Git connection exists.

**Judgment calls — what was NOT done, and why.**
- Did not copy the 11.6KB Cobe build into `pages_content.py`. A second copy drifts the first time
  either file is touched; reading it keeps one source and the assert fails loudly if it moves.
- Did not keep the route arcs, and did not relabel them as something coverage-related. Both would
  have been decoration dressed as data.
- Did not carry over the marketing globe's `HOTELS: 4.3M+` overlay. It is a marketing figure, not a
  portal fact, and this page deliberately carries no counts.
- Did not deploy from the repo root. Root `.vercel/` points at `fcg-website`, a different project;
  deploying from there would have pushed the marketing site into the portal's URL.
- Did not assume the missing pages meant a failed deploy. The deployment was `READY` — it was simply
  older than the work, which the API's `created` timestamp settles in one call.

**Reusable rule.** When asked to reuse a component from a sibling surface, import the implementation
at build time rather than reproducing the appearance. And when a live URL looks stale, read the
project's `link` and its latest deployment's `source` before touching anything: "pushed to GitHub"
and "deployed" are the same sentence only when a Git connection exists.

## 2026-09-08 (session 2) — The four Products pages, built and design-checked

### What changed

**Sandbox, Request Trace, Coverage Map and Hotel Mapping are real pages.** The Products mega menu's four
placeholder destinations now point at
[sandbox](open-portal-redesign/variant-b-impeccable/sandbox.html),
[request-trace](open-portal-redesign/variant-b-impeccable/request-trace.html),
[coverage-map](open-portal-redesign/variant-b-impeccable/coverage-map.html) and
[hotel-mapping](open-portal-redesign/variant-b-impeccable/hotel-mapping.html), authored in
[pages_content.py](open-portal-redesign/variant-b-impeccable/pages_content.py) and built in all three
locales. The portal is 16 pages × 3 locales = 48.

Content came from the console captures in
[reference/console-dev](open-portal-redesign/reference/console-dev) — the four screenshots plus
`_text.json` — rewritten into FCG's declarative voice in British English. Nothing was invented: where the
console shows a control but not its data (batch statuses, coverage counts), the page describes what the
control reports instead of showing a fabricated number.

**Coverage Map carries the one new component**: an orthographic wireframe globe, tilt 18°, centred on
60°E, with hidden-line removal, plotted from real city coordinates and sized by the console's own legend
bands. Geometry is generated once and baked in, not computed at build time.

**Nav and chrome:** the Products trigger now takes an active state on the four menu-only pages, the
footer picks all four up, and `verify-pages.js` covers them.

### Decisions

- **Extension, not a new visual world.** Impeccable's `context.mjs` asked for `init`/PRODUCT.md first;
  skipped deliberately. `open-portal-redesign/DESIGN-SYSTEM.md` plus the twelve built pages already are
  the authority, and interviewing for product truth would have re-derived what the repo states.
- **No fabricated data anywhere.** Request Trace shows an illustrative table with `{trace_id}`-style
  placeholders and a `.disclaim`, which is the pattern index.html already uses. Hotel Mapping's batch
  history became a column-definition list instead of a second placeholder table — repeating the device
  twice would have read as filler.
- **Grouped IA taken from the console.** Two rails: App Management / Sandbox / Request Trace (the
  console's "Integration & Debugging") and Coverage Map / Hotel Mapping (its "Hotel Catalog").
- **Nine filters two-up.** A nine-row full-width definition list read as a second essay directly under a
  six-row one; the two-column variant reads as a lookup.

### Fixed along the way

- **`i18n.py` dropped the slash from self-closing tags.** Harmless for `<br/>`, fatal for SVG: `<circle
  .../>` came out as `<circle ...>`, so every shape after it nested inside a shape and the globe rendered
  as an empty ring in both Chinese locales. Fixed in `handle_startendtag`; the empty-table round-trip is
  still byte-identical across all 16 English pages.
- **The header overflowed the 1200px content column.** Pre-existing: it sat 51px past the column at every
  width and scrolled the document sideways below ~1180px. The sixth nav pill made it worse. Header
  metrics tightened (pill padding, gaps, 13px nav type) so it aligns exactly from 1180px up, and the
  drawer now takes over below 1180 instead of the header spilling.
- Bare `<code>` in a table cell or flow strip fell back to the browser's monospace rather than `--mono`.

### Verified

`verify-pages.js` across all three locales: **0 failing checks out of 48 per locale**, no JS errors, at
1280 / 768 / 375. Full-page captures reviewed at 1440 and 390 for all four pages plus zh-Hant. No dead
internal links across all 48 pages. Build reports both Chinese locales fully translated (430 new strings).

### Blockers / next actions

- The `small-orange` advisories the verifier prints are the documented `--accent-ink` contrast trade-off
  Crystal chose, not regressions.
- Orphan `__pycache__` entries exist for `build-console.py`, `console_content.py`, `console_nav.py` and
  `build_console_globe.py` whose sources are not in the tree. Left alone — worth asking about.

### Learnings

**Problem.** Add four pages to a twelve-page generated portal so they read as native to it, using a real
console as the source of truth, without inventing product facts.

**Approach.** Read the incumbent's own design spec and one representative page before writing anything,
then author only in the vocabulary that already exists (band, cards, steps, tbl, chips, note, rail) and
add exactly one new component. Take content from the console captures; where the capture shows a control
with no data, describe the control. Let the build's copy-rule gates and `verify-pages.js` be the checker
rather than self-assessment.

**Judgment calls — what was NOT done, and why.**
- Did not run Impeccable's `init` gate. A documented design system and twelve shipped pages already carry
  more product truth than an interview would have produced, and the skill's own routing allows extension
  on the incumbent.
- Did not fabricate metric values to fill the console's stat strips. All-zero counters look broken and
  invented ones are worse; naming what each counter reports keeps the page honest and still useful.
- Did not build a geographically accurate coverage map. Real per-region counts do not exist on the
  portal, so the globe is labelled illustrative and plots city coordinates for shape, not for claims.
- Did not add a second placeholder table on Hotel Mapping, and did not create stub pages for controls
  that need authentication.
- Did not fix the header overflow by shrinking only the new element. The defect predated the mega menu
  and needed the whole header re-fitted to the column.

**Reusable rule.** When extending a generated site, the incumbent's spec plus one representative page is
the brief; add at most one new component and let the project's own build gates and verifier decide when
it is done. And when a parser rewrites markup, test it against SVG — HTML void-element assumptions break
silently in foreign content, and the failure is invisible in the source locale.

## 2026-09-08 — Products mega menu in the Direction B nav

### What changed

**A `Products` mega menu** in the portal's pill nav, from a screenshot Crystal supplied: three columns
(Start / Build / Operate) with nine icon-and-description links. Added to
[build-pages.py](open-portal-redesign/variant-b-impeccable/build-pages.py) as a `MEGA` table, so all
twelve pages in all three locales get it from one definition. `Home` left the top-level nav (the logo
still links home) and moved into the mobile drawer under a `More` group, matching the screenshot.

CSS and the ~20 lines of behaviour went into
[index.html](open-portal-redesign/variant-b-impeccable/index.html), the shell donor, so they propagate
on the next build. Click to toggle, click-away and Escape to close, focus returns to the trigger.
17 new strings added to both Chinese tables; build reports fully translated.

### Decisions

- **Existing tokens only, no new icon.** The panel is `--hair` borders, `--shell` hover, `.micro`
  eyebrows, 999px pills, Inter — the same grammar as the rest of the header. The chevron is the shared
  `solar:arrow-right-linear` rotated 90°, so the menu adds nothing to the icon payload. Every mega icon
  is one already used elsewhere in the build, so no unverified Iconify name can silently render blank.
- **No stub pages for the four console surfaces that do not exist.** Sandbox, Request Trace, Coverage Map
  and Hotel Mapping point at the nearest real surface (`index.html#start-integration`,
  `api-docs-errors.html`, `index.html#network`, `api-docs-hotel-process.html`). Empty stubs would look
  like shipped pages in a prototype that is being reviewed for direction.
- **Click, not hover, to open.** Hover intent needs timers and a safe triangle; the click toggle is
  keyboard- and touch-correct with no extra state.
- **Mobile drawer repeats the mega, then adds whatever top-level links it misses.** The `seen` set is
  computed from hrefs, so the drawer cannot drift from the panel when `MEGA` or `NAV` changes.

### Verified

Local server, en and zh-Hant at 1440×900 and 375×812: panel renders as designed, toggle / click-away /
Escape all correct, drawer groups render, Chinese copy fits the columns. Build: 36 pages, both locales
fully translated.

### Blockers / next actions

- Crystal to confirm the four placeholder destinations, or ask for real stub pages.
- Not committed, not deployed — working tree only, on `portal-redesign-direction-b`.

### Learnings

**Problem.** Add a mega menu to a portal whose twelve pages are generated from one donor file, without
letting the nav drift between pages or locales.

**Approach.** Put the content in one Python table and derive three consumers from it — the desktop panel,
the mobile drawer, and the drawer's "everything the panel missed" list via a set of hrefs. Put CSS and JS
in the donor `index.html`, never in a generated page. Add the English strings, run the build, and let its
hard-fail on untranslated strings enumerate exactly what the Chinese tables need.

**Judgment calls — what was NOT done, and why.**
- Did not invent Iconify names. Every icon was grepped out of the existing pages first; a wrong Solar name
  renders as blank space with no error, which a screenshot review would miss.
- Did not create stub pages for the four missing console surfaces. In a direction review, a stub reads as
  a shipped page and invites feedback on work that does not exist.
- Did not add hover-to-open. It needs open/close timers and a safe-triangle to not fight the pointer, for
  a nav that already works from click, keyboard and touch.
- Did not hand-translate before building. The builder's missing-string report is the authoritative list;
  guessing it produces both gaps and dead keys.

**Reusable rule.** In a generator with a donor file, new chrome goes in exactly two places — one data table
for content, the donor for CSS and behaviour. Let the build's own failure mode enumerate the follow-up work
instead of predicting it.

## 2026-09-07 (session 2) — Simplified and Traditional Chinese, and a design-system spec

### What changed

**36 pages now: English, Simplified Chinese and Traditional Chinese**, twelve each, at
[variant-b-impeccable/](open-portal-redesign/variant-b-impeccable) with `zh-Hans/` and `zh-Hant/`
subdirectories. The language control is real cross-locale links, wired correctly in all three
directions, with the current locale marked `aria-current="page"`.

**Only copy changes between locales, never layout** — enforced by construction, not by discipline.
[i18n.py](open-portal-redesign/variant-b-impeccable/i18n.py) parses the built English page and swaps
**text nodes and four translatable attributes only** (`placeholder`, `aria-label`, `title`, `content`).
CSS, tokens, classes and markup are byte-identical across locales because nothing else is touched.

**A design-system spec** → [DESIGN-SYSTEM.md](open-portal-redesign/DESIGN-SYSTEM.md). Written to be
followed cold for a new page or an app screen: tokens, the accent law, type scale, the enforced copy
rules, every component with real CSS, the motion rules, the layout traps that shipped as bugs in this
build, the accessibility floor, and a section on what changes when applying this to app UI rather than
marketing pages.

### Decisions

- **Translate the built HTML, not the content source.** Duplicating `pages_content.py` per locale would
  have tripled 1,200 lines of structure and let the design drift silently between languages. Swapping
  text nodes makes design drift impossible.
- **Proved the round-trip is lossless before authoring a single translation.** Translating with an empty
  table must reproduce the input byte-for-byte. It did not at first: Python's `HTMLParser` lowercases
  attribute names, so `viewBox` became `viewbox` and the inlined wordmark stopped rendering. Fixed with
  a small camelCase restore map, and losslessness is now asserted on every build — a new camelCase SVG
  attribute fails the build rather than silently breaking a logo.
- **Traditional Chinese is written for Taiwan/Hong Kong, not converted.** No converter was installed and
  installing one needs approval, but hand-authoring was the better answer anyway: the regional IT and
  travel vocabulary differs, so a glyph conversion produces mainland phrasing in Traditional characters.
  介面 not 接口, 資料 not 數據, 伺服器 not 服務器, 金鑰 not 密鑰, 簽章 not 簽名, 權杖 not 令牌,
  回呼 not 回調, 飯店 not 酒店, 開票 not 出票, 票價 not 運價, 登入 not 登錄, 主控台 not 控制台,
  使用者名稱 not 用戶名, 電子郵件 not 郵箱, 原始碼 not 源碼, 簽核 not 審批, 商旅管理公司 not 差旅管理公司.
- **Nothing is silently left in English.** The build reports every string with no table entry and exits
  non-zero. Both tables hold 606 entries with identical key sets and zero untranslated strings.
- **Product names, endpoint paths, error codes, field names and partner lockups stay as-is** in every
  locale. Pattern-matched (a leading `/`, an `MCP001`-shaped code, a camelCase identifier, an install
  command) rather than listed one by one.

### Also in this session, before the Chinese work

- **The orange pass** Crystal asked for, against three screenshots of the marketing site's own treatment:
  orange eyebrow labels, an orange second clause on a headline, an orange lede lead-in, a tinted status
  chip, orange mono card labels, one filled orange circular arrow on tertiary links. Buttons and panels
  stay ink. Small orange text resolves through `--accent-ink`, so switching to the AA-passing `#C2410C`
  is one value.
- **Three copy rules, each enforced by the build and proved by deliberately breaking it:** an orange
  `<em>` clause must follow a comma; an `<h1>` is a title and never ends in a full stop; one orange
  emphasis per block. The orange clause is `display:block`, so a comma never orphans a word.
- **A motion pass** on Emil Kowalski's framework — press feedback on every pressable, every hover gated
  behind `(hover:hover) and (pointer:fine)`, custom curves, 160ms hover, 60ms stagger, layout properties
  moved onto `transform`, the drawer transitioning with `allow-discrete` plus `@starting-style`, and
  reduced-motion keeping opacity and colour rather than nuking every transition.
- **Chips audited against the page.** Seven band chips removed for restating the heading or lede directly
  below them; eight remain. Chips ride the eyebrow line, never the CTA row.
- **Mobile fixes:** the tab rail now wraps instead of scrolling (a scroller hid options behind an edge),
  buttons size to content with the label flush left, the drawer's CTA pill renders correctly, Login is a
  full-width button there with Register kept in the header, and the language control is a full-width
  three-way segmented row.

### Verified

- `verify-pages.js` — 12 pages × 1280 and 375, per locale. **English 24/24, zh-Hans 24/24, zh-Hant 24/24**,
  no JS errors. It takes an optional locale argument: `node verify-pages.js zh-Hans`.
- `verify-motion.js` — **12/12**, no `transition:all`, no `scale(0)` entry, no `ease-in` on UI, no UI
  transition over 300ms, no layout property animated, `:active` on every pressable, every hover gated.
- Static: CSS token block and all `class` attributes byte-identical across the three locales; every
  internal link resolves in every locale; the language switcher's nine cross-locale hrefs are correct.

### Still open

- **Nothing is deployed.** The live marketing site is served from OneDrive `07 Website` on nginx, not
  this repo and not Vercel. The portal redesign has no deployment target agreed.
- **The AA call on small orange text** is Crystal's, reversible in one token.
- **Image generation still blocked** — both Google AI Studio keys return `429 free_tier limit 0`;
  Higgsfield needs an interactive `hf auth login`. Brand-kit raster boards unbuilt, prompts stored.
- **Six duplicate full-tree folders** remain untracked junk needing Crystal's approval to delete, along
  with `.vercel/` and `.claude/`.
- **All of this is on branch `portal-redesign-direction-b`**, not `main`, and is not pushed.

### Learnings

**Problem.** Ship three language editions of a twelve-page site without the design drifting between
them, while the brief kept changing.

**Approach.** Separate the two things that were being conflated: structure and copy. Generate the page
once, then swap only its text nodes — so "the design is identical across locales" stops being a promise
and becomes a property of the pipeline. Before authoring 1,352 translations, prove the swap is a no-op
when the table is empty. Then drive the untranslated-string count to zero and let the build fail if it
is ever non-zero.

**Judgment calls — what was NOT done, and why.**
- Did not duplicate the content module per locale. Three copies of the structure is three places for the
  design to diverge, and the divergence would be invisible until someone opened two languages side by side.
- Did not author a single translation until the identity round-trip was byte-for-byte clean. It was not,
  and the failure was silent: a lowercased `viewBox` breaks the logo without any error.
- Did not install a Simplified-to-Traditional converter, and would not have used one if it were present.
  It solves the glyphs and leaves the vocabulary wrong for the audience.
- Did not translate product names, endpoint paths, error codes or API field names, and matched them by
  shape rather than listing them, so a new endpoint does not need a table entry.
- Did not accept the horizontal-scroll check as proof of no clipping — `body{overflow-x:hidden}` turns
  overflow into silent truncation, which is exactly how the tab rail shipped cut off.
- Did not fix visual bugs from the screenshot alone. Reading the computed style named the colliding class
  (`.path`) in one query; measuring the boxes showed a `min-height` was landing on the wrong element.

**Reusable rule.** When one artefact must exist in several variants, make the variance a pipeline
property rather than a copy: generate once, transform narrowly, and assert the transform is a no-op on
empty input before trusting it with real content. And turn each accepted rule into a build assertion the
moment it is agreed, then break it once to prove it fires.

## 2026-09-07 (later) — Direction B built out to 12 pages, then an orange pass

### What changed

**Built the eleven remaining portal pages in Direction B**, plus the homepage, at
[open-portal-redesign/variant-b-impeccable/](open-portal-redesign/variant-b-impeccable): app management,
G-Link docs (overview, integration flow, API reference), F-Link docs, error codes, SDK, Skills,
AI Assistant, login, register.

**One shell source.** [build-pages.py](open-portal-redesign/variant-b-impeccable/build-pages.py) lifts the
head, token block and behaviour script verbatim out of `index.html` and generates nav and footer from one
list, writing them back into `index.html` too. Tokens are byte-identical across all twelve files, checked.
Page content is in [pages_content.py](open-portal-redesign/variant-b-impeccable/pages_content.py).

**Content came off the live portal**, read on 7 September 2026: endpoint paths, methods, SDK versions and
install commands, error codes, rate limits. Nothing invented; copy rewritten into FCG's declarative voice
in British English.

**Then Crystal asked for more orange**, against three screenshots of the marketing site's own treatment.
Applied: orange eyebrow labels, an orange second clause on a headline, an orange lead-in phrase on a lede,
a tinted status chip (orange dot + orange label on a pale orange pill), orange mono card labels, and one
filled orange circular arrow on tertiary links. Buttons and panels stay ink.

### Decisions

- **Small orange text is now intended, and sits behind one token.** `--accent-ink` carries every orange
  label under 18px. `#F97316` on white is 2.80:1 and fails AA, which is what the earlier open question was
  about; Crystal chose to match the marketing site. Switching that single token to `#C2410C` (4.6:1) makes
  every small orange label pass without touching anything else. The required-field asterisk on the auth
  forms is ink, not orange, because it is the only visual marker of a required field.
- **Three copy rules, each enforced by the build rather than remembered.** `build-pages.py` refuses to
  build if any of them break, and each was tested by deliberately breaking it:
  1. An orange `<em>` clause must follow a comma. A headline with no comma stays entirely ink.
  2. An `<h1>` is a page title and never ends in a full stop. Section headings are sentences and keep theirs.
  3. One orange emphasis per block: if a heading carries an orange clause, its lede does not also get an
     orange lead-in.
- **The orange clause is block-level**, so a comma can never leave an orphan word at the end of the ink line.
- **Chips must add information the page does not already carry.** Seven band chips were removed for
  restating the heading or lede immediately below them. Eight remain: the Sandbox/Production ready badges on
  the Skills cards (the live portal's own treatment), `Online` on the AI Assistant, `New` on Skills. Chips
  ride the eyebrow line, never the CTA row.
- **Mobile buttons size to content with the label flush left.** Full-bleed pills read as banners on a phone
  and centre their label away from the text column. The form submit stays full width, as forms conventionally do.
- **Header keeps Register; the drawer carries Login as a full-width button** and a three-way
  ENG / 简体 / 繁體 control as a segmented row.
- **Did not extend the chooser.** Its job (pick a direction) is done, and its base64 `srcdoc` embedding
  would break the new cross-page links.

### Bugs found and fixed, all by measuring rather than reading code

- **`td class="path"` collided with the homepage's unscoped `.path` closing card** (`border-radius:24px`,
  `padding:40px 38px`, `display:flex`), rendering every path cell as an overflowing rounded panel. Table cell
  classes now carry a `t-` prefix. A sweep for classes styled in both CSS blocks showed `.path` was the only
  genuine collision; the rest are scoped or deliberate shared components.
- **The tab rail was clipped, not scrolling, below about 585px.** `.band-foot` sizes to content in a column
  flex container and `min-width:auto` stopped it shrinking, so `max-width:100%` on the rail never bit.
  `body{overflow-x:hidden}` meant no document scrollbar appeared and the horizontal-scroll check passed while
  content was silently cut off.
- **The donor script crashed on the auth pages** — the reduced header has no burger, and the unguarded
  `addEventListener` also killed the scroll-reveal observer on those two pages.
- **`.mnav a` was unscoped**, so `display:block` plus vertical padding flattened the drawer's CTA pills and
  pushed their labels outside. Now `.mnav ul a`.
- **`code.inl` was scoped to `.docs-main`**, so instances in chat bubbles and section ledes fell back to the
  browser's default monospace.
- **`min-height` for card-row alignment was hitting `.card-k`** (also a `<p>`), inflating the eyebrow and
  never touching the description.
- **The docs column had a flat 26px between every sibling**, giving a heading the same weight as a paragraph
  break. Now has real rhythm: open above a heading, tight beneath it.
- **Nav `<h4>` labels and the auth aside's `<h2>` sat before the `<h1>`** in the heading outline. They are
  navigation labels, not document headings, so they became `<p>` with `aria-labelledby` on a `<nav>`.

### Verified

[verify-pages.js](open-portal-redesign/verify-pages.js) attaches to Chrome for Testing on `:9222`, loads all
twelve pages at 1280 and 375, forces the reveal animations to their end state so full-page captures are not
blank, and asserts: no console or page errors, no horizontal scroll, nothing clipped by its `.wrap`, the
accent never filling anything at button scale, Inter throughout, one `h1` per page with no heading skips, no
dead `href="#"`, no table cell inheriting panel styling, card meta rows aligned within a visual row, and
`--accent-ink` holding an approved value. **24 / 24 pass, no JS errors.** Screenshots in
[shots/b-pages/](open-portal-redesign/shots/b-pages).

Static checks alongside it: every internal link resolves, and the `:root` token block plus the nav and footer
markup are byte-identical across all twelve files.

### Still open

- **Nothing is deployed.** The live marketing site is served from OneDrive `07 Website` on nginx, not this
  repo and not Vercel, so nothing here changes anything live. The portal redesign has no deployment target
  agreed yet.
- **The AA call on small orange text** is Crystal's, and reversible in one token if she wants `#C2410C`.
- **Image generation still blocked** — both Google AI Studio keys return `429 free_tier limit 0`; Higgsfield
  needs an interactive `hf auth login` from Crystal. Brand-kit raster boards remain unbuilt, prompts stored.
- **Six duplicate full-tree folders** (`about/`, `whitelabel/`, `atlas/`, `agreeease/`,
  `corporate-booking-tool/`, `advisory-implementation/`) are untracked junk from an old copy operation.
  Deleting them needs Crystal's approval. `.vercel/` and `.claude/` also left untracked.
- **This work is on branch `portal-redesign-direction-b`**, not `main`, and is not pushed.

### Learnings

**Problem.** Build eleven pages that must match one existing page exactly, then restyle all twelve to a
moving brief, without drift.

**Approach.** Make the existing page the shell donor rather than a thing to copy: lift its head, token block
and script verbatim at build time and generate nav and footer from one list, writing them back into the donor
too. Then, as each style rule arrives, encode it as a build assertion instead of applying it by hand, and
prove the assertion by deliberately breaking it.

**Judgment calls — what was NOT done, and why.**
- Did not hand-write twelve copies of a 450-line token block. Duplication is how "byte-identical" quietly
  becomes false three edits later.
- Did not trust the horizontal-scroll check. `body{overflow-x:hidden}` converts overflow into silent
  clipping, so a passing scroll check proved nothing; comparing each child against its `.wrap` content box
  found the real bug.
- Did not guess at the rounded-panel table cells from the screenshot. Reading the computed style named the
  colliding class in one query, and a sweep for classes defined in both stylesheets showed it was the only one.
- Did not fix the card-alignment defect by nudging a magic number after each failure. Measuring the actual
  boxes revealed the `min-height` was landing on the wrong element entirely.
- Did not add a "learn more" orange circle to primary CTAs, and did not let orange fill a button or panel,
  even while adding orange everywhere else it was asked for.
- Did not extend the chooser to the new pages. It had already served its purpose, and its embedding method
  is incompatible with cross-page links.

**Reusable rule.** When a brief arrives in pieces, turn each accepted rule into a build-time assertion and
break it once to prove it fires — otherwise rule five silently undoes rule two. And when a symptom is
visual, read the computed style before reading the source; the collision is usually a class name, not logic.

## 2026-09-07 — Live-source audit, brand kit, developer-portal redesign directions

### What changed

**1. Established what actually serves the live site.** `fusionconnectgroup.com` is **not** built from this
repo. Verified by byte-hashing every live page against every local candidate.

- Live host: nginx at `43.135.32.47` (Tencent Cloud range). **Not Vercel**, despite `.vercel/project.json`
  (`prj_bIBO2PVjRM052GwQXYZN0ZxoPCWB`, work team `team_SyKixqrcZUCIGFNYQC13rwVl`) sitting in this repo.
- Live source of truth: `~/Library/CloudStorage/OneDrive-SharedLibraries-FusionConnectGroup/FCG Marketing - Documents/07 Website/`.
  Every live page matches a file there byte-for-byte, except that the deployer stripped the space out of
  the `* _crystal-denzel-edit.html` filenames and rewrote the `%20` hrefs. Uploaded 20 July 2026.
- Only `components.html` in this repo matches live. Everything else is a stale May-2026 "Full Website V8"
  generation: `4.3M+` / `300+ partners` / US spelling, and pages (`whitelabel`, `advisory-implementation`,
  `api-access`, `ai-mapping`, `agent-booking-tool`) that were never live.
- **nginx serves the homepage as a catch-all for unknown paths**, so a 200 does not prove a page exists.
  Compare bytes, never status codes.

**2. Built the FCG brand kit** → [brandkit/](brandkit). `designlang` v12.15.0 full extraction plus a written
spec, with every token cross-checked against the live page's own inline `<style>` block.

**3. Built two developer-portal homepage directions** → [open-portal-redesign/](open-portal-redesign),
realigning `open.fusionconnectgroup.com/home` to the marketing brand. Direction A via `huashu-design`,
Direction B via `impeccable`, both assembled into a self-contained tabbed chooser.

### Decisions

- **The brand kit's authority is the live HTML, not designlang.** designlang's heuristics rank CSS
  frequency, not brand intent. It was right that Inter carries everything (Sora is loaded in the live
  `<head>` and never applied — do not reintroduce it), but its `foreground: #000000` and "Title Case"
  voice call both contradict the source (`#0F1114`; sentence case with a terminal full stop).
- **The accent rule is the whole system.** `#F97316` appears 49 times against ink's 188 and is never a
  surface — only status dots, section-eyebrow dashes, statistic unit suffixes, thin arcs, focus rings.
  The current portal breaks this with orange button and panel fills; both directions fix it.
- **Raster brand boards deliberately not faked.** The `brandkit` skill is image generation and every
  model refused on quota. Built the board in code from the real tokens and the real wordmark instead —
  more accurate than a model's approximation, and editable. Prompts stored for later.
- **Did not polish the losing variant.** Two known cosmetic defects in Direction A (faint partner-grid
  crosshairs, orange arcs spilling outside the globe) are logged, not fixed, until a direction is chosen.

### Blockers

- **Image generation: BLOCKED.** Both Google AI Studio keys in 1Password return
  `429 … free_tier_requests, limit: 0` for every Gemini image model — no billing on either project.
  Higgsfield returns `Not authenticated` and needs an interactive `hf auth login` from Crystal.
- **Open question for Crystal — small orange text.** `#F97316` on white is 2.80:1 and fails AA; it is one
  of the three contrast failures designlang flagged on the live site. Both directions independently set
  the eyebrow label in ink and kept only the dash orange. Recommended resolution: `#C2410C` (4.6:1) for
  small orange text, `#F97316` retained at display size. Awaiting her call.
- **External publication not done.** The chooser is local only; hosting it publicly needs her approval.
- **`brandkit` skill is not session-registered.** It lives at `Desktop/Claude/.claude/skills/brandkit`,
  one level above this project, so `Skill(brandkit)` fails with "Unknown skill". Read and followed the
  SKILL.md directly. Its `.agents/skills/brandkit` twin is byte-identical.

### Next actions

1. Crystal picks Direction A or B from [open-portal-redesign/choose.html](open-portal-redesign/choose.html).
2. Apply the small-orange-text decision to the chosen direction.
3. Build the remaining portal pages in the chosen direction: `/home/app-management`,
   `/home/api-docs/detail/hotel` (+ `/apis`, `/integration/process`), `/home/api-docs/detail/flink`,
   `/home/api-docs/errors`, `/home/sdk-assistant`, `/home/skills`, `/home/ai-assistant`, `/login`, `/register`.
4. Decide what to do about this repo being stale — reconcile the live OneDrive generation in as the new
   baseline, or retire the repo as a historical checkpoint.
5. Six duplicate full-tree copies (`about/`, `whitelabel/`, `atlas/`, `agreeease/`,
   `corporate-booking-tool/`, `advisory-implementation/`) are untracked junk from an earlier copy
   operation. Deleting them needs Crystal's approval; do not commit them.

### Learnings

**Problem.** Work out which of ~150 local HTML files serves a live site, then realign a sibling portal to
that site's design language.

**Approach.** Hash the live bytes against every local candidate before reading a single file — identity
first, similarity second. When nothing matched, extract the live page's *link graph* rather than its
content: filenames the live homepage referenced (`*_crystal-denzel-edit.html`, `glink`, `addn`) existed
nowhere in the repo or its git history, which located the real source in one Spotlight query. For the
design language, treat the live page's own inline `<style>` block as authority and the extraction tool as
a corroborating witness.

**Judgment calls — what was NOT done, and why.**
- Did not trust `designlang`'s token report, and did not discard it either. Used it for screenshots,
  scale measurement and structure; overrode it on foreground colour and voice where the source disagreed.
- Did not probe live pages by status code. nginx's catch-all returns 200 for everything, so
  `whitelabel.html` and `api-access.html` both looked real at 164,654 bytes — the homepage.
- Did not generate the raster brand boards with a fallback model or a stock stand-in. A board with an
  invented wordmark would have been worse than no board and would have propagated into the redesign.
- Did not accept either subagent's self-report. Direction B's accent check was a false pass on method —
  it grepped the literal hex, missing `var(--accent)`. The conclusion happened to hold; the method
  would not have caught a violation.
- Did not fix the losing variant's cosmetic defects. Polish before selection is work thrown away.

**Reusable rule.** For "which file is live", compare bytes and follow the live page's own link graph —
never filenames, mtimes, or HTTP status codes. For "match this design", the target's own stylesheet
outranks any extraction tool, and the tool's job is screenshots and measurement.
