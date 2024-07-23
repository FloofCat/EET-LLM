import streamlit as st
import workflow
import random
import time

st.title('EET-LLM: Emotional Empathetic Task-oriented Large Language Model')

def response_generator():
    response = workflow.generate_output(prompt)
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = ''.join([word + " " for word in response_generator()])
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

st.markdown("[Provide your feedback here!](https://github.com/BitC3t/EET-LLM/issues/1)")