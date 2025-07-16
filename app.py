import streamlit as st
import time 
from src.helper import get_pdf_text, get_text_chunks, get_vector_store, get_conversational_chain

def user_input(user_query):
    # Clear previous chat history display
    if 'chatHistory' in st.session_state:
        del st.session_state.chatHistory
    
    # Get response for the current question
    response = st.session_state.conversation({"question": user_query})
    
    # Display only the current question and response
    st.write(f"**User:** {user_query}")
    st.write(f"**Bot:** {response['answer']}")


def main():
    st.title("Information Retrieval")
    st.header("Welcome to the Information Retrieval System 🚀")
    user_query = st.text_input("Ask a question about the uploaded documents:")

    if 'conversation' not in st.session_state:
        st.session_state.conversation = None
    if 'conversation_history' not in st.session_state:
        st.session_state.conversation_history = []
    if user_query:
        user_input(user_query)

    with st.sidebar:
        st.subheader("Menu: ")
        pdf_docs = st.file_uploader("Upload PDF Documents and click on the submit and process button", accept_multiple_files=True)
        if st.button("Submit and Process"):
            with st.spinner("Processing..."):
                time.sleep(2)
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                vector_store = get_vector_store(text_chunks)
                st.session_state.conversation = get_conversational_chain(vector_store)

                st.success("Documents processed successfully!")
                
        


if __name__ == "__main__":
    main()
