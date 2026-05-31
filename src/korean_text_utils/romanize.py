"""Simple Revised Romanization helpers for Hangul text."""

from __future__ import annotations

from korean_text_utils.hangul import (
    CHOSEONG,
    HANGUL_BASE,
    JONGSEONG,
    JONGSEONG_COUNT,
    JUNGSEONG,
    SYLLABLE_BLOCK_SIZE,
    is_hangul_syllable,
)

INITIAL_ROMANIZATION = {
    "ㄱ": "g",
    "ㄲ": "kk",
    "ㄴ": "n",
    "ㄷ": "d",
    "ㄸ": "tt",
    "ㄹ": "r",
    "ㅁ": "m",
    "ㅂ": "b",
    "ㅃ": "pp",
    "ㅅ": "s",
    "ㅆ": "ss",
    "ㅇ": "",
    "ㅈ": "j",
    "ㅉ": "jj",
    "ㅊ": "ch",
    "ㅋ": "k",
    "ㅌ": "t",
    "ㅍ": "p",
    "ㅎ": "h",
}

VOWEL_ROMANIZATION = {
    "ㅏ": "a",
    "ㅐ": "ae",
    "ㅑ": "ya",
    "ㅒ": "yae",
    "ㅓ": "eo",
    "ㅔ": "e",
    "ㅕ": "yeo",
    "ㅖ": "ye",
    "ㅗ": "o",
    "ㅘ": "wa",
    "ㅙ": "wae",
    "ㅚ": "oe",
    "ㅛ": "yo",
    "ㅜ": "u",
    "ㅝ": "wo",
    "ㅞ": "we",
    "ㅟ": "wi",
    "ㅠ": "yu",
    "ㅡ": "eu",
    "ㅢ": "ui",
    "ㅣ": "i",
}

FINAL_ROMANIZATION = {
    "": "",
    "ㄱ": "k",
    "ㄲ": "k",
    "ㄳ": "k",
    "ㄴ": "n",
    "ㄵ": "n",
    "ㄶ": "n",
    "ㄷ": "t",
    "ㄹ": "l",
    "ㄺ": "k",
    "ㄻ": "m",
    "ㄼ": "l",
    "ㄽ": "l",
    "ㄾ": "l",
    "ㄿ": "p",
    "ㅀ": "l",
    "ㅁ": "m",
    "ㅂ": "p",
    "ㅄ": "p",
    "ㅅ": "t",
    "ㅆ": "t",
    "ㅇ": "ng",
    "ㅈ": "t",
    "ㅊ": "t",
    "ㅋ": "k",
    "ㅌ": "t",
    "ㅍ": "p",
    "ㅎ": "t",
}


def romanize(text: str) -> str:
    """Romanize Hangul text with a practical Revised Romanization mapping.

    This function uses syllable-level mappings and does not apply every
    pronunciation assimilation rule.
    """

    result: list[str] = []

    for char in text:
        if not is_hangul_syllable(char):
            result.append(char)
            continue

        choseong, jungseong, jongseong = _split_syllable(char)
        result.append(INITIAL_ROMANIZATION[choseong])
        result.append(VOWEL_ROMANIZATION[jungseong])
        result.append(FINAL_ROMANIZATION[jongseong])

    return "".join(result)


def _split_syllable(char: str) -> tuple[str, str, str]:
    offset = ord(char) - HANGUL_BASE
    choseong_index = offset // SYLLABLE_BLOCK_SIZE
    jungseong_index = (offset % SYLLABLE_BLOCK_SIZE) // JONGSEONG_COUNT
    jongseong_index = offset % JONGSEONG_COUNT

    return (
        CHOSEONG[choseong_index],
        JUNGSEONG[jungseong_index],
        JONGSEONG[jongseong_index],
    )
