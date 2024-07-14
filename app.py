import streamlit as st
import requests

st.title('Fake News Detector')

input_text = st.text_input('Enter news article')

if input_text:
    response = requests.post("http://127.0.0.1:8000/predict", json={"content": input_text})
    prediction = response.json()
    st.write(prediction['prediction'])
