# 📚 PDF Chat Assistant

Chat with multiple PDF documents using the power of **LangChain**, **OpenAI**, and **Streamlit**. This application lets you upload PDF files, processes them into embeddings, and then ask intelligent questions based on their content.

> Built with 🧠 LangChain + 🗃️ FAISS + 🤖 OpenAI + 🎈 Streamlit

---

## 🔥 Features

- Upload and chat with multiple PDF files
- Uses OpenAI embeddings and LLMs for accurate responses
- Stores document embeddings in FAISS for fast retrieval
- Maintains conversation history using memory buffer
- Clean and interactive UI using Streamlit
- Designed for both casual use and document Q&A applications

---

## 🖼️ Demo Preview

![demo](https://user-images.githubusercontent.com/your-gif-or-screenshot.gif)

---

## 🛠️ Tech Stack

- **Frontend/UI**: Streamlit
- **LLM & Embeddings**: OpenAI (`text-embedding-ada-002`, `gpt-3.5-turbo`)
- **Vector Store**: FAISS (in-memory)
- **PDF Parsing**: PyPDF2
- **LangChain**: For chaining and memory

---

## 🚀 How to Run Locally

> ⚠️ **Note:** You must create a `.env` file with your OpenAI API key.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/pdf-chat-assistant.git
cd pdf-chat-assistant
```

### 2. Create and Activate Virtual Environment (Optional but Recommended)

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Your OpenAI API Key

Create a `.env` file in the project root with the following content:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

> 🔐 Do NOT commit this file to version control (`.gitignore` already excludes it).

### 5. Run the App

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
├── app.py                     # Main Streamlit application
├── htmlTemplates.py           # Custom HTML for chat bubbles and styling
├── requirements.txt           # Python dependencies
├── .env                       # Stores OpenAI API key (not tracked by Git)
├── .gitignore                 # Ignores .env and other unnecessary files
```

---

## ✅ Example Usage

1. Upload one or more PDF files from the sidebar.
2. Click "🚀 Process" to embed and analyze them.
3. Ask any question related to the documents in the input box.
4. Get smart, contextual answers from your documents!

---

## 🔒 Security Note

- This project uses in-memory FAISS and does not send PDF content to any third-party services other than OpenAI.
- Make sure not to expose your `.env` file or API key publicly.

---

## ✨ Future Improvements

- Support for OCR-based scanned PDFs (using Tesseract)
- Option to use local models like HuggingFace or Ollama
- Multi-language document support
- Upload history or persistent vector storage
- Feel free to fork and enhance!
---
