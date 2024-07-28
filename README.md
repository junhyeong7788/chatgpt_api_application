# ChatGPT_API_Application

> ChatGPT, Bard, googletrans, papagotrans, deepltrans API사용하여 Streamlit Web 페이지 개발 및 배포 프로젝트

# ch01, ch02

chatGPT API를 사용하여 '피자만드는 방법'과 '문장 번역', '프롬프트 답변지정', '프롬프트 어텐션' 등을 테스트

# ch03 Streamlit basic

### Streamlit

: 개발자들이 쉽게 대화형 웹 어플리케이션을 만들 수 있는 python 오픈소스 라이브러리  
특징 : 코드에 어떤 변화가 있으면 전체 코드 다시 실행, 즉 이전에 입력한 데이터가 초기화됨

```
pip 설치 : pip install streamlit
파이썬 파일 실행 : streamlit run 01_test.py
```

### ch03_01_test.py

title, header, subheader, text, caption, sample code box, markdown

### ch03_02_data.py

pandas, dataframe, table, metric

### ch03_03_chart.py

line, bar, histogram(matplotlib), plotly

### ch03_04_inputWidget.py

button, text_input, box_input, password_input, download_button, radio_button, selectbox, multiselect

### ch03_05_layout.py

layout, colunms, sidebar, tab

# ch04 : ChatGPT API 사용 요약 프로그램

### streamlit cloud 배포를 위해 실행되는데 필요한 라이브러리 파일 생성 코드

`pip freeze > requirements.txt`

# ch05 : ChatGPT API 사용 광고 문구 생성프로그램

제품명, 제품특징, 필수포함키워드, 브랜드명, 톤앤매너, 브랜드핵심가치를 토대로 광고문구생성 웹페이지

# ch06

### 01_bard_api_test.py

bard api 사용하여 간단한 질의응답 테스트 (bard api 불안정)

### 02_session_state.py

streamlit 특징 해결 : 코드가 재실행되면 이전에 입력한 데이터가 사라지는 것을 seesion_state로 데이터 저장

### 03_chatGPTvsBard.py

ChatGPT vs Bard 응답 비교 웹 프로그램

# ch07 번역기 비교 웹 프로그램

### 01_googletrans.py

구글번역기 라이브러리 테스트

### 02_papagotrans.py

네이버 파파고번역기 API 테스트

### 03_deepltrans.py

deepl번역기 API 테스트

### 04_trans_app.py

ChatGPT, 파파고번역기, 구글 번역기, deepl번역기 비교 웹 프로그램

# ch08 dalle2 사용 이미지 생성, 인스타그램 사진 업로드

### 01_dalle2.py

dalle_2모델을 사용하여 적절한 프롬프트 입력 시 이미지 url 생성 -> 이미지 생성

### 02_insta.py

pathlib과 instagrapi, PIL 라이브러리를 사용하여 인스타그램 게시글 업로드

# information

### 아나콘다 base 자동활성화 끄기

conda config --set auto_activate_base false

### 파이썬 가상환경 (window)

python -m venv 가상환경이름  
가상환경이름₩Scripts₩activate.bat (bat을 붙이는 이유 : 파일 2개일수도 있음)

### 파이썬 가상환경 ( macOS )

가상환경 만들기 : python3 -m venv ./{your venv name}  
가상환경 활성화 : source {your venv name}/bin/activate  
가상환경 비활성화 : deactivate

### 파이썬 가상환경 사용이유

- 가상환경은 프로젝트 별로 패키지를 관리하기 위함
- 프로젝트별로 안정적인 패키지 버전 관리 가능

# error

### 1. git pull error

_git pull origin master error_  
fatal: couldn't find remote ref master  
fatal: Need to specify how to reconcile divergent branches.  
-> 해결 종류 (3중 택1)

1. git config pull.rebase true : rebase 후 pull
2. git config pull.rebase false : revase 없이 pull
3. git config pull.ff only : fast-forward일때만 pull 허용

- rebase : 새 브랜치가 시작된 분기점 커밋을 기준 브랜치의 가장 최근커밋으로 변경하는 작업
- rebase는 git history가 깔끔해질 수 있지만, 부주의하게 사용할 경우 별도의 알림없이 git history를 영구적으로 변경할 수 있기 때문에 ff-only방식을 추천

### 2. googletrans _AttributeError: 'NoneType' object has no attribute 'group'_ 에러

: 버전 변경  
`pip install googletrans==5` : googletrans 버전 리스트 뽑아줌  
`pip install googletrans==3.1.0a0` : 3.1.0a0 버전 재설치

### 3. googletrans _AttributeError: module 'httpcore' has no attribute 'SyncHTTPTransport'_ 싱크해결

: client.py 파일 수정 , 55번줄 SyncHTTPTransport 객체를 AsyncHTTPProxy로 대체, httpx 호환성문제
