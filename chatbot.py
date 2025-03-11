import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_community.chat_models import ChatOpenAI

# you will need to get your own api key, by going to openai ai keys and generate a new api key. Then you can replace it with the one that's here
OPENAI_API_KEY = "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"

# Upload PDF file
st.header("My first chatbot")

with st.sidebar:
    st.title("Your Documents")
    file = st.file_uploader("Upload a PDF file and start asking questions", type=['pdf'])

#example file is the US Constitution
# Extract text from PDF if file is uploaded
if file is not None:
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    # Break into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        separators="\n",
        chunk_size=1000,
        chunk_overlap=150,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    #st.write(chunks)

    # Generate embeddings
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

    # Create a vector store - FAISS
    vector_store = FAISS.from_texts(chunks, embeddings)

    # Ask questions Like who can be president of the United States?
    user_question = st.text_input("Ask a question here")

    # Do similarity search
    if user_question:
        match = vector_store.similarity_search(user_question)
        #st.write(match)

        # Define LLM
        llm = ChatOpenAI(
            openai_api_key=OPENAI_API_KEY,
            temperature=0,
            max_tokens=1000,
            model_name="gpt-3.5-turbo"
        )

        # Output results
        chain = load_qa_chain(llm, chain_type="stuff")
        response = chain.run(input_documents=match, question=user_question)
        st.write(response)
