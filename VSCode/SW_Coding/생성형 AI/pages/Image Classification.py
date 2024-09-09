import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
from pyngrok import ngrok
from tensorflow.keras.applications.efficientnet import EfficientNetB0, preprocess_input, decode_predictions

# ngrok 인증 토큰 설정
ngrok.set_auth_token("NGROK_API_KEY")

# EfficientNetB0 모델 로드 (ImageNet 사전 학습된 가중치 사용)
efficientnet_model = EfficientNetB0(weights="imagenet", input_shape=(224, 224, 3))

# 스트림릿 애플리케이션 설정
st.set_page_config(page_title="이미지 분류기", page_icon="🖼️", layout="centered")

# 스트림릿 애플리케이션 제목 설정
st.title("이미지 분류 애플리케이션")
st.subheader("이미지를 업로드하면 해당 이미지의 분류 결과를 보여드립니다.")

# 파일 업로더 생성 (사용자가 이미지를 업로드하도록 함)
file = st.file_uploader("이미지를 업로드 해주세요.", type=["jpg", "png"])

if file is None:
    # 파일이 업로드되지 않은 경우 메시지 표시
    st.info("이미지를 먼저 올려주세요.")
else:
    # 파일이 업로드된 경우 이미지 열기
    image = Image.open(file)
    st.image(image, use_column_width=True)  # 업로드된 이미지 표시
    
    # 이미지를 224x224 크기로 변경하고 RGB 모드로 변환
    img_resized = ImageOps.fit(image, (224, 224), Image.LANCZOS)
    img_resized = img_resized.convert("RGB")
    
    # 이미지를 배열로 변환하고 전처리
    img_array = np.asarray(img_resized)
    img_array = preprocess_input(img_array)

    # 모델을 사용하여 예측 수행
    pred = efficientnet_model.predict(img_array.reshape([1, 224, 224, 3]))
    
    # 예측 결과를 디코딩하여 인간이 읽을 수 있는 형태로 변환
    decoded_pred = decode_predictions(pred, top=5)
    
    # 예측 결과를 문자열로 포맷팅
    results = ''
    for i, instance in enumerate(decoded_pred[0]):
        results += "{}위: {} ({:.2f}%)\n".format(i+1, instance[1], instance[2] * 100)
    
    # 예측 결과를 성공 메시지로 표시
    st.success("예측 결과:\n" + results)
