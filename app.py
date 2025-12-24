import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain_classic.chains import conversation
from  langchain_classic.prompts import ChatPromptTemplate
from langchain_classic.memory import ConversationBufferMemory
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

api = os.getenv("GROQ_API_KEY")

llm = ChatGroq(api_key= api , 
         model="llama-3.1-8b-instant",
        temperature= 1,
        max_tokens=  1000 )

user = st.text_input("pls ask me a question")
parser = StrOutputParser()


if st.button("click"):
    if user :
        chain = llm | parser
        response = chain.invoke(user)
        st.write(response)
