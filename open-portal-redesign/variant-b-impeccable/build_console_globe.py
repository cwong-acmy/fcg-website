# -*- coding: utf-8 -*-
"""The marketing site's Cobe globe, lifted verbatim so the console plots the
same globe the FCG website does rather than a second implementation."""

from pathlib import Path

_SITE = Path(__file__).parent.parent.parent / "index.html"
_src = _SITE.read_text(encoding="utf-8")
_a = _src.index("var createGlobe=function(){")
_b = _src.index("</script>", _a)
GLOBE_LIB = "<script>\n" + _src[_a:_b].strip() + "\n</script>"
assert "createGlobe" in GLOBE_LIB and len(GLOBE_LIB) > 10000, "globe not found in the marketing index.html"
