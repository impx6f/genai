from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()
mykey=os.getenv("GROQ_API-KEY")
chat = ChatGroq(groq_api_key=mykey,model_name="llama-3.3-70b-versatile")

url_text=st.text_input("Enter a URL")
user_msg=st.text_input("Enter your message")

btn=st.button("Submit")

if btn:

    response= chat.invoke("solve the 0/1 knapsack problem using python")

    docs = WebBaseLoader(url_text)

    extractedText=docs.load()

    textFromFirstWebsite=extractedText[0].page_content

    extract_prompt=PromptTemplate.from_template("""
    ------------------
    The scrapped text is:
    {textFromFirstWebsite}
    -----------------
    Instruction:
    {user_msg}
    """)

    chain=extract_prompt | chat

    res=chain.invoke(input={'textFromFirstWebsite':textFromFirstWebsite,
    "user_msg":user_msg})


    print(res.content)


    st.title("Chat with any website")

    st.text(res.content)

    st.markdown(res.content,unsafe_allow_html=True)