"""Hangul syllable decomposition and composition helpers."""

from __future__ import annotations

from collections.abc import Iterable

HANGUL_BASE = 0xAC00
HANGUL_END = 0xD7A3
JUNGSEONG_COUNT = 21
JONGSEONG_COUNT = 28
SYLLABLE_BLOCK_SIZE = JUNGSEONG_COUNT * JONGSEONG_COUNT

CHOSEONG = [
    "ㄱ",
    "ㄲ",
    "ㄴ",
    "ㄷ",
    "ㄸ",
    "ㄹ",
    "ㅁ",
    "ㅂ",
    "ㅃ",
    "ㅅ",
    "ㅆ",
    "ㅇ",
    "ㅈ",
    "ㅉ",
    "ㅊ",
    "ㅋ",
    "ㅌ",
    "ㅍ",
    "ㅎ",
]

JUNGSEONG = [
    "ㅏ",
    "ㅐ",
    "ㅑ",
    "ㅒ",
    "ㅓ",
    "ㅔ",
    "ㅕ",
    "ㅖ",
    "ㅗ",
    "ㅘ",
    "ㅙ",
    "ㅚ",
    "ㅛ",
    "ㅜ",
    "ㅝ",
    "ㅞ",
    "ㅟ",
    "ㅠ",
    "ㅡ",
    "ㅢ",
    "ㅣ",
]

JONGSEONG = [
    "",
    "ㄱ",
    "ㄲ",
    "ㄳ",
    "ㄴ",
    "ㄵ",
    "ㄶ",
    "ㄷ",
    "ㄹ",
    "ㄺ",
    "ㄻ",
    "ㄼ",
    "ㄽ",
    "ㄾ",
    "ㄿ",
    "ㅀ",
    "ㅁ",
    "ㅂ",
    "ㅄ",
    "ㅅ",
    "ㅆ",
    "ㅇ",
    "ㅈ",
    "ㅊ",
    "ㅋ",
    "ㅌ",
    "ㅍ",
    "ㅎ",
]

CHOSEONG_INDEX = {jamo: index for index, jamo in enumerate(CHOSEONG)}
JUNGSEONG_INDEX = {jamo: index for index, jamo in enumerate(JUNGSEONG)}
JONGSEONG_INDEX = {jamo: index for index, jamo in enumerate(JONGSEONG) if jamo}


def is_hangul_syllable(char: str) -> bool:
    """Return True when char is one precomposed Hangul syllable."""

    return len(char) == 1 and HANGUL_BASE <= ord(char) <= HANGUL_END


def decompose(text: str) -> list[str]:
    """Split Hangul syllables into compatibility jamo.

    Non-Hangul characters are preserved as-is.
    """

    result: list[str] = []

    for char in text:
        if not is_hangul_syllable(char):
            result.append(char)
            continue

        offset = ord(char) - HANGUL_BASE
        choseong_index = offset // SYLLABLE_BLOCK_SIZE
        jungseong_index = (offset % SYLLABLE_BLOCK_SIZE) // JONGSEONG_COUNT
        jongseong_index = offset % JONGSEONG_COUNT

        result.append(CHOSEONG[choseong_index])
        result.append(JUNGSEONG[jungseong_index])
        if jongseong_index:
            result.append(JONGSEONG[jongseong_index])

    return result


def compose(jamo: Iterable[str] | str) -> str:
    """Combine compatibility jamo into precomposed Hangul syllables.

    Characters that cannot form a syllable are preserved.
    """

    chars = list(jamo)
    result: list[str] = []
    index = 0

    while index < len(chars):
        current = chars[index]

        if (
            current not in CHOSEONG_INDEX
            or index + 1 >= len(chars)
            or chars[index + 1] not in JUNGSEONG_INDEX
        ):
            result.append(current)
            index += 1
            continue

        choseong_index = CHOSEONG_INDEX[current]
        jungseong_index = JUNGSEONG_INDEX[chars[index + 1]]
        jongseong_index = 0
        consumed = 2

        possible_jongseong_index = index + 2
        if possible_jongseong_index < len(chars):
            possible_jongseong = chars[possible_jongseong_index]
            next_char_index = possible_jongseong_index + 1
            followed_by_vowel = (
                next_char_index < len(chars)
                and chars[next_char_index] in JUNGSEONG_INDEX
            )

            if possible_jongseong in JONGSEONG_INDEX and not followed_by_vowel:
                jongseong_index = JONGSEONG_INDEX[possible_jongseong]
                consumed = 3

        codepoint = (
            HANGUL_BASE
            + (choseong_index * SYLLABLE_BLOCK_SIZE)
            + (jungseong_index * JONGSEONG_COUNT)
            + jongseong_index
        )
        result.append(chr(codepoint))
        index += consumed

    return "".join(result)
