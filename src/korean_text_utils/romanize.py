"""Simple Revised Romanization helpers for Hangul text."""

from __future__ import annotations

from dataclasses import dataclass

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

IOTIZED_VOWELS = {"ㅣ", "ㅑ", "ㅕ", "ㅛ", "ㅠ", "ㅖ", "ㅒ"}
VELAR_FINALS = {"ㄱ", "ㄲ", "ㅋ", "ㄳ", "ㄺ"}
DENTAL_FINALS = {"ㄷ", "ㅅ", "ㅆ", "ㅈ", "ㅊ", "ㅌ", "ㅎ"}
BILABIAL_FINALS = {"ㅂ", "ㅍ", "ㄼ", "ㄿ", "ㅄ"}
PALATAL_INITIAL_BY_FINAL = {
    "ㄷ": "ㅈ",
    "ㅌ": "ㅊ",
}
ASPIRATED_INITIAL_BY_INITIAL = {
    "ㄱ": "ㅋ",
    "ㄷ": "ㅌ",
    "ㅂ": "ㅍ",
    "ㅈ": "ㅊ",
}
ASPIRATED_INITIAL_BY_FINAL = {
    "ㄱ": "ㅋ",
    "ㄲ": "ㅋ",
    "ㅋ": "ㅋ",
    "ㄳ": "ㅋ",
    "ㄺ": "ㅋ",
    "ㄷ": "ㅌ",
    "ㅅ": "ㅌ",
    "ㅆ": "ㅌ",
    "ㅈ": "ㅊ",
    "ㅊ": "ㅊ",
    "ㅌ": "ㅌ",
    "ㅂ": "ㅍ",
    "ㅍ": "ㅍ",
    "ㄼ": "ㅍ",
    "ㄿ": "ㅍ",
    "ㅄ": "ㅍ",
}
FINAL_WITH_HIEUT = {
    "ㅎ": "",
    "ㄶ": "ㄴ",
    "ㅀ": "ㄹ",
}


@dataclass
class SyllableParts:
    initial: str
    vowel: str
    final: str


def romanize(text: str) -> str:
    """Romanize Hangul text with a practical Revised Romanization mapping.

    Common pronunciation changes between adjacent Hangul syllables are reflected,
    but name, address, and lexical exception rules are intentionally out of scope.
    """

    units: list[SyllableParts | str] = [
        _split_syllable(char) if is_hangul_syllable(char) else char
        for char in text
    ]
    _apply_pronunciation_rules(units)

    result: list[str] = []
    previous_syllable: SyllableParts | None = None

    for unit in units:
        if isinstance(unit, str):
            result.append(unit)
            previous_syllable = None
            continue

        result.append(_romanize_syllable(unit, previous_syllable))
        previous_syllable = unit

    return "".join(result)


def _apply_pronunciation_rules(units: list[SyllableParts | str]) -> None:
    for index, current in enumerate(units[:-1]):
        next_unit = units[index + 1]
        if isinstance(current, str) or isinstance(next_unit, str):
            continue

        _apply_aspiration(current, next_unit)
        _apply_palatalization(current, next_unit)
        _apply_liquid_assimilation(current, next_unit)
        _apply_nasal_assimilation(current, next_unit)


def _apply_aspiration(current: SyllableParts, next_unit: SyllableParts) -> None:
    if (
        current.final in FINAL_WITH_HIEUT
        and next_unit.initial in ASPIRATED_INITIAL_BY_INITIAL
    ):
        current.final = FINAL_WITH_HIEUT[current.final]
        next_unit.initial = ASPIRATED_INITIAL_BY_INITIAL[next_unit.initial]
        return

    if next_unit.initial == "ㅎ" and current.final in ASPIRATED_INITIAL_BY_FINAL:
        next_unit.initial = ASPIRATED_INITIAL_BY_FINAL[current.final]
        current.final = ""


def _apply_palatalization(current: SyllableParts, next_unit: SyllableParts) -> None:
    if (
        current.final in PALATAL_INITIAL_BY_FINAL
        and next_unit.initial == "ㅇ"
        and next_unit.vowel in IOTIZED_VOWELS
    ):
        next_unit.initial = PALATAL_INITIAL_BY_FINAL[current.final]
        current.final = ""


def _apply_liquid_assimilation(current: SyllableParts, next_unit: SyllableParts) -> None:
    if current.final == "ㄴ" and next_unit.initial == "ㄹ":
        current.final = "ㄹ"
        next_unit.initial = "ㄹ"
    elif current.final == "ㄹ" and next_unit.initial == "ㄴ":
        next_unit.initial = "ㄹ"
    elif current.final == "ㅇ" and next_unit.initial == "ㄹ":
        next_unit.initial = "ㄴ"


def _apply_nasal_assimilation(current: SyllableParts, next_unit: SyllableParts) -> None:
    if next_unit.initial not in {"ㄴ", "ㅁ", "ㄹ"}:
        return

    nasal_final = _nasalized_final(current.final)
    if not nasal_final:
        return

    current.final = nasal_final
    if next_unit.initial == "ㄹ":
        next_unit.initial = "ㄴ"


def _nasalized_final(final: str) -> str:
    if final in VELAR_FINALS:
        return "ㅇ"
    if final in DENTAL_FINALS:
        return "ㄴ"
    if final in BILABIAL_FINALS:
        return "ㅁ"
    return ""


def _romanize_syllable(
    syllable: SyllableParts,
    previous_syllable: SyllableParts | None,
) -> str:
    initial = INITIAL_ROMANIZATION[syllable.initial]
    if (
        previous_syllable is not None
        and previous_syllable.final == "ㄹ"
        and syllable.initial == "ㄹ"
    ):
        initial = "l"

    return (
        initial
        + VOWEL_ROMANIZATION[syllable.vowel]
        + FINAL_ROMANIZATION[syllable.final]
    )


def _split_syllable(char: str) -> SyllableParts:
    offset = ord(char) - HANGUL_BASE
    choseong_index = offset // SYLLABLE_BLOCK_SIZE
    jungseong_index = (offset % SYLLABLE_BLOCK_SIZE) // JONGSEONG_COUNT
    jongseong_index = offset % JONGSEONG_COUNT

    return SyllableParts(
        CHOSEONG[choseong_index],
        JUNGSEONG[jungseong_index],
        JONGSEONG[jongseong_index],
    )
