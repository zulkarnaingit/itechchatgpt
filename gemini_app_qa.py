import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

# Set page configuration with title and icon
st.set_page_config(
    page_title="I-TECH Generative AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
    <style>
        .main {
            background-color: #F0F8FF;
            padding: 2rem;
        }
        .stTextInput>div>div>input {
            background-color: #ffffff;
            color: #333333;
        }
        .header {
            color: #4a4a4a;
            padding: 1rem 0;
        }
        .info-box {
            background-color: #e8f4fc;
            border-radius: 10px;
            padding: 1.5rem;
            margin-bottom: 2rem;
        }
        .response-box {
            background-color: #ffffff;
            border-radius: 10px;
            padding: 1.5rem;
            margin-top: 1rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .logo {
            display: flex;
            align-items: center;
            margin-bottom: 1rem;
        }
        .logo img {
            height: 60px;
            margin-right: 15px;
        }
    </style>
""", unsafe_allow_html=True)

# Header with logo
col1, col2 = st.columns([1, 4])
with col1:
    st.image("itechlogo.jpg", width=200)  # Replace with your actual logo URL
with col2:
    st.markdown("<h1 class='header'>I-TECH Generative AI Assistant</h1>", unsafe_allow_html=True)

# Information section about Generative AI
st.markdown("""
    <div class='info-box'>
        <h2>Welcome to the Future of AI Conversations</h2>
        <p>This assistant is powered by I-Tech AI, one of the most advanced generative AI models available today.</p>
        
        <p>Ask anything - from technical questions to creative brainstorming!</p>
    </div>
""", unsafe_allow_html=True)

# Initialize the model
@st.cache_resource
def load_model():
    return ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )

llm = load_model()

# Set up the prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful, knowledgeable, and friendly AI assistant from I-TECH. Provide clear, concise, and accurate responses."),
    ("human", "Question: {question}")
])

# Chat interface
input_text = st.text_input(
    "Enter your question here:",
    placeholder="Type your question and press Enter...",
    key="user_input"
)

output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    with st.spinner('Generating response...'):
        try:
            response = chain.invoke({'question': input_text})
            st.markdown(f"""
                <div class='response-box'>
                    <h3>AI Response:</h3>
                    <p>{response}</p>
                </div>
            """, unsafe_allow_html=True)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #666666; font-size: 0.9rem;'>
        <p>Powered by © 2023 I-TECH AI Solutions</p>
    </div>
""", unsafe_allow_html=True)
