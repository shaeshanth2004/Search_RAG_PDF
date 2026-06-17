from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv
load_dotenv()

# Pass the key directly into the components
my_key =os.getenv("api")

embeddings = NVIDIAEmbeddings(
    model="nvidia/nv-embed-v1",
    nvidia_api_key=my_key
)

llm = ChatNVIDIA(
    model="meta/llama-3.1-70b-instruct",
    nvidia_api_key=my_key
)

loader = PyPDFLoader("Source/Path....")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
chunks = splitter.split_documents(docs)






vector_db = FAISS.from_documents(
    chunks,
    embeddings
)
vector_db.save_local("faiss_index")


retriever = vector_db.as_retriever(
    search_kwargs={"k": 3}
)





prompt = ChatPromptTemplate.from_template("""
You are a helpful assistant.

Answer ONLY from the supplied context.

Context:
{context}

Question:
{question}
""")




def ask(question):

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    final_prompt = prompt.format(
        context=context,
        question=question
    )

    response = llm.invoke(final_prompt)

    return response.content
