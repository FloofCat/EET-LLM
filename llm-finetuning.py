from datasets import load_dataset
from huggingface_hub import login, whoami
from peft import LoraConfig, get_peft_model
from transformers import AutoModelForCausalLM, TrainingArguments, BitsAndBytesConfig
import torch
from trl import SFTTrainer
import streamlit as st

API_KEY = st.secrets["HF_API_KEY"]
login(token=API_KEY)

training = load_dataset("Estwld/empathetic_dialogues_llm")

training_data = (
    training['train']
    .shuffle()
    .map(
        remove_columns=["conv_id", "situation", "emotion"]
    )
)

eval_data = (
    training['valid']
    .shuffle()
    .map(
        remove_columns=["conv_id", "situation", "emotion"]
    )
)

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
)

model = AutoModelForCausalLM.from_pretrained("unsloth/Phi-3-mini-4k-instruct", quantization_config=bnb_config, trust_remote_code=True)
config = LoraConfig(
            r=64,
            lora_alpha=16,
            lora_dropout=0.1,
            bias="none",
            task_type="CAUSAL_LM",
            target_modules=["o_proj" ,"qkv_proj"]
        )

training_arguments = TrainingArguments(
    output_dir="finetuned-eet",
    per_device_train_batch_size=8,
    per_device_eval_batch_size=16,
    gradient_accumulation_steps=4,
    optim="paged_adamw_32bit",
    learning_rate=2e-4,
    logging_steps=1,
    fp16=True,
    max_grad_norm=0.3,
    warmup_ratio=0.03,
    group_by_length=True,
    num_train_epochs=3,
    evaluation_strategy="steps",
)

model = get_peft_model(model, config)
model.print_trainable_parameters()


trainer = SFTTrainer(
    model=model,
    train_dataset=training_data,
    eval_dataset=eval_data,
    args=training_arguments,
)

trainer.train()

training_logs = trainer.state.log_history
import matplotlib.pyplot as plt
train_loss = [log["loss"] for log in training_logs if "loss" in log]
eval_loss = [log["eval_loss"] for log in training_logs if "eval_loss" in log]

plt.figure(figsize=(10, 5))
plt.plot(range(len(train_loss)), train_loss, label="Training Loss")
plt.plot(range(len(eval_loss)), eval_loss, label="Evaluation Loss")
plt.xlabel("Steps")
plt.ylabel("Loss")
plt.title("Loss vs. Training Steps")
plt.legend()
plt.savefig("./training_loss.png")

trainer.save_model("./model")

model.save_pretrained("./model2")


            
        
    

