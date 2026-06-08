/* FCG nuitee-templates — shared behavior: theme toggle + scroll reveals.
   The pre-paint theme read lives inline in each file's <head> to avoid flash. */
(function () {
    // ---- theme toggle ----
    function applyTheme(theme) {
        document.documentElement.setAttribute("data-theme", theme);
        document.documentElement.classList.toggle("dark", theme === "dark");
        try { localStorage.setItem("theme", theme); } catch (e) {}
        var label = document.querySelector("[data-theme-label]");
        if (label) label.textContent = theme === "dark" ? "Light" : "Dark";
    }
    function currentTheme() {
        return document.documentElement.getAttribute("data-theme") === "light" ? "light" : "dark";
    }
    var toggle = document.querySelector("[data-theme-toggle]");
    if (toggle) {
        var label = document.querySelector("[data-theme-label]");
        if (label) label.textContent = currentTheme() === "dark" ? "Light" : "Dark";
        toggle.addEventListener("click", function () {
            applyTheme(currentTheme() === "dark" ? "light" : "dark");
        });
    }

    // ---- feature tabs (chip rail → viewport) ----
    document.querySelectorAll("[data-tabs]").forEach(function (group) {
        var tabs = group.querySelectorAll("[data-tab]");
        var panels = group.querySelectorAll("[data-panel]");
        tabs.forEach(function (tab) {
            tab.addEventListener("click", function () {
                var key = tab.getAttribute("data-tab");
                tabs.forEach(function (t) { t.classList.toggle("is-active", t === tab); });
                panels.forEach(function (p) { p.classList.toggle("is-active", p.getAttribute("data-panel") === key); });
            });
        });
    });

    // ---- scroll reveal ----
    var revealables = document.querySelectorAll(".reveal");
    if (!("IntersectionObserver" in window) || !revealables.length) {
        revealables.forEach(function (el) { el.classList.add("is-visible"); });
        return;
    }
    var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
            if (entry.isIntersecting) {
                entry.target.classList.add("is-visible");
                io.unobserve(entry.target);
            }
        });
    }, { threshold: 0.12, rootMargin: "0px 0px -8% 0px" });
    revealables.forEach(function (el) { io.observe(el); });
})();
