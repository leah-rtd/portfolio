import streamlit as st
import requests
from streamlit_timeline import timeline
from streamlit_lottie import st_lottie
import streamlit.components.v1 as components
from llama_index.core import GPTVectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.langchain import LangChainLLM
from constant import *
from PIL import Image
import openai
from langchain_community.chat_models import ChatOpenAI

st.set_page_config(page_title='Leah Rothschild' ,layout="wide",page_icon='👧🏻',
                   initial_sidebar_state = "expanded")

# -----------------  chatbot  ----------------- #
# Set up the OpenAI key
openai_api_key = st.sidebar.text_input('Enter your OpenAI API Key and hit Enter', type="password")
openai.api_key = (openai_api_key)

# load the file
documents = SimpleDirectoryReader(input_files=["extra_material/bio.txt"]).load_data()

pronoun = info["Pronoun"]
name = info["Name"]
def ask_bot(input_text):
    # define LLM
    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        temperature=0,
        openai_api_key=openai.api_key,
    )
    Settings.llm = LangChainLLM(llm=llm)


    # load index
    index = GPTVectorStoreIndex.from_documents(documents, llm=llm)

    # query LlamaIndex and GPT-3.5 for the AI's response
    PROMPT_QUESTION = f"""You are Buddy, an AI assistant dedicated to assisting {name} in her job search by providing recruiters with relevant and concise information.
    If you do not know the answer, politely admit it and let recruiters know how to contact {name} to get more information directly from {pronoun}.
    Keep your answers short and concise.
    Don't put "Buddy" or a breakline in the front of your answer.
    Human: {input}
    """

    output = index.as_query_engine().query(PROMPT_QUESTION.format(input=input_text))
    print(f"output: {output}")
    return output.response

# get the user's input by calling the get_text function
def get_text():
    input_text = st.text_area("After providing OpenAI API Key on the sidebar, you can send your questions and hit Ctrl + Enter to know more about me.", key="input")
    return input_text

st.markdown("Ask my AI agent Buddy some questions about me !")
user_input = get_text()

if user_input:
#   text = st.text_area('Enter your questions')
  if not openai_api_key.startswith('sk-'):
    st.warning('⚠️Please enter your OpenAI API key on the sidebar.', icon='⚠')
  if openai_api_key.startswith('sk-'):
    st.info(ask_bot(user_input))

# -----------------  loading assets  ----------------- #
st.sidebar.markdown('<hr>Click on the image to view my <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" width="20px" style="vertical-align:middle;">', unsafe_allow_html = True)
st.sidebar.markdown(info['Photo'],unsafe_allow_html=True)

@st.cache_resource
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

local_css("style/style.css")

# loading assets
python_lottie = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_2znxgjyt.json")
my_sql_lottie = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_w11f2rwn.json")
git_lottie = load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_03cuemhb.json")
github_lottie = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_6HFXXE.json")
docker_lottie = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_35uv2spq.json")
tensorflow_lottie = load_lottieurl("https://lottie.host/6df2f0b7-30ad-4c26-b6de-724820fd47a1/F43wjHIHZF.json")
google_cloud_platform_lottie = load_lottieurl("https://lottie.host/c4ec4a9f-05f0-4e49-a207-aefd841169b2/39ilxANJIZ.json")
sklearn_lottie = load_lottieurl("https://lottie.host/fa31caed-9262-4e23-b9a1-09ebce377f00/9r4yZZPaMN.json")

# ----------------- info ----------------- #
def gradient(color1, color2, color3, content1, content2):
    st.markdown(f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:60px;border-radius:2%;">'
                f'<span style="color:{color3};">{content1}</span><br>'
                f'<span style="color:white;font-size:17px;">{content2}</span></h1>',
                unsafe_allow_html=True)

with st.container():

    full_name = info['Full_Name']

    gradient("#DED9FA","#7677C4",'e0fbfc',f"Hi, I'm {full_name}👋", info["Intro"])
    st.write("")
    st.write(info['About'])




