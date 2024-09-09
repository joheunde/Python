import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.chains.summarize import load_summarize_chain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.schema import Document
from dotenv import load_dotenv
import os

# 환경 변수 로드
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

# 스트림릿 페이지 설정
st.set_page_config(page_title="PDF 요약기", page_icon="🖼️", layout="centered")

# 스트림릿 앱 제목 및 설명 설정
st.title("PDF 요약 애플리케이션")
st.subheader("PDF 파일을 업로드하여 내용을 요약하고 질문을 해보세요.")

# PDF 파일 업로더 생성
file = st.file_uploader("PDF 파일을 업로드 해주세요.", type=["pdf"])

if file is None:
    st.info("계속하려면 PDF 파일을 업로드 해주세요.")
else:
    # PDF에서 텍스트 추출
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    # 텍스트를 청크로 분할
    text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1500, chunk_overlap=300, length_function=len)
    chunks = text_splitter.split_text(text)

    # 텍스트 청크를 문서 객체로 래핑
    documents = [Document(page_content=chunk) for chunk in chunks]

    # 임베딩 생성
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    knowledge_base = FAISS.from_documents(documents, embeddings)

    # 한국어 요약을 위한 프롬프트 정의
    summarization_prompt = PromptTemplate(
        input_variables=["text"],
        template="다음 텍스트를 한국어로 완전히 요약해 주세요:\n\n{text}\n"
    )

    # 사용자 정의 프롬프트로 요약 체인 생성
    summarize_chain = load_summarize_chain(
        OpenAI(api_key=openai_api_key, max_tokens=1500),  # 필요 시 max_tokens 증가
        chain_type="map_reduce",
        verbose=True,
        map_prompt=summarization_prompt,
        combine_prompt=summarization_prompt
    )

    # 전체 문서 요약 생성
    with st.spinner('PDF 요약 생성 중...'):
        summary = summarize_chain.run(documents)
        st.write("요약:")
        st.write(summary)

    # 질문 응답 체인
    qa_chain = load_qa_chain(OpenAI(api_key=openai_api_key), chain_type="stuff")

    # 사용자 질문 입력 받기
    user_question = st.text_input("PDF 내용에 대해 질문하세요:")
    if user_question:
        with st.spinner('처리 중...'):
            response = qa_chain.run(input_documents=documents, question=f"{user_question} (대답을 한국어로 해주세요)")
            st.write(response)
