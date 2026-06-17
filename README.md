# Conversational Document Search Engine

Ask questions. Get answers grounded in your documents. No hallucinations.

## Quick Start

```bash
pip install -r requirements.txt
```

Create `.env`:
```
api=your_key
```

Run:
```bash
python terminal_app.py
```

## How It Works

Upload PDF → Chunk text → Create embeddings → Search semantically → LLM answers based on retrieved content

## Stack

- LangChain
- FAISS (vector search)
- NVIDIA NIM (free LLM)
- Python

## Features

✅ Works with any document  
✅ Interactive chat mode  
✅ fewer hallucinations  
✅ Save/load vector stores   

## Usage

```python
from main import RAGApplication

app = RAGApplication()
app.load_documents("document.pdf")
answer = app.ask("Your question?")
```

## Use Cases

- Research papers
- FAQ databases
- Legal documents
- Internal knowledge bases

## Why RAG?

LLMs hallucinate on domain-specific info. RAG forces them to retrieve actual documents first, then answer.

**Result:** Accurate answers from your content.

