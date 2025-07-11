
import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from htmlTemplates import css, bot_template, user_template

load_dotenv()


def get_pdf_text(pdf_docs):
    text_docs = ""
    for doc in pdf_docs:
        pdf_reader = PdfReader(doc)
        for page in pdf_reader.pages:
            text_docs += page.extract_text()
    return text_docs


def get_text_chunks(raw_text):
    text_splitter = CharacterTextSplitter(
        separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len
    )
    chunks = text_splitter.split_text(raw_text)
    return chunks


def get_vectorstores(chunks):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts=chunks, embedding=embeddings)
    return vectorstore


def get_conversation_chain(vecst):
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm, retriever=vecst.as_retriever(), memory=memory
    )
    return conversation_chain


def handle_user_ip(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace('{{MSG}}', message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace('{{MSG}}', message.content), unsafe_allow_html=True)


# ---------- Streamlit Layout ---------- #

st.set_page_config(
    page_title="PDF Chat Assistant",
    page_icon="📚",
    layout="wide"
)
st.write(css, unsafe_allow_html=True)

if 'conversation' not in st.session_state:
    st.session_state.conversation = None
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = None

st.title("📚 Chat with Multiple PDFs")
st.markdown("<h3 style='color:#56ccf2;'>Ask questions, get intelligent responses from your documents</h3>", unsafe_allow_html=True)

user_quest = st.text_input("Ask a question about your documents:")

if user_quest:
    handle_user_ip(user_quest)

# ---------- Sidebar ---------- #
with st.sidebar:
    st.subheader("📁 Your Documents")
    pdfs = st.file_uploader(
        "Upload Your PDFs here and press 'Process'", accept_multiple_files=True
    )

    if st.button("🚀 Process"):
        with st.spinner("Processing documents... Please wait."):
            # Step 1: Extract Text
            text = get_pdf_text(pdfs)

            # Step 2: Text Splitting
            text_chunks = get_text_chunks(text)

            # Step 3: Vector Embeddings
            vecstore = get_vectorstores(text_chunks)

            # Step 4: Conversational Chain
            st.session_state.conversation = get_conversation_chain(vecstore)

        st.success("✅ Documents processed! Start chatting now.")

    st.markdown("---")
    st.markdown("#### 💡 Tips:")
    st.markdown("- Upload multiple PDFs")
    st.markdown("- Ask specific or general questions")
    st.markdown("- Use clear language for best results")
