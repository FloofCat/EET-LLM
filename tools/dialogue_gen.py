from llama_index.llms.deepinfra import DeepInfraLLM
import streamlit as st
API_KEY = st.secrets["DEEP_INFRA"]
from llama_index.core.base.llms.types import ChatMessage

llm = DeepInfraLLM(
    model="meta-llama/Meta-Llama-3-8B-Instruct", 
    api_key=API_KEY,
    temperature=0.5,
    max_tokens=200,
    additional_kwargs={"top_p": 0.9},
)

dialogue_sys_msg = ""
with(open("./tasks/dialogue_gen.task", "r")) as f:
    dialogue_sys_msg += f.read()
    
def generate_topics(context):
    global dialogue_sys_msg
    messages = [
        ChatMessage(
            role="system", content=dialogue_sys_msg
        ),
        ChatMessage(role="user", content=context),
    ]
    resp = llm.chat(messages)
    resp = str(resp)
    
    topics = []
    topic_ids = ["TOPIC 1", "TOPIC 2", "TOPIC 3", "TOPIC 4", "TOPIC 5"]
    for line in resp.split("\n"):
        for topic_id in topic_ids:
            if topic_id in line:
                topics.append(line.split(topic_id + ": ")[1])
            
    return topics

