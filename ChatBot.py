import streamlit as st
import google.generativeai as genai
API_KEY=AIzaSyB7xzMQagiej76HKVhss3SQzLzeyUzfZNI
genai.configure(api_key=API_KEY)
model=genai.GenerativeModel('gemini-1.5-flash')
if "chat" not in st.session_state:
    st.session_state.chat=model.start_chat(history=[])
st.title=('chatbot')
st.write('This is chatbot made by Pranathi.......')
if "message" not in st.session_state:
  st.session.message=[]
for message in st.session_state.message:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])
if prompt:=st.chat_input("what is up"):
  st.session_state.message.append({"role":"user","content":prompt})
  with st.chat_message("user"):
    st.markdown(prompt)
  response=st.session_state.chat.send_message(prompt)
  with st.chat_message("assistant"):
    st.markdown(response.text)
  st.session_state.message.append({"role":"assistant","content":response.text})
