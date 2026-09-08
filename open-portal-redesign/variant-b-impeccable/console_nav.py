# -*- coding: utf-8 -*-
"""Console sidebar tables — imported by build-console.py and console_content.py.

Mirrors the real sidebar captured on 8 September 2026: same groups, same order,
same labels. (group, [(key, label, icon, href)])
"""

DEV_NAV = [
    ("Start", [
        ("getting-started", "Getting Started", "solar:flag-2-linear", "getting-started.html"),
        ("home", "Home", "solar:home-smile-angle-linear", "../index.html"),
    ]),
    ("Integration &amp; debugging", [
        ("apps", "App Management", "solar:widget-5-linear", "app-management.html"),
        ("sandbox", "Sandbox Environment", "solar:test-tube-linear", "sandbox.html"),
        ("trace", "Request Trace", "solar:routing-2-linear", "trace.html"),
    ]),
    ("Business resources", [
        ("console", "Console", "solar:chart-2-linear", "index.html"),
        ("coverage", "Coverage Map", "solar:map-point-linear", "coverage.html"),
        ("mapping", "Hotel Mapping", "solar:link-round-angle-linear", "hotel-mapping.html"),
        ("horders", "Hotel Orders", "solar:bed-linear", "hotel-orders.html"),
        ("forders", "Flight Orders", "solar:plane-linear", "flight-orders.html"),
    ]),
    ("Developer", [
        ("tmc", "Build My TMC", "solar:buildings-3-linear", "tmc-builder.html"),
        ("docs", "API Docs", "solar:document-text-linear", "../api-docs-hotel.html"),
        ("sdk", "SDK", "solar:code-square-linear", "sdk.html"),
        ("skills", "Skills", "solar:magic-stick-3-linear", "skills.html"),
    ]),
    ("Support", [
        ("ai", "AI Assistant", "solar:chat-round-dots-linear", "ai-assistant.html"),
        ("tickets", "My Tickets", "solar:ticket-linear", "tickets.html"),
    ]),
]

ADMIN_NAV = [
    ("Overview", [
        ("dashboard", "Dashboard", "solar:chart-2-linear", "admin-dashboard.html"),
    ]),
    ("Review &amp; service", [
        ("users", "User List", "solar:users-group-rounded-linear", "admin-user-list.html"),
        ("review", "App Review", "solar:clipboard-check-linear", "admin-app-review.html"),
        ("atickets", "Ticket List", "solar:ticket-linear", "admin-ticket-list.html"),
    ]),
    ("Platform operations", [
        ("atrace", "Request Trace", "solar:routing-2-linear", "admin-trace.html"),
        ("asdk", "SDK Management", "solar:box-linear", "admin-sdk-management.html"),
        ("adocs", "Docs Management", "solar:documents-linear", "admin-docs-management.html"),
    ]),
]