# ----------------- skillset ----------------- #
with st.container():
    st.subheader('⚒️ Skills')
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        st_lottie(python_lottie, height=70,width=70, key="python", speed=2.5)
    with col2:
        st_lottie(tensorflow_lottie, height=70,width=70, key="tensorflow", speed=4)
    with col3:
        st_lottie(my_sql_lottie,height=70,width=70, key="mysql", speed=2.5)
    with col4:
        st_lottie(git_lottie,height=70,width=70, key="git", speed=2.5)
    with col1:
        st_lottie(github_lottie,height=70,width=70, key="github", speed=2.5)
    with col2:
        st_lottie(docker_lottie,height=70,width=70, key="docker", speed=2.5)
    with col3:
        st_lottie(google_cloud_platform_lottie,height=70,width=70, key="gcp", speed=2.5)
    with col4:
        st_lottie(sklearn_lottie,height=70,width=70, key="js", speed=1)


# ----------------- timeline ----------------- #
with st.container():
    st.markdown("""""")
    st.subheader('📌 Career Snapshot')

    # load data
    with open('extra_material/timeline.json', "r") as f:
        data = f.read()
    # for number of students as of 29/07/2025
    # render timeline
    timeline(data, height=600)

# -----------------  notebooks  -----------------  #

# Teaching Materials Page URL
teaching_material_page_link = "/Teaching_Materials"

# Helper to generate slideshow HTML for a given notebook list and unique ID
def create_slideshow(notebooks, unique_id):
    slides_html = ""
    dots_html = ""

    for idx, notebook in enumerate(notebooks):
        slides_html += f"""
        <div class="mySlides-{unique_id} fade">
            <div style="text-align:left; margin-bottom: 10px;">
                <h4 style="color: #FFFFFF;">{notebook['title']}</h4>
            </div>
            <img src="{notebook['thumbnail']}" style="width:100%; border-radius: 10px;">
        </div>
        """
        dots_html += f'<span class="dot-{unique_id}"></span>\n'

    html_code = f"""
    <div class="slideshow-container">
        {slides_html}
    </div>

    <br>
    <div style="text-align:center">
        {dots_html}
    <br>
    </div>

    <style>
        * {{box-sizing: border-box;}}
        .mySlides-{unique_id} h4 {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-weight: 600;
            margin: 0;
        }}
        img {{vertical-align: middle;}}
        .dot-{unique_id} {{
            height: 14px;
            width: 14px;
            margin: 0 4px;
            background-color: #bbb;
            border-radius: 50%;
            display: inline-block;
            transition: background-color 0.6s ease;
            cursor: pointer;
        }}
        .active-{unique_id} {{background-color: #333;}}
        .fade {{
            animation-name: fade;
            animation-duration: 1s;
        }}
        @keyframes fade {{
            from {{opacity: .4}}
            to {{opacity: 1}}
        }}
    </style>

    <script>
    let slideIndex_{unique_id} = 0;
    showSlides_{unique_id}();

    function showSlides_{unique_id}() {{
        let i;
        let slides = document.getElementsByClassName("mySlides-{unique_id}");
        let dots = document.getElementsByClassName("dot-{unique_id}");
        for (i = 0; i < slides.length; i++) {{
            slides[i].style.display = "none";
        }}
        slideIndex_{unique_id}++;
        if (slideIndex_{unique_id} > slides.length) {{slideIndex_{unique_id} = 1}}
        for (i = 0; i < dots.length; i++) {{
            dots[i].className = dots[i].className.replace(" active-{unique_id}", "");
        }}
        slides[slideIndex_{unique_id}-1].style.display = "block";
        dots[slideIndex_{unique_id}-1].className += " active-{unique_id}";
        setTimeout(showSlides_{unique_id}, 5000);
    }}
    </script>
    """

    return html_code


# Layout: Two Columns
with st.container():
    st.markdown("""""")
    st.subheader('👩‍🏫 Teaching Materials')
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("English Notebooks")
        components.html(create_slideshow(notebooks_gb, "GB"), height=410)
        st.markdown("""""")


    with col2:
        st.markdown("Notebooks en Français")
        components.html(create_slideshow(notebooks_fr, "FR"), height=410)
        st.markdown("""""")






# -----------------  contact  ----------------- #
with st.container():
    st.subheader("📨 Contact Me")
    contact_form = f"""
        <form action="https://formsubmit.co/430d11100db23f61bdfebe1e4ea6e020" method="POST">
            <input type="hidden" name="_captcha value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
    st.markdown(contact_form, unsafe_allow_html=True)
