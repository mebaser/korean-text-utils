from korean_text_utils.normalize import clean_text, collapse_repeated_chars


def test_clean_text_removes_symbols_and_collapses_whitespace():
    assert clean_text("안녕하세요!!!   ^_^  반가워요~~~~") == "안녕하세요 반가워요"


def test_clean_text_can_keep_emoji_when_requested():
    assert clean_text("좋아요 😊!!!", keep_emoji=True) == "좋아요 😊"


def test_collapse_repeated_chars_limits_repeated_characters():
    assert collapse_repeated_chars("ㅋㅋㅋㅋ 안녕~~~~", max_repeat=2) == "ㅋㅋ 안녕~~"
