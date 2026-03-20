from flask import Flask, render_template, jsonify, request
from src.helper import download_embed
from langchain_pinecone import PineconeVectorStore
from langchain_groq import ChatGroq
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os


app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
groq_api_key=os.getenv("GROQ_API_KEY")

os.environ["PINECONE_API_KEY"]= PINECONE_API_KEY
os.environ["GROQ_API_KEY"]= groq_api_key

embedding = download_embed()

index_name = "medi-chatbot"

docsearch = PineconeVectorStore.from_existing_index(
  embedding=embedding,
  index_name=index_name
)

retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k":3})

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant"
)
prompt = ChatPromptTemplate.from_messages(
  [
    ("system", system_prompt),
    ("human", "{input}"),
  ]
)

que_ans_chain = create_stuff_documents_chain(llm,prompt)
rag_chain = create_retrieval_chain(retriever, que_ans_chain)

@app.route("/")
def index():
  return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    response = rag_chain.invoke({"input": msg})
    print("Response : ", response["answer"])
    return str(response["answer"])



if __name__ == '__main__':
  app.run(host="0.0.0.0", port = 8080, debug=True)
