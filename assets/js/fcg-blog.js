// Blog index topic filter (shareable via ?topic=), the newsletter box and the book-a-demo form.
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

    // Forms post to /api/* (Vercel functions in api/). Success is shown only after the server saved the row.
    function post(path, data) {
        return fetch(path, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data), signal: AbortSignal.timeout(15000) })
            .then(function (r) { return r.json().catch(function () { return {}; }).then(function (b) { return { ok: r.ok, status: r.status, error: b.error }; }); })
            .catch(function () { return { ok: false }; });
    }
    // Same event names as accomy.com (src/lib/analytics.ts). posthog only exists on the live domain.
    function track(event, props) {
        if (window.posthog) window.posthog.capture(event, props);
    }
    function say(el, text, isError) {
        el.textContent = text;
        el.classList.toggle('is-error', !!isError);
    }
    const FALLBACK = 'We could not send this. Please try again or email hello@fusionconnectgroup.com.';

    document.querySelectorAll('.blog-sub').forEach(function (form) {
        form.addEventListener('submit', function (e) {
            e.preventDefault();
            const status = form.querySelector('.blog-sub-status');
            const input = form.querySelector('input[type=email]');
            if (!input.checkValidity()) { say(status, 'Enter a valid work email.', true); input.focus(); return; }
            const btn = form.querySelector('button[type=submit]');
            btn.disabled = true;
            post('/api/subscribe', { email: input.value, source: 'blog_newsletter', website: (form.querySelector('[name=website]') || {}).value || '' })
                .then(function (r) {
                    btn.disabled = false;
                    if (r.ok) { say(status, 'Thanks, you are subscribed.'); form.reset(); track('newsletter_subscribed', { locale: 'en', source: 'blog' }); }
                    else { say(status, r.error || FALLBACK, true); track('lead_submit_failed', { form: 'newsletter', status: r.status }); }
                });
        });
    });

    const demo = document.getElementById('demoForm');
    if (demo) {
        const product = new URLSearchParams(location.search).get('product');
        const select = demo.querySelector('[name=product]');
        if (product && select.querySelector('option[value="' + CSS.escape(product) + '"]')) select.value = product;
        demo.addEventListener('submit', function (e) {
            e.preventDefault();
            const status = demo.querySelector('.demo-status');
            let firstBad = null;
            demo.querySelectorAll('input, select, textarea').forEach(function (el) {
                if (el.name === 'website') return;
                const bad = !el.checkValidity();
                el.setAttribute('aria-invalid', String(bad));
                if (bad && !firstBad) firstBad = el;
            });
            if (firstBad) { say(status, 'Please fill in the highlighted fields.', true); firstBad.focus(); return; }
            const data = Object.fromEntries(new FormData(demo));
            data.page = location.pathname + location.search;
            const btn = demo.querySelector('button[type=submit]');
            btn.disabled = true;
            say(status, 'Sending…');
            post('/api/book-demo', data).then(function (r) {
                btn.disabled = false;
                if (!r.ok) { say(status, r.error || FALLBACK, true); track('lead_submit_failed', { form: 'book_demo', status: r.status }); return; }
                track('lead_submitted', { form: 'book_demo', product: data.product });
                demo.hidden = true;
                const done = document.getElementById('demoDone');
                done.hidden = false;
                done.focus();
            });
        });
    }
});
