from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.embeddings import FakeEmbeddings

vector_store = None

def ingest_pdfs(files):
    global vector_store
    texts = []

    for file in files:
        reader = PdfReader(file)
        for page in reader.pages:
            text = page.extract_text()
            if text:
                texts.append(text)

    if not texts:
        return

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    chunks = splitter.split_text("\n".join(texts))

    # ✅ NO INTERNET, NO API, NO TORCH
    embeddings = FakeEmbeddings(size=768)

    vector_store = FAISS.from_texts(chunks, embeddings)


def rag_answer(query: str) -> str:
    if vector_store is None:
        return "No documents uploaded yet."

    docs = vector_store.similarity_search(query, k=4)
    return "\n".join([d.page_content for d in docs])
