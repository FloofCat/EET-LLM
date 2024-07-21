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

# Get system message from rl.task file
system_msg = ""
with open("./tasks/rl.task", "r") as f:
    system_msg = f.read()

def generate_reward_score(prompt):
    messages = [
        ChatMessage(
            role="system", content=system_msg
        ),
        ChatMessage(role="user", content=prompt),
    ]
    resp = llm.chat(messages)
    
    resp = str(resp)
    
    # Get the score and emotion detected
    # resp is a string and you need to get the score which is after "SCORE:" and the emotion detected which is after "EMOTION DETECTED:"
    score = 0
    emotion_detected = "neutral"
    for line in resp.split("\n"):
        if "SCORE:" in line:
            score = float(line.split("SCORE: ")[1])
        
        if "EMOTION DETECTED:" in line:
            emotion_detected = line.split("EMOTION DETECTED: ")[1]
            
    print("LOGS: " + resp)
    return score, emotion_detected
