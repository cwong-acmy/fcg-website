#!/usr/bin/env python3
"""Build the shared parts of the static FCG site. Stdlib only, idempotent.

    python3 tools/build-site.py          # write
    python3 tools/build-site.py --check  # exit 1 if any page is out of date

1. Copies _shell/nav.html and _shell/footer.html into every page (between SHARED:NAV / SHARED:FOOTER markers).
2. Renders the blog from blog/posts/<slug>.json (one file per post, edited in Pages CMS or by hand):
   index cards, the homepage strip, "Related reading" on product pages, one page per post,
   blog/feed.xml and sitemap.xml.

Edit _shell/*.html and blog/posts/*.json, never the generated regions. The GitHub Action in
.github/workflows/build-site.yml runs this on every push, so a CMS save rebuilds the pages.
"""
import html
import json
import re
import sys
from datetime import datetime, timezone
from email.utils import format_datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://www.fusionconnectgroup.com"  # launch domain for canonical/OG/RSS; the blog ships with the redesign
SKIP = {"components.html", "nav-preview.html"}  # design reference + throwaway nav preview, not live pages
NO_STRIP = {"about.html", "contact.html", "404.html"}  # nav/footer only, no blog strip
WPM = 220  # reading speed for the "N min read" label
DEFAULT_CTA = {"title": "Talk to FCG", "text": "See how FCG connects your team to live travel supply.",
               "href": "contact.html", "label": "Book a demo"}
ICON = '<link rel="icon" href="favicon.svg" type="image/svg+xml">'
# PostHog "FCG Website" project 693521 (org Fusion Connect Group, US cloud); public token, also in 1Password
# LLM Automations "PostHog - FCG Website project token". Empty = no tracking on any page.
POSTHOG_KEY = "phc_zUEdMcAbLzpFBva9aVHXWi2tGesuFFdvCgw6Wd3LGg96"
# Google Tag Manager "FCG" container for www.fusionconnectgroup.com; it loads GA4 G-QM59ND5BC3.
# 1Password LLM Automations "Google Analytics + Tag Manager - FCG Website".
GTM_ID = "GTM-MKFC3SDS"
SEO = json.loads((ROOT / "_shell" / "seo.json").read_text(encoding="utf-8"))
ORG_ID = f"{SITE}/#organization"


def org_ld():
    o = SEO["organization"]
    d = {"@type": "Organization", "@id": ORG_ID, "name": o["name"], "alternateName": o["alternateName"], "url": f"{SITE}/",
         "logo": f"{SITE}/{o['logo']}", "email": o["email"], "description": o["description"]}
    if o["sameAs"]:
        d["sameAs"] = o["sameAs"]
    return d


def seo_head(name, s):
    """<title>, description, canonical, Open Graph and one JSON-LD @graph for a core page, from _shell/seo.json."""
    assert len(s["title"]) <= 60 and len(s["description"]) <= 160, f"{name}: title <= 60 and description <= 160 characters"
    url = f"{SITE}/" if name == "index.html" else f"{SITE}/{name}"
    kind = s["schema"]
    graph = [org_ld()]
    if kind == "WebSite":
        graph.append({"@type": "WebSite", "@id": f"{SITE}/#website", "url": f"{SITE}/", "name": SEO["organization"]["name"],
                      "alternateName": "FCG", "publisher": {"@id": ORG_ID}})
    elif kind in ("SoftwareApplication", "Service"):
        item = {"@type": kind, "name": s["name"], "description": s["description"], "url": url}
        if kind == "Service":
            item["provider"] = {"@id": ORG_ID}
        else:
            item.update(publisher={"@id": ORG_ID}, applicationCategory="BusinessApplication", operatingSystem="Web")
        graph.append(item)
    graph.append({"@type": "AboutPage" if kind == "AboutPage" else "WebPage", "@id": f"{url}#webpage", "url": url, "name": s["title"],
                  "description": s["description"], "isPartOf": {"@id": f"{SITE}/#website"}, "about": {"@id": ORG_ID}})
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False).replace("</", "<\\/")
    img = f"{SITE}/{SEO['og_image']}"
    return "\n".join([
        f"    <title>{esc(s['title'])}</title>",
        f'    <meta name="description" content="{esc(s["description"])}">',
        f'    <link rel="canonical" href="{url}">',
        '    <meta property="og:type" content="website">',
        f'    <meta property="og:site_name" content="{esc(SEO["organization"]["name"])}">',
        f'    <meta property="og:title" content="{esc(s["title"])}">',
        f'    <meta property="og:description" content="{esc(s["description"])}">',
        f'    <meta property="og:url" content="{url}">',
        f'    <meta property="og:image" content="{img}">',
        '    <meta name="twitter:card" content="summary_large_image">',
        f'    <script type="application/ld+json">{ld}</script>',
    ])


