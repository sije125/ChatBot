# PDF Chatbot with OpenAI and FAISS

Overview

This Streamlit-based chatbot allows users to upload a PDF file and ask questions about its content. The system extracts text from the PDF, processes it into chunks, generates vector embeddings, and uses OpenAI's GPT model to answer questions based on the document's content.

# Features

Upload a PDF document

Extract text from the document

Split text into manageable chunks

Generate vector embeddings using OpenAI Embeddings

Store and retrieve relevant document chunks using FAISS

Query the document and receive AI-generated responses

# Requirements

Ensure you have the following dependencies installed before running the project:

pip install streamlit PyPDF2 langchain openai faiss-cpu

Usage

Run the Streamlit App

streamlit run chatbot.py

Upload a PDF File

Click on the sidebar and upload a PDF (e.g., the U.S. Constitution).

# Ask Questions

Type a question in the input box (e.g., Who can be president of the United States?).

The chatbot will process the question and return an answer based on the document's content.

# How It Works

PDF Processing: The PDF is read using PyPDF2, and text is extracted.

Text Splitting: The text is broken into chunks using RecursiveCharacterTextSplitter to improve search efficiency.

Vector Embeddings: OpenAI Embeddings (text-embedding-ada-002) are generated for the chunks.

FAISS Vector Storage: The embeddings are stored and used for similarity search.

Question Answering: When a user submits a query, relevant document chunks are retrieved, and OpenAI's GPT model generates a response.

Environment Variables

Replace OPENAI_API_KEY with your OpenAI API key in the code:

OPENAI_API_KEY = "your-api-key-here"

# Notes
you will need to be in a virtual environment.
you can do this by typing: venv\Scripts\activate into the terminal

The chatbot currently supports text-based PDFs only.

FAISS is used for efficient similarity search but can be replaced with another vector database.

Future Enhancements

Improve response accuracy with fine-tuned models.

Add support for multiple file formats (e.g., DOCX, TXT).

Implement persistent storage for previously uploaded documents.
# you will need to get your own api key, by going to openai ai keys and generate a new api key. Then you can replace it with the one that's there
