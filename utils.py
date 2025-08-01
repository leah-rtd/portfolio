import requests
from PIL import Image, ImageOps
from llama_index.core import GPTVectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.langchain import LangChainLLM
from llama_index.readers.json import JSONReader

import openai
from langchain_community.chat_models import ChatOpenAI
from constant import info

# Home page util functions


from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings
from llama_index.readers.json import JSONReader
from llama_index.llms.openai import OpenAI
import openai

def ask_bot(input_text):


    # Load primary documents (bio) with high priority metadata
    bio_documents = SimpleDirectoryReader(input_files=["extra_material/bio.txt"]).load_data()
    for doc in bio_documents:
        doc.metadata["document_type"] = "primary_bio"
        doc.metadata["priority"] = "high"
        doc.metadata["source"] = "bio"

    # Load timeline JSON with high priority
    json_reader = JSONReader()
    timeline_documents = json_reader.load_data(
        input_file="extra_material/timeline.json",
        extra_info={"document_type": "timeline", "priority": "medium", "source": "timeline"}
    )


    application_documents = SimpleDirectoryReader(input_dir="extra_material/applications/").load_data()
    for doc in application_documents:
        doc.metadata["document_type"] = "application_letter"
        doc.metadata["priority"] = "medium"
        doc.metadata["source"] = "applications"

    # Combine all documents
    all_docs = bio_documents + timeline_documents + application_documents

    # Setup LLM
    llm = OpenAI(
        model="gpt-3.5-turbo",
        temperature=0.01,
        api_key=openai.api_key,
    )
    Settings.llm = llm

    # Create index
    index = VectorStoreIndex.from_documents(all_docs)

    # Create query engine with custom retriever settings
    query_engine = index.as_query_engine(
        similarity_top_k=10,  # Retrieve more documents to ensure priority docs are included
        response_mode="tree_summarize"  # Better for combining multiple sources
    )

    pronoun = info["Pronoun"]
    name = info["Name"]

    # Enhanced prompt with document prioritization instructions
    PROMPT_QUESTION = f"""You are Buddy, an AI assistant dedicated to assisting {name} in her job search by providing recruiters with relevant and concise information.
    If you do not know the answer, politely admit it and let recruiters know how to contact {name} to get more information directly from {pronoun}.
    Keep your answers short and concise.
    Don't put "Buddy" or a breakline in the front of your answer.
    Human: {input}
    """


    output = query_engine.query(PROMPT_QUESTION.format(input=input_text))
    print(f"output: {output}")
    return output.response

def ask_bot2(input_text):

    pronoun = info["Pronoun"]
    name = info["Name"]
    documents = SimpleDirectoryReader(input_files=["extra_material/bio.txt"]).load_data()
    json_reader = JSONReader()
    documents_json = json_reader.load_data(input_file="extra_material/timeline.json", extra_info={})
    all_docs = documents + documents_json
    # define LLM
    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        temperature=0,
        openai_api_key=openai.api_key,
    )
    Settings.llm = LangChainLLM(llm=llm)


    # load index
    index = GPTVectorStoreIndex.from_documents(all_docs, llm=llm)

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


def return_all_lotties():
    """
    Return all six lotties needed for home.py
    """
    def load_lottieurl(url: str):
        """
        Sub function to get the lotties
        """
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    """Lottie requests"""
    python_lottie = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_2znxgjyt.json")
    my_sql_lottie = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_w11f2rwn.json")
    git_lottie = load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_03cuemhb.json")
    github_lottie = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_6HFXXE.json")
    docker_lottie = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_35uv2spq.json")
    tensorflow_lottie = load_lottieurl("https://lottie.host/6df2f0b7-30ad-4c26-b6de-724820fd47a1/F43wjHIHZF.json")
    google_cloud_platform_lottie = load_lottieurl("https://lottie.host/c4ec4a9f-05f0-4e49-a207-aefd841169b2/39ilxANJIZ.json")
    sklearn_lottie = load_lottieurl("https://lottie.host/fa31caed-9262-4e23-b9a1-09ebce377f00/9r4yZZPaMN.json")

    return [python_lottie, my_sql_lottie, git_lottie, github_lottie, docker_lottie, tensorflow_lottie, google_cloud_platform_lottie, sklearn_lottie]

