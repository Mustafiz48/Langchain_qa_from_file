import os
from dotenv import load_dotenv
from langchain.embeddings import OpenAIEmbeddings
from Langchain import Langchain

load_dotenv()
open_ai_api_key = os.getenv("OPEN_AI_API_KEY")

if __name__ == '__main__':
    text_path = "the_winepress.txt"
    persist_directory = "vector_db"
    embedding = OpenAIEmbeddings(openai_api_key=open_ai_api_key)
    query = input("Please ask your question: ")
    langchain = Langchain()
    texts = langchain.load_and_process(text_path)
    if not os.listdir(persist_directory):
        langchain.init_persisted_chromadb(texts, persist_directory, embedding)
    qa = langchain.load_vecctordb_and_create_chain(persist_directory, embedding, open_ai_api_key)
    ans = langchain.ask_question(qa, query)
    print(ans)
