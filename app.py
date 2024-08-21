from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true" #For tracing via LangChain
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Prompt Template
prompt = ChatPromptTemplate.from_messages({
    ("system","You are a helpful assistant. Please response to the usre quaries"),
    ("user","Question:{question}")
})

# Defining Streamlit Framework
st.title("Langchain Demo with Google Gemini")
input_text = st.text_input("Search the topic you want")

# Gemini LLM
llm = ChatGoogleGenerativeAI(model='gemini-1.5-flash')
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))