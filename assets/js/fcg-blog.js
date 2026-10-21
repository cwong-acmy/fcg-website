// Blog index topic filter (shareable via ?topic=) and the not-yet-connected subscribe form.
document.addEventListener('DOMContentLoaded', function () {
    const tags = document.querySelectorAll('.blog-tag');
    const posts = document.querySelectorAll('.blog .post');
    const count = document.getElementById('blogCount');
    const empty = document.getElementById('blogEmpty');

    function apply(tag) {
        let shown = 0;
        tags.forEach(function (b) { b.setAttribute('aria-pressed', String(b.dataset.tag === tag)); });
        posts.forEach(function (p) {
            const hit = tag === 'all' || p.dataset.tags.split(' ').includes(tag);
            p.hidden = !hit;
            if (hit) shown++;
        });
        if (count) count.textContent = 'Showing ' + shown + (shown === 1 ? ' post' : ' posts');
        if (empty) empty.hidden = shown > 0;
    }

    if (tags.length) {
        const valid = Array.from(tags, function (b) { return b.dataset.tag; });
        const fromUrl = new URLSearchParams(location.search).get('topic');
        apply(valid.includes(fromUrl) ? fromUrl : 'all');
        tags.forEach(function (btn) {
            btn.addEventListener('click', function () {
                const tag = btn.dataset.tag;
                apply(tag);
                const url = new URL(location.href);
                if (tag === 'all') url.searchParams.delete('topic'); else url.searchParams.set('topic', tag);
                history.replaceState(null, '', url);
            });
        });
    }

    // ponytail: no email provider is chosen yet, so the form says so instead of faking success. Wire the provider here.
    document.querySelectorAll('.blog-sub').forEach(function (form) {
        form.addEventListener('submit', function (e) {
            e.preventDefault();
            const status = form.querySelector('.blog-sub-status');
            if (status) status.textContent = 'Subscriptions open when the blog launches. Your email was not saved.';
        });
    });
});
