from korean_text_utils.hangul import compose, decompose, is_hangul_syllable


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
