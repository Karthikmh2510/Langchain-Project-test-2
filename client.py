import requests
import streamlit as st

def get_gimini_response(input_text):
    response = requests.post("http://localhost:8001/essay/invoke",
                             json={'input':{'topic':input_text}})
    return response.json()['output']['content']

def get_ollama_response(input_text):
    response = requests.post("http://localhost:8001/poem/invoke",
                             json={'input':{'topic':input_text}})
    return response.json()['output']

#Streamlit Framework
st.title("Langchain Demo with Google Gimini and Llama2")
input_text1 = st.text_input("Write an essay on..")
input_text2 = st.text_input("Write an poem on..")

if input_text1:
    st.write(get_gimini_response(input_text1))

if input_text2:
    st.write(get_ollama_response(input_text2))