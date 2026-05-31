"""Utilities for working with Korean text."""

from korean_text_utils.hangul import compose, decompose, is_hangul_syllable
from korean_text_utils.normalize import clean_text, collapse_repeated_chars
from korean_text_utils.romanize import romanize

__all__ = [
    "clean_text",
    "collapse_repeated_chars",
    "compose",
    "decompose",
    "is_hangul_syllable",
    "romanize",
]

__version__ = "0.1.0"
