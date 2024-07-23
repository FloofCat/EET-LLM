from peft import PeftModel, PeftConfig
from transformers import AutoModelForCausalLM, AutoTokenizer

config = PeftConfig.from_pretrained("Advik007/EET-LLM")
base_model = AutoModelForCausalLM.from_pretrained("facebook/opt-125m")
model = PeftModel.from_pretrained(base_model, "Advik007/EET-LLM")
tokenizer = AutoTokenizer.from_pretrained("./model/")

# Get reward score
import sys
sys.path.append("./RL/")
sys.path.append("./tools/")
import rlsetup
import dialogue_gen
import conversing_llm

context_old = "Here lies older conversations to learn context of the conversation: "
context_non = ""

def generate_output(prompt):
    # Get topics
    global context_non, context_old
    context_old += "\nUSER:" + prompt
    context_non += "\nUSER:" + prompt
    topics = dialogue_gen.generate_topics(context_non)
    
    if topics == []:
        resp = generate_topic_output(prompt, "Validate user's emotions.")
        context_old += "\nASSISTANT:" + resp
        context_non += "\nASSISTANT:" + resp
        return resp
    
    # best variables
    best_score = 0
    best_topic = ""
    best_resp = ""
    
    for topic in topics:
        resp = generate_topic_output(prompt, topic)
        temp_context = context_non + "\nASSISTANT:" + resp
        predicted_prompt = conversing_llm.generate_possible_user_prompt(temp_context)
        
        if predicted_prompt == "":
            continue
        
        score, _ = rlsetup.generate_reward_score(predicted_prompt)
        if score > best_score:
            best_score = score
            best_resp = resp
            best_topic = topic
    
    print("List of topics: " + str(topics) + "; Best topic: " + best_topic)
    context_old += "\nASSISTANT:" + best_resp
    context_non += "\nASSISTANT:" + best_resp
    return best_resp
        
def generate_topic_output(prompt, topic):
    global context_old, count
    score, emotion = rlsetup.generate_reward_score(prompt)
    score = str(score)
    
    system_msg = ""
    with open("./tasks/system.task", "r") as f:
        system_msg += f.read()
        
    if count != 0:
        system_msg += "\n\n" + context_old

    # add score and emotion to system message
    system_msg += f"\nSCORE: {score}\nEMOTION DETECTED: {emotion}\nTOPIC: {topic}"
    
    combined_input = "System: \n" + system_msg + "\n\nUser: \n" + prompt
    
    inputs = tokenizer(combined_input, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=1024)
    
    resp = tokenizer.decode(outputs[0], skip_special_tokens=True)
    resp = str(resp)
    
    return resp