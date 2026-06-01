"""Small shared helpers for korean_text_utils."""

from __future__ import annotations

import re

_WHITESPACE_RE = re.compile(r"\s+")
_SENTENCE_RE = re.compile(r"[^.!?。！？]+(?:[.!?。！？]+|$)")


def normalize_spaces(text: str) -> str:
    """Collapse consecutive whitespace and trim the result."""

    return _WHITESPACE_RE.sub(" ", text).strip()


def split_sentences(text: str) -> list[str]:
    """Split text into sentences while keeping sentence-ending punctuation."""

    sentences: list[str] = []

    for match in _SENTENCE_RE.finditer(text):
        sentence = normalize_spaces(match.group())
        if sentence:
            sentences.append(sentence)

    return sentences


def text_length(text: str, *, include_spaces: bool = False) -> int:
    """Return the Unicode character length of text.

    Spaces are excluded by default so Korean copy length is easier to estimate.
    When include_spaces is true, consecutive whitespace counts as one space.
    """

    normalized = normalize_spaces(text)
    if include_spaces:
        return len(normalized)

    return sum(1 for char in normalized if not char.isspace())
