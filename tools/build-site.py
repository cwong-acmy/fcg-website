#!/usr/bin/env python3
"""Build the shared parts of the static FCG site. Stdlib only, idempotent.

    python3 tools/build-site.py          # write
    python3 tools/build-site.py --check  # exit 1 if any page is out of date

1. Copies _shell/nav.html and _shell/footer.html into every page (between SHARED:NAV / SHARED:FOOTER markers).
2. Renders the blog from blog/posts.json: index cards, the homepage strip,
   "Related reading" on product pages, one page per post, and blog/feed.xml.

Edit _shell/nav.html, _shell/footer.html, _shell/blog-head.html and blog/posts.json, never the generated regions.
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
          "publisher": {"@type": "Organization", "name": "FCG Group", "url": SITE}}
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


def build():
    data = json.loads(read("blog/posts.json"))
    posts = data["posts"]
    for p in posts:
        assert p["topic"] in TOPICS and set(p["tags"]) <= set(TOPICS), f"unknown topic in {p['slug']}"
        assert re.fullmatch(r"[a-z0-9-]+", p["slug"]), f"bad slug {p['slug']}"
        assert re.fullmatch(r"[\w./-]+", p["image"]), f"image path must be plain (no quotes or spaces): {p['image']}"
        assert (ROOT / p["image"]).is_file(), f"image not found: {p['image']}"
    head = read("_shell/blog-head.html")
    css = '<link rel="stylesheet" href="assets/css/fcg-blog.css">'
    out = {}

    for page in sorted(ROOT.glob("*.html")):
        if page.name in SKIP:
            continue
        text = chrome(page.read_text(encoding="utf-8"), "")
        if page.name == "blog.html":
            text = region(text, "BUILD:HEAD", head.replace("{{root}}", "").rstrip("\n"))
            used = [t for t in TOPICS if any(t in p["tags"] for p in posts)]
            tags = ['                    <button class="blog-tag" type="button" data-tag="all" aria-pressed="true">All posts</button>']
            tags += [f'                    <button class="blog-tag" type="button" data-tag="{t}" aria-pressed="false">{TOPICS[t]}</button>' for t in used]
            text = region(text, "BLOG:TAGS", "\n".join(tags))
            # ponytail: one page of cards; add pagination once there are more than ~24 posts
            cards = [card(posts[0], "", featured=True, h="h2"), '            <div class="blog-grid">']
            cards += [card(p, "") for p in posts[1:]] + ["            </div>"]
            text = region(text, "BLOG:CARDS", "\n".join(cards))
        elif page.name == "index.html":
            text = ensure_region(text, "BLOG:LATEST", css)
            text = region(text, "BLOG:LATEST", strip(posts[:3], "Latest from the blog", "All posts"))
        elif page.name != "about.html":
            slug = page.stem
            mine = [p for p in posts if slug in p["products"]]
            picks = (mine + [p for p in posts if p not in mine])[:3]  # top up with latest so the row is always full
            text = ensure_region(text, "BLOG:RELATED", css)
            title = "Related reading" if mine else "From the blog"
            text = region(text, "BLOG:RELATED", strip(picks, title, "All posts"))
        out[page] = text

    for p in posts:
        out[ROOT / "blog" / f"{p['slug']}.html"] = post_page(p, posts, head)
    out[ROOT / "blog" / "feed.xml"] = feed(posts)

    stale = [k for k, v in out.items() if not k.exists() or k.read_text(encoding="utf-8") != v]
    orphans = [f for f in (ROOT / "blog").glob("*.html") if f.name != "_post.html" and f not in out]
    for f in orphans:
        print("orphan (not in posts.json, delete it if the post was removed or renamed):", f.relative_to(ROOT))
    if "--check" in sys.argv:
        for k in stale:
            print("out of date:", k.relative_to(ROOT))
        return 1 if stale or orphans else 0
    for k in stale:
        k.write_text(out[k], encoding="utf-8")
        print("wrote", k.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(build())
