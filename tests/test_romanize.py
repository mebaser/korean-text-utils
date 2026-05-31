from korean_text_utils.romanize import romanize


def test_romanize_uses_revised_romanization_for_common_syllables():
    assert romanize("안녕하세요") == "annyeonghaseyo"


def test_romanize_preserves_spacing_and_ascii_text():
    assert romanize("한글 text") == "hangeul text"


def test_romanize_handles_final_consonants():
    assert romanize("밥") == "bap"
    assert romanize("꽃") == "kkot"
