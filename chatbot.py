# 🧠 Simple Q & A Bot 🤖

import streamlit as st
from langchain_openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

# Function to load OpenAI and get response 💬
def get_openai_response(question):
    llm = OpenAI(
        openai_api_key=os.environ["OPENAI_API_KEY"], 
        model_name="gpt-3.5-turbo-instruct",
        temperature=0.5
    )
    response = llm(question)
    return response

# Initialize our Streamlit app 🏁
st.set_page_config(page_title="🧠 Simple Q & A Bot 🤖")

# Custom CSS for styling
st.markdown(
    """
    <style>
    h1 {
        color: #ff4b4b;
        text-align: center;
    }
    h3 {
        color: #4bff62;
    }
    .stTextInput>div>div>input {
        font-size: 20px;
        height: 50px;
        width: 100%;
        padding: 10px;
        border-radius: 8px; /* Rounded corners for the input box */
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 10px auto;
        cursor: pointer;
        border-radius: 4px;
        display: block;
    }
    .stButton>button:hover {
        background-color: white; 
        color: black; 
        border: 2px solid #4CAF50;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1>Langchain Application 🏁</h1>", unsafe_allow_html=True)

input_text = st.text_input("", placeholder="Enter Your Question Here 🤔", key="input")

if st.button("Submit ✅"):
    response = get_openai_response(input_text)
    st.markdown("<h3>The Response is 📝</h3>", unsafe_allow_html=True)
    st.write(response)
