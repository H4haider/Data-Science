﻿import streamlit as st
from backend import answer

st.title("Chatbot using Groq and Streamlit")

if "messages" not in st.session_state:
    st.session_state.messages=[]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt:=st.chat_input("Write your prompt"):
    st.session_state.messages.append({"role":"user", "content":prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

with st.chat_message("assistant"):
    response=answer(prompt)
    res=st.write_stream(response)
    st.session_state.messages.append({"role":"assistant", "content":res})
