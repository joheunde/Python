import streamlit as st

# ChatBot 제목 및 설명 설정
st.title("ChatBot")
st.subheader("사용자와 여러가지 대화를 할 수 있는 챗봇입니다.")
st.write("이 Streamlit 애플리케이션 코드는 OpenAI의 GPT-3.5-turbo 모델을 사용하여 챗봇을 구현하는 방법을 보여줍니다. 이 챗봇은 사용자가 입력한 메시지에 대해 응답을 생성하고, 대화 내용을 화면에 표시하며, 사용자가 대화를 초기화할 수 있는 기능을 제공합니다. 다음은 이 코드의 작동 방식과 주요 기능에 대한 요약입니다.")

# 버튼 토글 상태를 세션 상태로 관리
if 'show_summary_chatbot' not in st.session_state:
    st.session_state.show_summary_chatbot = False

# 버튼 클릭 이벤트 처리
if st.button("요약 내용 보기/숨기기", key="chatbot_summary_button"):
    st.session_state.show_summary_chatbot = not st.session_state.show_summary_chatbot

# 토글 상태에 따라 요약 내용 표시
if st.session_state.show_summary_chatbot:
    st.markdown("""
    ### 작동 방식 요약

    **애플리케이션 설정**:
    - `st.markdown`을 사용하여 애플리케이션의 스타일과 디자인을 설정합니다. 이에는 배경색, 버튼 스타일, 텍스트 입력 필드의 스타일 등이 포함됩니다.
    - 애플리케이션 제목과 환영 메시지를 설정합니다.

    **OpenAI API 키 설정**:
    - `st.secrets`를 통해 OpenAI API 키를 보안 유지하며 설정합니다.

    **모델 및 세션 상태 초기화**:
    - 세션 상태에 'openai_model'이 없으면 기본 모델로 'gpt-3.5-turbo'를 설정합니다.
    - 채팅 기록을 저장할 세션 상태 'messages'를 초기화합니다.

    **대화 내용을 스크롤 가능한 컨테이너에 표시**:
    - 대화 내용이 많아질 경우 스크롤할 수 있도록 컨테이너를 설정합니다.
    - 이전 채팅 기록을 화면에 표시합니다.

    **사용자 입력 처리**:
    - 사용자로부터 입력을 받아 챗봇에게 메시지를 보냅니다.
    - 사용자가 입력한 메시지를 화면에 표시하고, 세션 상태에 저장합니다.

    **어시스턴트의 응답 생성**:
    - OpenAI ChatCompletion API를 사용하여 어시스턴트의 응답을 생성합니다.
    - 스트리밍 모드로 응답을 받아 실시간으로 표시합니다.
    - 어시스턴트의 응답을 세션 상태에 저장합니다.

    **오류 처리**:
    - 할당량 초과 오류나 기타 OpenAI 오류가 발생할 경우 적절한 오류 메시지를 표시합니다.

    **대화 초기화**:
    - 사용자가 대화 내용을 초기화할 수 있는 버튼을 제공합니다.
    - 버튼을 클릭하면 세션 상태의 메시지 리스트를 비우고 애플리케이션을 새로고침합니다.

    ### 요약
    이 애플리케이션은 OpenAI의 GPT-3.5-turbo 모델을 사용하여 실시간 대화형 챗봇을 구현합니다. 사용자가 입력한 메시지에 대해 챗봇이 응답을 생성하고, 대화 내용을 화면에 표시하며, 사용자가 대화 내용을 초기화할 수 있는 기능을 제공합니다. 또한, 오류 발생 시 적절한 오류 메시지를 표시하여 사용자에게 알립니다. 이 애플리케이션은 사용자 친화적인 인터페이스를 제공하여 누구나 쉽게 사용할 수 있도록 설계되었습니다.
    """)

# 구분선 추가
st.markdown("---")

# 이미지 분류 애플리케이션 제목 및 설명 설정
st.title("이미지 분류 애플리케이션")
st.subheader("이미지를 업로드하면 해당 이미지의 분류 결과를 보여드립니다.")
st.write("이 Streamlit 애플리케이션 코드는 TensorFlow의 EfficientNetB0 모델을 사용하여 이미지를 분류하는 방법을 보여줍니다. 사용자가 이미지를 업로드하면 모델이 이미지를 분석하고 분류 결과를 화면에 표시합니다. 다음은 이 코드의 작동 방식과 주요 기능에 대한 요약입니다.")

# 버튼 토글 상태를 세션 상태로 관리
if 'show_summary_image_classifier' not in st.session_state:
    st.session_state.show_summary_image_classifier = False

# 버튼 클릭 이벤트 처리
if st.button("요약 내용 보기/숨기기", key="image_classifier_summary_button"):
    st.session_state.show_summary_image_classifier = not st.session_state.show_summary_image_classifier