def ensure_seo_region(text, name):
    """First run only: replace the page's own <title> with an empty BUILD:SEO region."""
    if "<!-- BUILD:SEO -->" not in text:
        text, n = re.subn(r"[ \t]*<title>.*?</title>\n", "", text, count=1, flags=re.S)
        assert n == 1, f"{name}: no <title> to replace"
        text = text.replace("</head>", "<!-- BUILD:SEO --><!-- /BUILD:SEO -->\n</head>", 1)
    return text
TOPICS = {"product": "Product", "engineering": "Engineering", "ai": "AI", "industry": "Industry", "company": "Company"}
STRIP_BEFORE = [  # first marker found on a page is where the blog strip goes
    "<!-- ===== CLOSING CTA ===== -->",
    "<!-- FOOTER -->",
    "<!-- SHARED:FOOTER -->",
]
# First run only: the hand-built nav and footer get wrapped in SHARED markers.
NAV_RE = re.compile(r"    <nav class=\"marine-header-section.*?</nav>\n", re.S)
FOOTER_RE = re.compile(r"    <footer class=\"site-footer.*?</footer>\n", re.S)

esc = html.escape
read = lambda p: (ROOT / p).read_text(encoding="utf-8")


def region(text, name, content):
    """Replace content between <!-- NAME --> and <!-- /NAME -->."""
    pat = re.compile(rf"(<!-- {name} -->).*?(<!-- /{name} -->)", re.S)
    assert pat.search(text), f"missing <!-- {name} --> region"
    return pat.sub(lambda m: m.group(1) + "\n" + content + "\n" + m.group(2), text, count=1)


def chrome(text, root):
    for name, pat in (("SHARED:NAV", NAV_RE), ("SHARED:FOOTER", FOOTER_RE)):
        if f"<!-- {name} -->" not in text:
            m = pat.search(text)
            assert m, f"page has no {name} markers and no element to wrap"
            text = text[:m.start()] + f"<!-- {name} --><!-- /{name} -->\n" + text[m.end():]
    text = region(text, "SHARED:NAV", read("_shell/nav.html").replace("{{root}}", root).rstrip("\n"))
    return region(text, "SHARED:FOOTER", read("_shell/footer.html").replace("{{root}}", root).rstrip("\n"))


def analytics(text):
    """PostHog + GTM (_shell/analytics.html) at the end of every page's <head>; an empty region until both IDs are set."""
    assert not POSTHOG_KEY or re.fullmatch(r"phc_\w+", POSTHOG_KEY), "POSTHOG_KEY must be a phc_ project token"
    assert not GTM_ID or re.fullmatch(r"GTM-[A-Z0-9]+", GTM_ID), "GTM_ID must look like GTM-XXXX"
    if "<!-- BUILD:ANALYTICS -->" not in text:
        text = text.replace("</head>", "<!-- BUILD:ANALYTICS --><!-- /BUILD:ANALYTICS -->\n</head>", 1)
    snippet = (read("_shell/analytics.html").replace("{{key}}", POSTHOG_KEY).replace("{{gtm}}", GTM_ID).rstrip("\n")
               if POSTHOG_KEY and GTM_ID else "")
    return region(text, "BUILD:ANALYTICS", snippet)


