# 🏥 Medical Chatbot (AI-Powered Healthcare Assistant)

## 📌 Project Overview
The **Medical Chatbot** is an AI-powered web application designed to provide basic medical information, symptom analysis, and health-related guidance. It uses Natural Language Processing (NLP) and Large Language Models (LLMs) to interact with users in a conversational manner.

This project helps users understand possible medical conditions and provides general health advice — **not a replacement for professional doctors**.

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

### ☁️ Deployment
- AWS
- Docker, Github Actions

---

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



