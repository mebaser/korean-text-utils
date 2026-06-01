from korean_text_utils.utils import split_sentences, text_length


def test_split_sentences_keeps_sentence_punctuation():
    text = "안녕하세요! 반가워요. 잘 지내죠?"

    assert split_sentences(text) == ["안녕하세요!", "반가워요.", "잘 지내죠?"]


def test_split_sentences_handles_trailing_sentence_without_punctuation():
    text = "첫 문장입니다. 마지막 문장입니다"

    assert split_sentences(text) == ["첫 문장입니다.", "마지막 문장입니다"]


def test_split_sentences_normalizes_extra_spaces_inside_sentences():
    text = "안녕하세요!   정말   반가워요."

    assert split_sentences(text) == ["안녕하세요!", "정말 반가워요."]


def test_text_length_counts_visible_characters_without_spaces_by_default():
    assert text_length("안녕 하세요!") == 6


def test_text_length_can_include_spaces_after_normalization():
    assert text_length("안녕   하세요!", include_spaces=True) == 7