def card(p, root, featured=False, h="h3"):
    contain = " post-media--contain" if p.get("contain") else ""
    cls = "post post--featured" if featured else "post"
    label = "Featured" if featured else ""
    meta = "".join(f"<span>{esc(x)}</span>" for x in (label, date_label(p), f"{p['minutes']} min read") if x)
    initials = "".join(w[0] for w in p["author"].split()[:2]).upper()
    return f"""            <article class="{cls}" data-tags="{esc(' '.join(p['tags']))}">
                <div class="post-media{contain}" style="background-image: url('{root}{esc(p['image'])}');" aria-hidden="true"></div>
                <div class="post-body">
                    <p class="post-meta">{meta}</p>
                    <{h} class="post-title"><a href="{root}blog/{p['slug']}.html">{esc(p['title'])}</a></{h}>
                    <p class="post-excerpt">{esc(p['excerpt'])}</p>
                    <div class="post-foot">
                        <span class="post-author"><span class="post-avatar" aria-hidden="true">{esc(initials)}</span>{esc(p['author'])}</span>
                        <a class="post-chip" href="{root}blog.html?topic={p['topic']}">{TOPICS[p['topic']]}</a>
                    </div>
                </div>
            </article>"""


def date_label(p):
    return p.get("date") or ("Draft" if p.get("draft") else "")


def strip(posts, title, link_text, root=""):
    cards = "\n".join(card(p, root) for p in posts)
    return f"""    <section class="blog-strip" aria-labelledby="blog-strip-heading">
        <div class="blog-wrap">
            <div class="blog-strip-head">
                <h2 class="blog-strip-title" id="blog-strip-heading">{title}</h2>
                <a class="blog-strip-link" href="{root}blog.html">{link_text}</a>
            </div>
            <div class="blog-grid">
{cards}
            </div>
        </div>
    </section>"""


def ensure_region(text, name, css_link):
    """First run only: add the strip region and the blog stylesheet to a page."""
    if f"<!-- {name} -->" not in text:
        marker = next(m for m in STRIP_BEFORE if m in text)
        i = text.index(marker)
        i = text.rfind("\n", 0, i) + 1
        text = text[:i] + f"<!-- {name} --><!-- /{name} -->\n" + text[i:]
    if css_link not in text:
        text = text.replace("</head>", f"    {css_link}\n</head>", 1)
    return text


def related(post, posts, n=3):
    others = [p for p in posts if p is not post]
    same = [p for p in others if set(p["tags"]) & set(post["tags"])]
    return (same + [p for p in others if p not in same])[:n]


def post_page(p, posts, head):
    url = f"{SITE}/blog/{p['slug']}.html"
    ld = {"@context": "https://schema.org", "@type": "BlogPosting", "headline": p["title"], "description": p["excerpt"],
          "url": url, "image": f"{SITE}/{p['image']}", "author": {"@type": "Person" if p["author"] != "FCG Team" else "Organization", "name": p["author"]},
          "publisher": {"@type": "Organization", "@id": ORG_ID, "name": SEO["organization"]["name"], "url": f"{SITE}/"}}
    if p.get("date"):
        ld["datePublished"] = p["date"]
    cta = p["cta"]
    fields = {
        "head_common": head.replace("{{root}}", "../").rstrip("\n"),
        "title": esc(p["title"]), "excerpt": esc(p["excerpt"]), "url": url, "site": SITE,
        "image_url": f"{SITE}/{esc(p['image'])}", "image": esc(p["image"]),
        "robots": '    <meta name="robots" content="noindex">\n' if p.get("draft") else "",
        "jsonld": json.dumps(ld).replace("</", "<\\/"),
        "topic": p["topic"], "topic_label": TOPICS[p["topic"]],
        "initials": esc("".join(w[0] for w in p["author"].split()[:2]).upper()),
        "author": esc(p["author"]), "role": esc(p.get("role", "")),
        "date_label": esc(date_label(p)), "minutes": str(p["minutes"]),
        "contain_class": " post-media--contain" if p.get("contain") else "",
        "draft_note": '            <p class="draft-note" role="note">Draft: this post is placeholder content and is hidden from search engines.</p>\n' if p.get("draft") else "",
        "body": "                " + p["body"],  # trusted, team-authored HTML
        "cta_title": esc(cta["title"]), "cta_text": esc(cta["text"]), "cta_href": esc(cta["href"]), "cta_label": esc(cta["label"]),
        "related": "\n".join(card(r, "../") for r in related(p, posts)),
    }
    out = read("blog/_post.html")
    out = re.sub(r"<!-- Template for .*?-->\n", "<!-- Generated by tools/build-site.py from blog/posts.json and blog/_post.html. Do not edit. -->\n", out, count=1)
    missing = set(re.findall(r"\{\{(\w+)\}\}", out)) - fields.keys()
    assert not missing, f"template placeholders with no value: {missing}"
    out = re.sub(r"\{\{(\w+)\}\}", lambda m: fields[m.group(1)], out)  # one pass, so post text containing {{ }} is left alone
    return chrome(out, "../")


