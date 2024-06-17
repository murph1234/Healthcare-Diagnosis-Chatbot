from src.helper import load_pdf, text_split, download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

# Set Pinecone API key
os.environ['PINECONE_API_KEY'] = 'f1c546bd-314f-4f77-a5fd-b26690c6779b'

# Load PDF data from the "data/" directory
extracted_data = load_pdf("data/")

# Split the extracted data into text chunks
text_chunks = text_split(extracted_data)

# Download HuggingFace embeddings
embedding = download_hugging_face_embeddings()

# Define the Pinecone index name
index_name = "medical-chatbot"

# Extract the text content from the text chunks
docs_chunks = [t.page_content for t in text_chunks]

# Create a Pinecone vector store from the text chunks and embeddings
pinecone_index = PineconeVectorStore.from_texts(
    docs_chunks,
    embedding,
    index_name=index_name
)
