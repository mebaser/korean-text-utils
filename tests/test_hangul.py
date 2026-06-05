from korean_text_utils.hangul import (
    compose,
    contains_hangul,
    decompose,
    extract_hangul,
    is_hangul_char,
    is_hangul_jamo,
    is_hangul_syllable,
)


def test_decompose_splits_hangul_syllables_into_jamo():
    assert decompose("안녕") == ["ㅇ", "ㅏ", "ㄴ", "ㄴ", "ㅕ", "ㅇ"]


def test_decompose_preserves_non_hangul_characters():
    assert decompose("A한!") == ["A", "ㅎ", "ㅏ", "ㄴ", "!"]


def test_compose_combines_jamo_into_hangul_syllables():
    assert compose(["ㅇ", "ㅏ", "ㄴ", "ㄴ", "ㅕ", "ㅇ"]) == "안녕"


def test_compose_accepts_plain_string_input():
    assert compose("ㅎㅏㄴㄱㅡㄹ") == "한글"


def test_compose_preserves_unmatched_characters():
    assert compose(["A", "ㅎ", "ㅏ", "ㄴ", "!"]) == "A한!"


def test_is_hangul_syllable_only_matches_precomposed_korean_syllables():
    assert is_hangul_syllable("한") is True
    assert is_hangul_syllable("ㅎ") is False
    assert is_hangul_syllable("A") is False


def test_is_hangul_jamo_matches_compatibility_and_modern_jamo():
    assert is_hangul_jamo("ㅎ") is True
    assert is_hangul_jamo("ᄒ") is True
    assert is_hangul_jamo("한") is False
    assert is_hangul_jamo("A") is False


def test_is_hangul_char_matches_syllables_and_jamo():
    assert is_hangul_char("한") is True
    assert is_hangul_char("ㅎ") is True
    assert is_hangul_char("ᄒ") is True
    assert is_hangul_char("A") is False


def test_contains_hangul_detects_hangul_anywhere_in_text():
    assert contains_hangul("hello 한글!") is True
    assert contains_hangul("123 ㄱㄴ") is True
    assert contains_hangul("hello!") is False


def test_extract_hangul_keeps_only_hangul_characters():
    assert extract_hangul("ABC 한글 123 ㄱㄴ!") == "한글ㄱㄴ"


def test_extract_hangul_can_exclude_jamo():
    assert extract_hangul("ABC 한글 123 ㄱㄴ!", include_jamo=False) == "한글"