def feed(posts):
    items = []
    for p in posts:
        if p.get("draft"):
            continue  # drafts are noindex; keep them out of feed readers too
        url = f"{SITE}/blog/{p['slug']}.html"
        date = f"<pubDate>{format_datetime(datetime.fromisoformat(p['date']).replace(tzinfo=timezone.utc))}</pubDate>" if p.get("date") else ""
        items.append(f"    <item><title>{esc(p['title'])}</title><link>{url}</link><guid>{url}</guid><description>{esc(p['excerpt'])}</description>{date}</item>")
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0">\n  <channel>\n'
            f"    <title>FCG Blog</title>\n    <link>{SITE}/blog.html</link>\n"
            "    <description>Product updates, engineering deep dives and market views from FCG Group.</description>\n"
            + "".join(i + "\n" for i in items) + "  </channel>\n</rss>\n")


def load_posts():
    """One JSON file per post; the filename is the URL slug. Featured first, then newest first."""
    pages = {f.stem for f in ROOT.glob("*.html")}
    posts = []
    for f in sorted((ROOT / "blog" / "posts").glob("*.json")):
        p = json.loads(f.read_text(encoding="utf-8"))
        p["slug"] = f.stem
        where = f"blog/posts/{f.name}"
        assert re.fullmatch(r"[a-z0-9-]+", p["slug"]), f"{where}: filename must be lowercase letters, numbers and hyphens"
        for k in ("title", "excerpt", "topic", "image", "author", "body"):
            assert str(p.get(k) or "").strip(), f"{where}: '{k}' is empty"
        p.setdefault("tags", [p["topic"]])
        p.setdefault("products", [])
        p.setdefault("role", "")
        p["image"] = p["image"].lstrip("/")  # Pages CMS writes /assets/...; pages prefix their own root
        assert p["topic"] in TOPICS and set(p["tags"]) <= set(TOPICS), f"{where}: unknown topic"
        assert set(p["products"]) <= pages, f"{where}: unknown product page {set(p['products']) - pages}"
        assert re.fullmatch(r"[\w./-]+", p["image"]), f"{where}: image path must be plain (no quotes or spaces): {p['image']}"
        assert (ROOT / p["image"]).is_file(), f"{where}: image not found: {p['image']}"
        if p.get("date"):
            p["date"] = str(p["date"])[:10]
            datetime.fromisoformat(p["date"])
        assert p.get("draft") or p.get("date"), f"{where}: a published post (draft off) needs a date"
        p["cta"] = p.get("cta") if (p.get("cta") or {}).get("href") else DEFAULT_CTA
        words = len(re.sub(r"<[^>]+>", " ", p["body"]).split())
        p["minutes"] = p.get("minutes") or max(1, round(words / WPM))
        posts.append(p)
    assert posts, "no posts in blog/posts/"
    posts.sort(key=lambda p: p["slug"])
    posts.sort(key=lambda p: p.get("date") or "", reverse=True)
    posts.sort(key=lambda p: not p.get("featured"))
    return posts


def sitemap(pages, posts):
    urls = [f"{SITE}/{'' if p == 'index.html' else p}" for p in pages]
    urls += [f"{SITE}/blog/{p['slug']}.html" for p in posts if not p.get("draft")]
    body = "".join(f"  <url><loc>{esc(u)}</loc></url>\n" for u in urls)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{body}</urlset>\n'


