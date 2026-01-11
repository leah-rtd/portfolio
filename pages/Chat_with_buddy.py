import openai
from utils import ask_bot as _ask_bot
import streamlit as st
from constant import *

# -----------------  page config  ----------------- #

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

local_css("style/style.css")


# -----------------  sidebar  ----------------- #

openai_api_key = st.sidebar.text_input('Enter your OpenAI API Key and hit Enter', type="password")
openai.api_key = (openai_api_key)
st.sidebar.markdown('<hr>Click on the image to view my <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" width="20px" style="vertical-align:middle;">', unsafe_allow_html = True)
st.sidebar.markdown(info['Photo'],unsafe_allow_html=True)

# -----------------  chatbot  ----------------- #
# get the user's input by calling the get_text function
def get_text():
    input_text = st.text_area("After providing OpenAI API Key on the sidebar, you can send your questions and hit Ctrl + Enter to know more about me.", key="input")
    return input_text

def ask_bot(user_input):
    return _ask_bot(user_input)

with st.container():
    st.markdown("""
                Ask my AI agent Buddy some questions about me !\n
                For example, ask it about my background, my values and my hobbies.""")

    user_input = get_text()

    if user_input:
    #   text = st.text_area('Enter your questions')
        if not openai_api_key.startswith('sk-'):
            st.warning('⚠️Please enter your OpenAI API key on the sidebar.', icon='⚠')
        if openai_api_key.startswith('sk-'):
            st.info(ask_bot(user_input))
