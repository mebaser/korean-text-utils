"""Small shared helpers for korean_text_utils."""

from __future__ import annotations

import re

_WHITESPACE_RE = re.compile(r"\s+")


def normalize_spaces(text: str) -> str:
    """Collapse consecutive whitespace and trim the result."""

    return _WHITESPACE_RE.sub(" ", text).strip()
