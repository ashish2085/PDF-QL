import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate

# Helper Functions
def configure_genai(api_key):
    """Configure Google Generative AI with the provided API key."""
    genai.configure(api_key=api_key)

def get_pdf_text(pdf_docs):
    """Extract text from uploaded PDF files."""
    text = ""
    for pdf in pdf_docs:
        try:
            pdf_reader = PdfReader(pdf)
            for page in pdf_reader.pages:
                text += page.extract_text()
        except Exception as e:
            st.error(f"Error reading {pdf.name}: {e}")
    return text

def get_text_chunks(text):
    """Split text into manageable chunks."""
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    return text_splitter.split_text(text)

def get_vector_store(text_chunks, api_key):
    """Create and save a FAISS vector store."""
    try:
        embeddings = GoogleGenerativeAIEmbeddings(google_api_key=api_key, model="models/embedding-001")
        vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
        vector_store.save_local("faiss_index")
    except Exception as e:
        st.error(f"Error creating vector store: {e}")

def get_conversational_chain(api_key):
    """Set up a conversational QA chain with a custom prompt."""
    prompt_template = """
    Answer the question as detailed as possible from the provided context.
    If the answer is not in the context, respond with:
    "I couldn't find an answer to your question in the provided context. You might want to refine your question or upload more relevant documents."
    
    Context:
    {context}
    Question:
    {question}
    Answer:
    """
    model = ChatGoogleGenerativeAI(google_api_key=api_key, model="gemini-pro", temperature=0.7)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    return load_qa_chain(model, chain_type="stuff", prompt=prompt)

def user_input(user_question, api_key):
    """Handle user queries and generate responses."""
    try:
        embeddings = GoogleGenerativeAIEmbeddings(google_api_key=api_key, model="models/embedding-001")
        vector_store = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
        docs = vector_store.similarity_search(user_question)
        chain = get_conversational_chain(api_key)
        response = chain({"input_documents": docs, "question": user_question}, return_only_outputs=True)
        return response["output_text"]
    except Exception as e:
        return f"Error processing query: {e}"

# Streamlit UI Configuration
st.set_page_config(page_title="PDF Query Language", page_icon="🔮")
st.header("PDF Query Language 🧙🏻‍♀️")
st.markdown("""
This app retrieves information from uploaded PDFs and answers your questions using Google Gemini.
""")

# Set API Key
if "api_key" not in st.session_state:
    st.session_state.api_key = None

st.sidebar.subheader("API Key Configuration")
st.session_state.api_key = st.sidebar.text_input(
    "Enter your Google Gemini API Key", 
    type="password",
    help="You can obtain your API key from the Google AI Developer Console."
)

st.sidebar.markdown("""
### How to Get Your API Key:
1. **Visit the [Google AI Developer Console](https://ai.google.dev/gemini-api/docs/api-key)**.
2. **Sign In:** Use your Google account to sign in.
3. **Create an API Key:** Follow the instructions to generate a new API key.
4. **Secure Your Key:** Keep it confidential to prevent unauthorized access.
""")

if st.session_state.api_key:
    configure_genai(st.session_state.api_key)

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Sidebar for PDF Uploads
with st.sidebar:
    st.image("images/genie.png")
    st.title("Your PDFs go here!")
    pdf_docs = st.file_uploader("Upload your PDF Files", accept_multiple_files=True)
    
    if st.button("Process"):
        if not st.session_state.api_key:
            st.error("Please set your API key before processing.")
        else:
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                if raw_text:
                    text_chunks = get_text_chunks(raw_text)
                    get_vector_store(text_chunks, st.session_state.api_key)
                    st.success("Processing complete! Ready for questions.")
                else:
                    st.error("No text extracted from the uploaded PDFs.")

# Chat Section
user_question = st.text_input("Ask any Question from the PDF Files")
if st.button("Ask"):
    if not st.session_state.api_key:
        st.error("Please set your API key before asking questions.")
    elif user_question:
        with st.spinner("Fetching response..."):
            response = user_input(user_question, st.session_state.api_key)
        # Save the question and response in the session state
        st.session_state.chat_history.append({"question": user_question, "answer": response})

# Display Chat History
st.subheader("Chat History")
for i, chat in enumerate(st.session_state.chat_history, 1):
    st.markdown(f"**Q{i}:** {chat['question']}")
    st.markdown(f"**A{i}:** {chat['answer']}")

# Footer
st.markdown("---")
st.markdown("*Built with ❤️ by Ashish Kumar*")
