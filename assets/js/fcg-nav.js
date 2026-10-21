// Shared nav behaviour, loaded by partials/nav.html on every page.
(function () {
    // Mobile menu
    const btn = document.querySelector('.fcg-menu-btn');
    const menu = document.getElementById('fcgMobileMenu');
    if (btn && menu) {
        const setOpen = function (open) {
            btn.setAttribute('aria-expanded', String(open));
            btn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
            const icon = btn.querySelector('iconify-icon');
            if (icon) icon.setAttribute('icon', open ? 'solar:close-circle-linear' : 'solar:hamburger-menu-linear');
            menu.hidden = !open;
            document.documentElement.classList.toggle('fcg-menu-open', open);
        };
        btn.addEventListener('click', function () { setOpen(menu.hidden); });
        menu.addEventListener('click', function (e) { if (e.target.closest('a')) setOpen(false); });
        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape' && !menu.hidden) { setOpen(false); btn.focus(); }
        });
        window.matchMedia('(min-width: 768px)').addEventListener('change', function (e) { if (e.matches) setOpen(false); });
    }

    // Mark the current page in both navs
    const here = location.pathname.split('/').pop() || 'index.html';
    const section = location.pathname.includes('/blog/') ? 'blog.html' : here;
    document.querySelectorAll('.fcg-nav-shell a, .fcg-mobile-menu a').forEach(function (a) {
        if (a.getAttribute('href').split('/').pop() === section) a.setAttribute('aria-current', 'page');
    });

    // Theme toggle. ponytail: older pages also bind their own inline copy; both set the same state, so it's harmless.
    const toggle = document.getElementById('themeToggle');
    if (toggle) {
        toggle.checked = document.documentElement.getAttribute('data-theme') === 'dark';
        toggle.addEventListener('change', function () {
            const theme = toggle.checked ? 'dark' : 'light';
            try { localStorage.setItem('theme', theme); } catch (e) {}
            document.documentElement.setAttribute('data-theme', theme);
            document.documentElement.classList.toggle('dark', theme === 'dark');
        });
    }
})();