def create_slideshow(notebooks, unique_id):
    """
    Function to return the html code for the notebook carousel
    """
    slides_html = ""
    dots_html = ""

    for idx, notebook in enumerate(notebooks):
        slides_html += f"""
        <div class="mySlides-{unique_id} fade-{unique_id}">
            <div style="text-align:left; margin-bottom: 10px;">
                <h4 class="slide-title-{unique_id}">{notebook['title']}</h4>
            </div>
            <div class="image-container-{unique_id}">
                <img src="{notebook['thumbnail']}" class="slide-image-{unique_id}">
            </div>
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

        .mySlides-{unique_id} {{
            display: none;
            position: relative;
        }}

        .mySlides-{unique_id}.show-{unique_id} {{
            display: block;
        }}

        .slide-title-{unique_id} {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-weight: 600;
            margin: 0;
            color: #FFFFFF;
            font-size: 18px;
        }}

        .image-container-{unique_id} {{
            width: 100%;
            height: 300px;
            overflow: hidden;
            border-radius: 10px;
            position: relative;
        }}

        .slide-image-{unique_id} {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: top left;
            transition: opacity 0.3s ease;
        }}

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

        .active-{unique_id} {{
            background-color: #333;
        }}

        .fade-{unique_id} {{
            opacity: 0;
            transition: opacity 1s ease-in-out;
        }}

        .fade-{unique_id}.show-{unique_id} {{
            opacity: 1;
        }}

        /* Responsive design */
        @media only screen and (max-width: 768px) {{
            .slide-title-{unique_id} {{
                font-size: 16px;
            }}
            .image-container-{unique_id} {{
                height: 250px;
            }}
        }}

        @media only screen and (max-width: 480px) {{
            .slide-title-{unique_id} {{
                font-size: 14px;
            }}
            .image-container-{unique_id} {{
                height: 200px;
            }}
        }}

        @media only screen and (max-width: 300px) {{
            .slide-title-{unique_id} {{
                font-size: 12px;
            }}
            .image-container-{unique_id} {{
                height: 150px;
            }}
        }}
    </style>

    <script>
    let slideIndex_{unique_id} = 0;
    showSlides_{unique_id}();

    function showSlides_{unique_id}() {{
        let slides = document.getElementsByClassName("mySlides-{unique_id}");
        let dots = document.getElementsByClassName("dot-{unique_id}");

        // Hide all slides and remove active classes
        for (let i = 0; i < slides.length; i++) {{
            slides[i].classList.remove("show-{unique_id}");
            dots[i].classList.remove("active-{unique_id}");
        }}

        slideIndex_{unique_id}++;
        if (slideIndex_{unique_id} > slides.length) {{
            slideIndex_{unique_id} = 1;
        }}

        // Show current slide and activate dot
        if (slides.length > 0) {{
            slides[slideIndex_{unique_id} - 1].classList.add("show-{unique_id}");
            dots[slideIndex_{unique_id} - 1].classList.add("active-{unique_id}");
        }}

        setTimeout(showSlides_{unique_id}, 5000);
    }}
    </script>
    """

    return html_code



# Hobby page util functions
def load_images():
    target_size = (300, 300)
    img_1 = ImageOps.fit(Image.open("images/skiing_2.jpg"), target_size)
    img_2 = ImageOps.fit(ImageOps.exif_transpose(Image.open("images/crochet.jpeg")), target_size)
    img_3 = ImageOps.fit(Image.open("images/hiking.jpeg"), target_size)
    return img_1, img_2, img_3
