# 🏥 Medical Chatbot (AI-Powered Healthcare Assistant)

## 📌 Project Overview
The **Medical Chatbot** is an AI-powered healthcare assistant designed to provide basic medical information, symptom-based guidance, and conversational support using Natural Language Processing (NLP) and Large Language Models (LLMs). The system leverages a Retrieval-Augmented Generation (RAG) architecture to enhance response accuracy by combining pre-trained language models with a domain-specific medical knowledge base.
The application integrates LangChain for workflow orchestration, Pinecone as a vector database for semantic search, and Flask for backend development. Sentence embeddings are generated using models from Hugging Face, enabling efficient similarity search. The chatbot is deployed using cloud and DevOps tools such as Amazon Web Services, Docker, and CI/CD pipelines.
This system aims to assist users in understanding symptoms and accessing general medical knowledge while emphasizing that it is not a substitute for professional healthcare consultation.

---

## 🎯 Objectives
- Provide quick medical information based on user queries  
- Assist users in identifying symptoms and possible conditions  
- Build an interactive chatbot for healthcare support  
- Implement Retrieval-Augmented Generation (RAG)  
- Deploy the project on a free platform  

---

## 🚀 Features
- 💬 Chat-based UI  
- 🧠 AI-powered responses  
- 📚 Medical knowledge base integration  
- 🔍 Symptom-based query handling  
- 🌐 Web-based application  
- 🔐 Optional login/authentication system  

---

## 🛠️ Tech Stack

### 👨‍💻 Frontend
- HTML5  
- CSS3   
- JavaScript 

### ⚙️ Backend
- Python  
- Flask  

### 🤖 AI / ML
- LangChain  
- LLM APIs (Groq)  
- Embeddings & Vector Store
- Pinecone
- Hugging Face (Sentence Transformers)

### ☁️ Deployment
- AWS
- Docker, Github Actions

---

## Model Architecture 
Architecture: Retrieval-Augmented Generation (RAG)
Flow:
1.	Medical PDF → Text Extraction 
2.	Text → Chunking 
3.	Chunking → Embeddings (Sentence Transformer) 
4.	Embeddings → Stored in Vector DB (Pinecone) 
5.	User Query → Converted to Embedding 
6.	Similar chunks retrieved from DB 
7.	Context + Query → LLM (Groq API) 
8.	Final Response generated

   
### Architecture Components:
-	Data Source: Medical PDF 
-	Embedding Model: Sentence Transformers (via Hugging Face) 
-	Vector Store: Pinecone 
-	LLM: Groq API 
-	Framework: LangChain 
-	Backend: Flask 
-	Deployment: AWS EC2 + AWS ECR + IAM  + Docker + CI/CD


## 📂 Project Structure
📦 Medical-Chatbot
│
├── 📁 .github
│ └── 📁 workflows
│ └── ⚙️ cicd.yaml # CI/CD pipeline
│
├── 📁 data
│ └── 📄 Medical_book.pdf # Knowledge base
│
├── 📁 research
│ └── 📓 trials.ipynb # Experiments
│
├── 📁 src
│ ├── 🐍 helper.py # Utility functions
│ ├── 🐍 prompt.py # Prompt templates
│ └── 🐍 init.py
│
├── 📁 static
│ └── 🎨 style.css # Styling
│
├── 📁 templates
│ └── 🌐 chat.html # Frontend UI
│
├── 🐍 app.py # Main Flask app
├── 🐍 store_index.py # Vector DB creation
├── 📄 requirements.txt # Dependencies
├── 🐳 Dockerfile # Container setup
├── ⚙️ setup.py # Package setup
├── 🖥️ template.sh # Setup script
├── 🔐 .env # API keys (not pushed)
├── 🚫 .gitignore
├── 📜 LICENSE
└── 📘 README.md



