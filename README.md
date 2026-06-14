# korean-text-utils

한글 텍스트를 쉽게 다루기 위한 Python 유틸리티 라이브러리입니다.  
초보자도 쉽게 사용할 수 있도록 간단하고 실용적인 함수들을 제공합니다.

## ✨ 주요 기능

- 한글 자모(초성/중성/종성) 분리 및 조합
- 한글 → 로마자 변환 (Revised Romanization)
- 텍스트 정규화 (띄어쓰기, 특수문자 처리)
- 오타/이모지/반복 문자 정리
- 한국어 문장 분리 및 길이 계산

## 📦 설치 방법

```bash
pip install git+https://github.com/mebaser/korean-text-utils.git
```

개발용으로 설치하려면:

```bash
pip install -e ".[dev]"
```

## 사용 예시

```python
from korean_text_utils.hangul import (
    compose,
    contains_hangul,
    decompose,
    extract_hangul,
    extract_initials,
    has_batchim,
)
from korean_text_utils.romanize import romanize
from korean_text_utils.normalize import clean_text
from korean_text_utils.utils import split_sentences, text_length

# 한글 자모 분리
print(decompose("안녕하세요"))
# 출력: ['ㅇ', 'ㅏ', 'ㄴ', 'ㄴ', 'ㅕ', 'ㅇ', ...]

# 한글 자모 조합
print(compose(["ㅇ", "ㅏ", "ㄴ", "ㄴ", "ㅕ", "ㅇ"]))
# 출력: 안녕

# 한글 포함 여부와 추출
print(contains_hangul("hello 한글!"))
# 출력: True

print(extract_hangul("ABC 한글 123 ㄱㄴ!"))
# 출력: 한글ㄱㄴ

print(extract_initials("한글 테스트"))
# 출력: ㅎㄱㅌㅅㅌ

print(has_batchim("강"))
# 출력: True

# 로마자 변환
print(romanize("안녕하세요"))
# 출력: annyeonghaseyo

# 대표 발음 변화 반영
print(romanize("신라 종로 같이 좋고"))
# 출력: silla jongno gachi joko

# 텍스트 정리
print(clean_text("안녕하세요!!!   ^_^  반가워요~~~~"))
# 출력: 안녕하세요 반가워요

# 문장 분리와 길이 계산
print(split_sentences("안녕하세요! 반가워요. 잘 지내죠?"))
# 출력: ['안녕하세요!', '반가워요.', '잘 지내죠?']

print(text_length("안녕 하세요!"))
# 출력: 6
```

## 상세 문서

- 한글 자모 처리: [`src/korean_text_utils/hangul.py`](./src/korean_text_utils/hangul.py)
- 로마자 변환: [`src/korean_text_utils/romanize.py`](./src/korean_text_utils/romanize.py)
- 텍스트 정규화: [`src/korean_text_utils/normalize.py`](./src/korean_text_utils/normalize.py)
- 문장 유틸리티: [`src/korean_text_utils/utils.py`](./src/korean_text_utils/utils.py)

## 기여 방법

1. Fork 후 Branch 생성
2. 수정 후 Pull Request
3. Issue에 버그나 기능 제안을 남겨 주세요.
