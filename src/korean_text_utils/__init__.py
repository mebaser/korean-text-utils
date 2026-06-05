"""Utilities for working with Korean text."""

from korean_text_utils.hangul import (
    compose,
    contains_hangul,
    decompose,
    extract_hangul,
    is_hangul_char,
    is_hangul_jamo,
    is_hangul_syllable,
)
from korean_text_utils.normalize import clean_text, collapse_repeated_chars
from korean_text_utils.romanize import romanize
from korean_text_utils.utils import normalize_spaces, split_sentences, text_length

__all__ = [
    "clean_text",
    "collapse_repeated_chars",
    "compose",
    "contains_hangul",
    "decompose",
    "extract_hangul",
    "is_hangul_char",
    "is_hangul_jamo",
    "is_hangul_syllable",
    "normalize_spaces",
    "romanize",
    "split_sentences",
    "text_length",
]

__version__ = "0.1.0"
