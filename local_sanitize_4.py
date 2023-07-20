import tkinter as tk
from tkinter import scrolledtext
from transformers import pipeline, set_seed, GPT2Tokenizer, GPT2Model

set_seed(42)
tokenizer = GPT2Tokenizer.from_pretrained('gpt2-medium')
model = GPT2Model.from_pretrained('gpt2-medium')
generator = pipeline('text-generation', model=model, tokenizer=tokenizer)

def sanitize_data(text):
    prompt = f"Sanitize the following sensiti information and replace it with similar, but fake data, while keeping rest of the information exactly the same. Sensitive information which needs to be replaced, can be a company's name, a person's name, a database, server or application's name, a date, time, addresses, I.P. addresses, Port Numbers, keys, etc.:\n\n{text}\n\n---\n\nSanitized text:"

    generated_text = generator(prompt, max_length=1024, num_return_sequences=1)

    sanitized_text = generated_text[0]["generated_text"]
    return sanitized_text

def sanitize_button_click():
    input_text = input_textbox.get("1.0", "end-1c")
    sanitized_text = sanitize_data(input_text)
    output_textbox.delete("1.0", tk.END)
    output_textbox.insert(tk.END, sanitized_text)