SOON = """            <div class="blog-soon">
                <p class="blog-soon-title">Coming soon</p>
                <p>Our first articles are on the way. Subscribe above to get them first.</p>
            </div>"""


def build():
    posts = load_posts()
    # Drafts still get their own (noindex) page for review by direct link, but are never listed.
    # No published post yet: the blog shows "Coming soon" and the home/product strips stay empty.
    public = [p for p in posts if not p.get("draft")]
    head = read("_shell/blog-head.html")
    css = '<link rel="stylesheet" href="assets/css/fcg-blog.css">'
    out = {}

    for page in sorted(ROOT.glob("*.html")):
        if page.name in SKIP:
            continue
        text = chrome(page.read_text(encoding="utf-8"), "")
        if "<!-- BUILD:HEAD -->" in text:
            text = region(text, "BUILD:HEAD", head.replace("{{root}}", "").rstrip("\n"))
        elif ICON not in text:
            text = text.replace("</head>", f"    {ICON}\n</head>", 1)
        if page.name in SEO["pages"]:
            text = region(ensure_seo_region(text, page.name), "BUILD:SEO", seo_head(page.name, SEO["pages"][page.name]))
        if page.name == "blog.html":
            used = [t for t in TOPICS if any(t in p["tags"] for p in public)]
            tags = ['                    <button class="blog-tag" type="button" data-tag="all" aria-pressed="true">All posts</button>'] if public else []
            tags += [f'                    <button class="blog-tag" type="button" data-tag="{t}" aria-pressed="false">{TOPICS[t]}</button>' for t in used]
            text = region(text, "BLOG:TAGS", "\n".join(tags))
            # ponytail: one page of cards; add pagination once there are more than ~24 posts
            if public:
                cards = [card(public[0], "", featured=True, h="h2"), '            <div class="blog-grid">']
                cards += [card(p, "") for p in public[1:]] + ["            </div>"]
            else:
                cards = [SOON]
            text = region(text, "BLOG:CARDS", "\n".join(cards))
        elif page.name == "index.html":
            text = ensure_region(text, "BLOG:LATEST", css)
            text = region(text, "BLOG:LATEST", strip(public[:3], "Latest from the blog", "All posts") if public else "")
        elif page.name not in NO_STRIP:
            slug = page.stem
            mine = [p for p in public if slug in p["products"]]
            picks = (mine + [p for p in public if p not in mine])[:3]  # top up with latest so the row is always full
            text = ensure_region(text, "BLOG:RELATED", css)
            title = "Related reading" if mine else "From the blog"
            text = region(text, "BLOG:RELATED", strip(picks, title, "All posts") if public else "")
        out[page] = analytics(text)

    for p in posts:
        out[ROOT / "blog" / f"{p['slug']}.html"] = analytics(post_page(p, posts if p.get("draft") else public, head))
    out[ROOT / "blog" / "feed.xml"] = feed(posts)
    out[ROOT / "sitemap.xml"] = sitemap(sorted(k.name for k in out if k.parent == ROOT and k.name != "404.html"), posts)

    stale = [k for k, v in out.items() if not k.exists() or k.read_text(encoding="utf-8") != v]
    orphans = [f for f in (ROOT / "blog").glob("*.html") if f.name != "_post.html" and f not in out
               and "Generated by tools/build-site.py" in f.read_text(encoding="utf-8")]  # never touch hand-written files
    if "--check" in sys.argv:
        for k in stale:
            print("out of date:", k.relative_to(ROOT))
        for f in orphans:
            print("orphan (its blog/posts/ file was removed or renamed):", f.relative_to(ROOT))
        return 1 if stale or orphans else 0
    for f in orphans:  # generated pages only, so a post deleted in the CMS takes its page with it
        f.unlink()
        print("removed", f.relative_to(ROOT))
    for k in stale:
        k.write_text(out[k], encoding="utf-8")
        print("wrote", k.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(build())
