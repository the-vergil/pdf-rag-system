from google import genai
from llama_index.readers.file import PDFReader
from llama_index.core.node_parser import SentenceSplitter
from dotenv import load_dotenv
import os

load_dotenv()

print("GEMINI_API_KEY loaded:", bool(os.getenv("GEMINI_API_KEY")))

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

EMBED_MODEL = "gemini-embedding-001"
EMBED_DIM = 3072

splitter = SentenceSplitter(
    chunk_size=1000,
    chunk_overlap=200
)


def load_and_chunk_pdf(path: str):
    docs = PDFReader().load_data(file=path)

    texts = [
        d.text
        for d in docs
        if getattr(d, "text", None)
    ]

    chunks = []

    for text in texts:
        chunks.extend(splitter.split_text(text))

    return chunks


def embed_texts(texts: list[str]) -> list[list[float]]:
    print(f"Generating embeddings for {len(texts)} chunks...")

    response = client.models.embed_content(
        model=EMBED_MODEL,
        contents=texts
    )

    vectors = [embedding.values for embedding in response.embeddings]

    print(f"Generated {len(vectors)} embeddings")

    return vectors
