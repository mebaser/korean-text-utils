"""Text normalization helpers for Korean strings."""

from __future__ import annotations

import re
import unicodedata

_WHITESPACE_RE = re.compile(r"\s+")


def collapse_repeated_chars(text: str, max_repeat: int = 2) -> str:
    """Limit consecutive repeated characters to max_repeat."""

    if max_repeat < 1:
        raise ValueError("max_repeat must be at least 1")

    result: list[str] = []
    previous = ""
    count = 0

    for char in text:
        if char == previous:
            count += 1
        else:
            previous = char
            count = 1

        if count <= max_repeat:
            result.append(char)

    return "".join(result)


def clean_text(
    text: str,
    *,
    keep_emoji: bool = False,
    max_repeat: int = 2,
) -> str:
    """Remove noisy symbols, limit repeated characters, and normalize spaces."""

    collapsed = collapse_repeated_chars(text, max_repeat=max_repeat)
    filtered = "".join(
        char for char in collapsed if _is_allowed_char(char, keep_emoji=keep_emoji)
    )
    return _WHITESPACE_RE.sub(" ", filtered).strip()


def _is_allowed_char(char: str, *, keep_emoji: bool) -> bool:
    if char.isspace():
        return True

    category = unicodedata.category(char)
    if category[0] in {"L", "N"}:
        return True

    return keep_emoji and _is_emoji(char)


def _is_emoji(char: str) -> bool:
    codepoint = ord(char)
    return (
        0x1F000 <= codepoint <= 0x1FAFF
        or 0x2600 <= codepoint <= 0x27BF
    )
