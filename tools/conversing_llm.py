from peft import PeftModel, PeftConfig
from transformers import AutoModelForCausalLM, AutoTokenizer

config = PeftConfig.from_pretrained("Advik007/EET-LLM")
base_model = AutoModelForCausalLM.from_pretrained("unsloth/Phi-3-mini-4k-instruct")
model = PeftModel.from_pretrained(base_model, "Advik007/EET-LLM")
tokenizer = AutoTokenizer.from_pretrained("./model/")

conversation_sys_msg = ""
with(open("./tasks/conversing.task", "r")) as f:
    conversation_sys_msg += f.read()
    
def generate_possible_user_prompt(context):
    global conversation_sys_msg
    system_message = conversation_sys_msg + "\nHere's the context of the conversation: " + context

    inputs = tokenizer(system_message, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=1024)
    
    resp = tokenizer.decode(outputs[0], skip_special_tokens=True)
    resp = str(resp)
    
    # remove "assistant:""
    resp = resp.replace("assistant: ", "")
    
    user_pred = ""
    for line in resp.split("\n"):
        if "HELPER [USER]:" in line:
            user_pred += line.split("HELPER [USER]: ")[1]
    
    return user_pred

