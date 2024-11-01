# app/nlp.py
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores.faiss import FAISS
from .schemas import DocumentCreate
import os

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Initialize the Google Gemini client
from google.cloud import gemini
from .config import settings  # Import settings

# Create your Gemini client using the API key from the settings
client = gemini.Client(api_key=settings.GEMINI_API_KEY)

class GoogleGeminiEmbeddings:
    def __init__(self):
        self.client = client

    def embed_text(self, text: str):
        # Assuming the Gemini client has an `embed` method for text embeddings
        response = self.client.embed(text)
        return response.embeddings

# Initialize embeddings with Google Gemini
embeddings = GoogleGeminiEmbeddings()  # Update according to actual usage

# Initialize the vector store
vectorstore = FAISS(embeddings)  
index = VectorStoreIndex(vectorstore=vectorstore)

def index_document(document: DocumentCreate):
    """Indexes a document after it's uploaded."""
    document_obj = {
        "filename": document.filename,
        "content": document.content,
        "metadata": document.document_metadata,
    }
    index.add_documents([document_obj])

def query(user_query: str):
    """Query the index for relevant documents based on user input."""
    relevant_docs = index.query(user_query)
    return relevant_docs
