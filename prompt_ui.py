import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import load_prompt  # 💡 

# Load the environment variables from your local .env file
load_dotenv()

#  Initialize Gemini model framework (using pro for detailed research analysis)
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.3)

st.header('Research Tool')

paper_input = st.selectbox(
    "Select Research Paper Name", 
    ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"]
)

style_input = st.selectbox(
    "Select Explanation Style", 
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
) 

length_input = st.selectbox(
    "Select Explanation Length", 
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
)

# Load the template configuration file
template = load_prompt('template.json')

if st.button('Summarize'):
    # LCEL chain pipeline: Template passes variables into the Gemini model
    chain = template | model
    
    result = chain.invoke({
        'paper_input': paper_input,
        'style_input': style_input,
        'length_input': length_input
    })
    
    st.write(result.content)