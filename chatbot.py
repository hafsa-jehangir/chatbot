import streamlit as st
import requests
st.image("https://images.seeklogo.com/logo-png/59/1/ollama-logo-png_seeklogo-593420.png", width=200)
st.title("Chatbot Interface")
if "messages" not in st.session_state:
    st.session_state.messages=[]
input=st.chat_input("Enter you message: ")
import requests

def ask_ollama(prompt):
    url = "http://localhost:11434/v1/chat/completions"
    payload = {
        "model": "llama3",
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(url, json=payload)
    return response.json()["choices"][0]["message"]["content"]

if input:
    st.session_state.messages.append({"role":"user","content":input})
    response= ask_ollama(input)
    st.session_state.messages.append({"role":"assistant","content":response})
for msg in st.session_state.messages:
    if msg["role"]=="user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**Bot:** {msg['content']}")  

reset=st.button("Reset Chat")
if reset:
    st.session_state.messages=[]