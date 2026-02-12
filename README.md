# TempleAssistant - Pilgrimage QA System 🛕🤖

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/framework-flask-orange.svg)](https://flask.palletsprojects.com/)
[![Groq](https://img.shields.io/badge/LLM-Groq-green.svg)](https://groq.com/)
[![Pinecone](https://img.shields.io/badge/VectorDB-Pinecone-blueviolet.svg)](https://www.pinecone.io/)

**TempleAssistant** is a context-aware Retrieval-Augmented Generation (RAG) system designed to answer complex queries about temples and pilgrimage sites. By leveraging high-performance LLMs (via Groq), vector similarity search (via Pinecone), and automated data scraping, it provides factual and concise information sourced directly from trusted corpora.

---

## 🚀 Features

- **Automated Scraping**: Periodically fetches data from reliable sources like Wikipedia using specialized scraping scripts.
- **Content Digitization**: Converts scraped HTML content into multi-page PDFs for standardized processing.
- **Semantic Search**: Uses HuggingFace embeddings and Pinecone vector store for accurate context retrieval.
- **Intelligent QA**: Powered by `llama-3.1-8b-instant` on Groq for lightning-fast, factual responses.
- **Clean UI**: A user-friendly Flask-based chat interface.

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **LLM Orchestration**: LangChain
- **Vector Database**: Pinecone
- **Inference Engine**: Groq (Llama 3.1)
- **Embeddings**: HuggingFace Sentence Transformers
- **Data Acquisition**: BeautifulSoup4, Requests, Readability-lxml

---
## Architecture
<img width="279" height="640" alt="image" src="https://github.com/user-attachments/assets/204bddeb-12e8-48a8-8de8-8befb40a8257" />


---

## 📁 Project Structure

```text
piligramageQA/
├── app.py              # Flask Application & RAG Logic
├── scrape.py           # Web Scraping & PDF Generation Script
├── store_index.py      # Pinecone Ingestion Script
├── src/
│   ├── helper.py       # Embedding & Utility Functions
│   └── prompt.py       # System Prompts & Templates
├── templates/
│   └── chat.html       # UI Template
├── static/
│   └── style.css       # UI Styling
├── data/               # Ingested Content & Metadata
├── .env                # Environment Variables (Private)
└── requirements.txt    # Python Dependencies
```

---

## ⚙️ Setup & Installation

### 1. Prerequisites
- Python 3.10+
- Pinecone API Key ([Get it here](https://app.pinecone.io/))
- Groq API Key ([Get it here](https://console.groq.com/))

### 2. Clone & Install
```bash
git clone https://github.com/rohithsukka/piligramageQA.git
cd piligramageQA
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Environment Variables
Create a `.env` file in the root directory:
```ini
PINECONE_API_KEY="your_pinecone_api_key"
GROQ_API_KEY="your_groq_api_key"
```

---

## 📖 Usage Guide

### Step 1: Data Acquisition
Run the scraper to fetch temple data and generate PDFs in the `data/` folder.
```bash
python scrape.py
```

### Step 2: Ingest into Vector Store
Initialize the Pinecone index and upload the document embeddings.
```bash
python store_index.py
```

### Step 3: Launch Assistant
Start the Flask server.
```bash
python app.py
```
Access the UI at `http://localhost:8080`.

---

## 🧠 System Design (RAG Workflow)
1. **User Query**: User asks a question via the chat interface.
2. **Retrieval**: The system searches the Pinecone index (`temples`) for top-3 relevant document chunks.
3. **Augmentation**: The chunks are injected into a specialized `TempleAssistant` system prompt.
4. **Generation**: Groq processes the context-rich prompt and returns a concise, factual answer.

---
## Demo Image
<img width="1914" height="856" alt="image" src="https://github.com/user-attachments/assets/93f6fbda-9f1e-4e39-a9ae-da422be2aebe" />


---

## 🤝 Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements.

---

## 📜 License
This project is licensed under the MIT License - see the LICENSE file for details.