# 토글 상태에 따라 요약 내용 표시
if st.session_state.show_summary_image_classifier:
    st.markdown("""
    ### 코드 작동 방식 요약

    **ngrok 인증 토큰 설정**:
    - ngrok을 사용하여 로컬 애플리케이션을 인터넷에서 접근 가능하게 설정합니다.

    **EfficientNetB0 모델 로드**:
    - TensorFlow의 EfficientNetB0 모델을 ImageNet 사전 학습된 가중치를 사용하여 로드합니다.

    **Streamlit 애플리케이션 설정**:
    - `st.set_page_config`를 사용하여 애플리케이션의 페이지 제목, 아이콘 및 레이아웃을 설정합니다.
    - `st.title`과 `st.subheader`를 사용하여 애플리케이션의 주요 제목과 부제목을 설정합니다.

    **파일 업로더 생성**:
    - `st.file_uploader`를 사용하여 사용자가 이미지를 업로드할 수 있도록 합니다.
    - 사용자가 이미지를 업로드하지 않은 경우 `st.info`를 사용하여 메시지를 표시합니다.

    **이미지 열기 및 전처리**:
    - 사용자가 이미지를 업로드하면 `PIL` 라이브러리를 사용하여 이미지를 엽니다.
    - `st.image`를 사용하여 업로드된 이미지를 화면에 표시합니다.
    - 이미지를 224x224 크기로 조정하고 RGB 모드로 변환합니다.
    - 이미지를 배열로 변환하고 `preprocess_input`을 사용하여 전처리합니다.

    **모델을 사용하여 예측 수행**:
    - 전처리된 이미지를 모델에 입력하여 예측을 수행합니다.
    - `decode_predictions`를 사용하여 예측 결과를 인간이 읽을 수 있는 형태로 디코딩합니다.

    **예측 결과 표시**:
    - 예측 결과를 문자열로 포맷팅합니다.
    - `st.success`를 사용하여 예측 결과를 성공 메시지로 화면에 표시합니다.

    ### 요약
    이 애플리케이션은 TensorFlow의 EfficientNetB0 모델을 사용하여 이미지를 분류합니다. 사용자가 이미지를 업로드하면 모델이 이미지를 분석하고 분류 결과를 화면에 표시합니다. 이 애플리케이션은 사용자 친화적인 인터페이스를 제공하여 누구나 쉽게 사용할 수 있도록 설계되었습니다. ngrok을 사용하여 로컬 애플리케이션을 인터넷에서 접근 가능하게 설정할 수 있습니다.
    """)

# 구분선 추가
st.markdown("---")

# PDF 요약 애플리케이션 제목 및 설명 설정
st.title("PDF 요약 애플리케이션")
st.subheader("PDF 파일을 업로드하여 내용을 요약하고 질문을 해보세요.")
st.write("이 Streamlit 애플리케이션 코드는 PDF 파일의 내용을 요약하고 질문에 답변하는 기능을 제공합니다. 다음은 이 코드의 작동 방식과 주요 기능에 대한 요약입니다.")

# 버튼 토글 상태를 세션 상태로 관리
if 'show_summary' not in st.session_state:
    st.session_state.show_summary = False

# 버튼 클릭 이벤트 처리
if st.button("요약 내용 보기/숨기기"):
    st.session_state.show_summary = not st.session_state.show_summary

# 토글 상태에 따라 요약 내용 표시
if st.session_state.show_summary:
    st.markdown("""
    ### 코드 작동 방식 요약

    **환경 변수 로드**:
    - `load_dotenv`를 사용하여 환경 변수를 로드하고, `os.getenv`를 사용하여 OpenAI API 키를 가져옵니다.

    **스트림릿 페이지 설정**:
    - `st.set_page_config`를 사용하여 애플리케이션의 페이지 제목, 아이콘 및 레이아웃을 설정합니다.
    - `st.title`과 `st.subheader`를 사용하여 애플리케이션의 주요 제목과 부제목을 설정합니다.

    **PDF 파일 업로더 생성**:
    - `st.file_uploader`를 사용하여 사용자가 PDF 파일을 업로드할 수 있도록 합니다.
    - 사용자가 파일을 업로드하지 않은 경우 `st.info`를 사용하여 메시지를 표시합니다.

    **PDF에서 텍스트 추출**:
    - `PdfReader`를 사용하여 PDF 파일에서 텍스트를 추출합니다.
    - 각 페이지의 텍스트를 하나의 문자열로 결합합니다.

    **텍스트를 청크로 분할**:
    - `CharacterTextSplitter`를 사용하여 텍스트를 일정 크기의 청크로 분할합니다.
    - `chunk_size`와 `chunk_overlap` 파라미터를 사용하여 청크의 크기와 중첩을 설정합니다.

    **임베딩 생성**:
    - `OpenAIEmbeddings`를 사용하여 텍스트 청크의 임베딩을 생성합니다.
    - `FAISS`를 사용하여 임베딩을 기반으로 지식 베이스를 생성합니다.

    **한국어 요약을 위한 프롬프트 정의**:
    - `PromptTemplate`을 사용하여 한국어 요약을 위한 프롬프트를 정의합니다.
    - 사용자 정의 프롬프트로 요약 체인을 생성합니다.

    **전체 문서 요약 생성**:
    - `load_summarize_chain`을 사용하여 요약 체인을 생성하고, `map_reduce` 체인 타입을 사용하여 요약을 수행합니다.
    - 요약 결과를 화면에 표시합니다.

    **질문 응답 체인**:
    - `load_qa_chain`을 사용하여 질문 응답 체인을 생성합니다.
    - 사용자가 입력한 질문에 대해 응답을 생성하고, 응답 결과를 화면에 표시합니다.

    ### 요약
    이 애플리케이션은 OpenAI의 GPT-3 모델과 LangChain 라이브러리를 사용하여 PDF 파일의 내용을 요약하고 질문에 답변하는 기능을 제공합니다. 사용자가 PDF 파일을 업로드하면, 애플리케이션은 파일에서 텍스트를 추출하고, 텍스트를 청크로 분할한 후 임베딩을 생성합니다. 그런 다음 요약 체인을 사용하여 전체 문서를 요약하고, 질문 응답 체인을 사용하여 사용자의 질문에 대한 답변을 생성합니다. 이 애플리케이션은 사용자 친화적인 인터페이스를 제공하여 누구나 쉽게 사용할 수 있도록 설계되었습니다.
    """)

# 구분선 추가
st.markdown("---")
