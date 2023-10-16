import streamlit as st

with open('styles.css') as f:
    st.markdown(f'<style>{(f.read())}</style>',unsafe_allow_html=True)
st.title("Personal Chatbot 🤖")

with st.sidebar:
    st.sidebar.header("Yet to Update..")
    user_csv = st.file_uploader("Upload your CSV File",type="csv")
    user_pdf = st.file_uploader("Upload PDF File", type="pdf")

if user_csv is not None:
    user_question = st.text_input("Ask a question about your CSV: ")

if user_pdf is not None:
    user_question = st.text_input("Ask a question about your PDF: ")

st.chat_input()