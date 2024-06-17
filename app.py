from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from langchain_huggingface import HuggingFaceEmbeddings

from langchain_pinecone import PineconeVectorStore

from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
from src.prompt import *
import os

# Initialize Flask app
app = Flask(__name__)

# Load environment variables from a .env file
load_dotenv()

# Initialize HuggingFace embeddings
embedding = HuggingFaceEmbeddings()

# Set Pinecone API key
os.environ['PINECONE_API_KEY'] = 'f1c546bd-314f-4f77-a5fd-b26690c6779b'
index_name = "medical-bot"

# Initialize Pinecone vector store using an existing index
pinecone_index = PineconeVectorStore.from_existing_index(
   index_name, embedding
)

# Set up the prompt template
PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

# Configuration for the chain type
chain_type_kwargs = {"prompt": PROMPT}

# Initialize the language model
llm = CTransformers(model="model/llama-2-7b-chat.ggmlv3.q4_0.bin",
                    model_type="llama",
                    config={'max_new_tokens': 512, 'temperature': 0.8})

# Set up the RetrievalQA chain
qa = RetrievalQA.from_chain_type(
    llm=llm, 
    chain_type="stuff", 
    retriever=pinecone_index.as_retriever(search_kwargs={'k': 2}),
    return_source_documents=True, 
    chain_type_kwargs=chain_type_kwargs
)

# Define the route for the homepage
@app.route("/")
def index():
    return render_template('chat.html')

# Define the route for handling chat messages
@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    
    # Process the input query using the QA chain
    result = qa({"query": input})
    print("Response : ", result["result"])
    
    # Return the result as a string
    return str(result["result"])

# Run the app
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
