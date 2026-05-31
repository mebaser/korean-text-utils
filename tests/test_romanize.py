from korean_text_utils.romanize import romanize


def test_romanize_uses_revised_romanization_for_common_syllables():
    assert romanize("안녕하세요") == "annyeonghaseyo"


def test_romanize_preserves_spacing_and_ascii_text():
    assert romanize("한글 text") == "hangeul text"


def test_romanize_handles_final_consonants():
    assert romanize("밥") == "bap"
    assert romanize("꽃") == "kkot"


def test_romanize_applies_common_consonant_assimilation():
    assert romanize("백마") == "baengma"
    assert romanize("종로") == "jongno"
    assert romanize("신라") == "silla"


def test_romanize_applies_palatalization_before_i_vowels():
    assert romanize("같이") == "gachi"
    assert romanize("해돋이") == "haedoji"


def test_romanize_applies_aspiration_with_hieut():
    assert romanize("좋고") == "joko"
    assert romanize("놓다") == "nota"
    assert romanize("낳지") == "nachi"
