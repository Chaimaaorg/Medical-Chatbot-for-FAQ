from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
import os

from dotenv import load_dotenv
load_dotenv()  

llm = ChatGoogleGenerativeAI(google_api_key=os.environ["GOOGLE_API_KEY"], temperature=0.1,model="models/gemini-1.5-flash")
instructor_embeddings = SentenceTransformerEmbeddings(model_name="sentence-transformers/paraphrase-MiniLM-L6-v2")
vectordb_file_path = "faiss_index"

def create_vector_db():
    # Load data from FAQ sheet
    loader = CSVLoader(file_path='Mental_Health_FAQ.csv', source_column="Questions")
    data = loader.load()

    # Create a FAISS instance for vector database from 'data'
    vectordb = FAISS.from_documents(documents=data,
                                    embedding=instructor_embeddings)

    # Save vector database locally
    vectordb.save_local(vectordb_file_path)


def get_qa_chain():
    # Load the vector database from the local folder
    vectordb = FAISS.load_local(vectordb_file_path, instructor_embeddings)

    # Create a retriever for querying the vector database
    retriever = vectordb.as_retriever(score_threshold=0.7)

    prompt_template = """Given the following context and a question, generate an answer based on this context only.
    In the answer try to provide as much text as possible from "response" section in the source document context without making much changes.
    If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.

    CONTEXT: {context}

    QUESTION: {question}"""

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    chain = RetrievalQA.from_chain_type(llm=llm,
                                        chain_type="stuff",
                                        retriever=retriever,
                                        input_key="query",
                                        return_source_documents=True,
                                        chain_type_kwargs={"prompt": PROMPT})

    return chain
