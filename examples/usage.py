from pathlib import Path
import sys

# Allow running this file directly from a fresh clone.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from korean_text_utils.hangul import compose, decompose
from korean_text_utils.normalize import clean_text
from korean_text_utils.romanize import romanize
from korean_text_utils.utils import split_sentences, text_length


def main() -> None:
    print(decompose("안녕하세요"))
    print(compose(["ㅇ", "ㅏ", "ㄴ", "ㄴ", "ㅕ", "ㅇ"]))
    print(romanize("안녕하세요"))
    print(clean_text("안녕하세요!!!   ^_^  반가워요~~~~"))
    print(split_sentences("안녕하세요! 반가워요. 잘 지내죠?"))
    print(text_length("안녕 하세요!"))


if __name__ == "__main__":
    main()
