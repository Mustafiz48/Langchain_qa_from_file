from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import VectorDBQA
from langchain.document_loaders import TextLoader


class Langchain:
    def __init__(self):
        pass

    @staticmethod
    def load_and_process(text_path):
        # Load  the text
        loader = TextLoader(text_path)
        documents = loader.load()

        # create chunks from the document
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        texts = text_splitter.split_documents(documents)
        return texts

    @staticmethod
    def init_persisted_chromadb(texts, persist_directory, embedding):
        # Embed and store the texts
        # Supplying a persist_directory will store the embeddings on disk
        persist_directory = persist_directory
        vectordb = Chroma.from_documents(documents=texts, embedding=embedding, persist_directory=persist_directory)
        vectordb.persist()
        vectordb = None

    @staticmethod
    def load_vecctordb_and_create_chain(persist_directory, embedding, open_ai_api_key):
        # Now we can load the persisted database from disk, and use it as normal.
        vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding)
        qa = VectorDBQA.from_chain_type(llm=OpenAI(openai_api_key = open_ai_api_key), chain_type="stuff", vectorstore=vectordb)
        return qa

    @staticmethod
    def ask_question(qa, query):
        return qa.run(query)
