from fastapi import FastAPI
from langchain.vectorstores.pgvector import PGVector
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title = 'GenAI')


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

@app.get("/retrieve_intent", tags = ['Vectors'])
async def retrieve_intent(question):

    # embedding model
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=GEMINI_API_KEY)
    
    # PG Vector
    connection_string = "postgresql+psycopg2://postgres:postgres@host.docker.internal:5432/vector_db" 
    collection = "test_collection"
    
    # load vector db object
    vector_store = PGVector(
    connection_string=connection_string,
    embedding_function=embeddings,
    collection_name= collection
    )

    result = vector_store.similarity_search(question, k = 1)
    for doc in result:
        intent = doc.page_content
    
    return {"intent":intent}



    

