import openai
import streamlit as st

# 애플리케이션 제목 설정
st.markdown("""
    <style>
        body {
            background-color: #f0f0f5;
        }
        .main {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .stButton>button {
            color: white;
            background-color: #4CAF50;
            padding: 10px 24px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .stTextInput>div>div>input {
            background-color: #ffffff;
            border-radius: 4px;
            border: 1px solid #ccc;
            padding: 10px;
        }
        .stFileUploader label, .stTextArea label, .stTextInput label {
            color: #333333;
        }
        .stMarkdown p {
            color: #333333;
        }
        .stAlert p {
            color: #333333;
        }
        .title {
            color: #333333;
            font-size: 2.5em;
            font-weight: bold;
            text-align: center;
            margin-bottom: 20px;
        }
        .chat-container {
            max-height: 400px;
            overflow-y: auto;
            padding: 10px;
            background-color: #ffffff;
            border: 1px solid #ddd;
            border-radius: 4px;
            margin-bottom: 10px;
        }
    </style>
    <div style="text-align: center;">
        <h1 class="title">🤖 챗봇 허브에 오신 것을 환영합니다</h1>
    </div>
    <h2 style="text-align: center; color: #333333;">대화형 AI의 미래를 경험해보세요</h2>
    <p style="text-align: center; color: #666666;">
        AI 기반 챗봇과 상호작용하세요. 무엇이든 물어보시면 즉각적인 답변을 드립니다.
    </p>
    <hr style="margin: 20px 0;">
    """, unsafe_allow_html=True)

# OpenAI API 키 설정 (st.secrets를 통해 보안 유지)
openai.api_key = st.secrets["OPENAI_API_KEY"]

# 세션 상태에 'openai_model'이 없으면 기본 모델로 'gpt-3.5-turbo'를 설정
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# 채팅 기록을 저장할 세션 상태 'messages' 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []

# 대화 내용을 스크롤 가능한 컨테이너에 표시
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for message in st.session_state.messages:
    with st.chat_message(message["role"]): # 메시지 역할(user 또는 assistant)에 따라 채팅 메시지 표시
        st.markdown(message["content"]) # 메시지 내용을 마크다운 형식으로 표시
st.markdown('</div>', unsafe_allow_html=True)

# 사용자 입력 받기
prompt = st.chat_input("챗봇에게 메시지 보내기")
if prompt: # 사용자가 메시지를 입력하고 전송 버튼을 클릭했을 때
    # 사용자가 입력한 메시지를 화면에 표시
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # 사용자가 입력한 메시지를 세션 상태 'messages' 리스트에 추가
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 어시스턴트의 응답을 생성하고 표시
    with st.chat_message("assistant"):
        message_placeholder = st.empty() # 실시간으로 메시지를 업데이트하기 위한 플레이스홀더
        full_response = "" # 전체 응답 메시지를 저장할 변수
        try:
            # OpenAI ChatCompletion API를 호출하여 응답 생성 (스트리밍 모드)
            for response in openai.ChatCompletion.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": m["role"], "content": m["content"]} # 세션 상태에 저장된 모든 메시지를 전달
                    for m in st.session_state.messages
                ],
                stream=True, # 스트리밍 모드 활성화
            ):
                full_response += response.choices[0].delta.get("content", "") # 응답 조각을 계속 추가
                message_placeholder.markdown(full_response + " ") # 현재까지의 응답을 표시
            message_placeholder.markdown(full_response) # 최종 응답 표시
            # 어시스턴트의 최종 응답을 세션 상태 'messages' 리스트에 추가
            st.session_state.messages.append({"role": "assistant", "content": full_response})
        except openai.error.RateLimitError:
            # 할당량 초과 오류 처리
            error_message = "할당량을 초과했습니다. 나중에 다시 시도해주세요."
            message_placeholder.markdown(f"<p style='color: #333333;'>{error_message}</p>", unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": error_message})
        except openai.error.OpenAIError as e:
            # 기타 OpenAI 오류 처리
            error_message = f"오류가 발생했습니다: {str(e)}"
            message_placeholder.markdown(f"<p style='color: #333333;'>{error_message}</p>", unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": error_message})

# 대화 내용을 초기화하는 버튼
if st.button("대화 초기화"):
    st.session_state.messages = [] # 세션 상태 'messages' 리스트를 비움
    st.experimental_rerun() # 앱을 새로고침하여 변경 사항 반영
