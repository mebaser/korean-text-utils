# korean-text-utils 문서

이 디렉터리는 `korean-text-utils`의 상세 문서를 정리하는 공간입니다.

## 모듈

- 한글 자모 처리: `src/korean_text_utils/hangul.py`
- 로마자 변환: `src/korean_text_utils/romanize.py`
- 텍스트 정규화: `src/korean_text_utils/normalize.py`
- 문장 유틸리티: `src/korean_text_utils/utils.py`

## 한글 자모 처리

`hangul.py`는 완성형 한글 음절뿐 아니라 호환 자모와 현대 자모까지 판별할 수 있습니다.

- `contains_hangul("hello 한글!") -> True`
- `extract_hangul("ABC 한글 123 ㄱㄴ!") -> "한글ㄱㄴ"`
- `extract_hangul("ABC 한글 123 ㄱㄴ!", include_jamo=False) -> "한글"`
- `extract_initials("한글 테스트") -> "ㅎㄱㅌㅅㅌ"`
- `has_batchim("강") -> True`

## 문장 유틸리티

`split_sentences()`는 문장 끝 문장부호를 보존하면서 한국어 문장을 나눕니다.
`text_length()`는 기본적으로 공백을 제외한 유니코드 문자 수를 반환하고, `include_spaces=True`를 주면 연속 공백을 하나로 정규화한 뒤 공백까지 셉니다.

## 로마자 변환 범위

`romanize()`는 Revised Romanization의 기본 자모 표를 사용하고, 인접한 한글 음절 사이의 대표 발음 변화 일부를 반영합니다.

- 비음화: `백마 -> baengma`
- 유음화/ㄹ 인접 변화: `신라 -> silla`, `종로 -> jongno`
- 구개음화: `같이 -> gachi`
- ㅎ 관련 거센소리: `좋고 -> joko`

인명, 행정구역 단위, 붙임표 사용, 단어별 예외 사전은 아직 별도 정책으로 다루지 않습니다.
