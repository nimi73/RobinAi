import tkinter as tk
from tkinter import scrolledtext
from transformers import pipeline, set_seed, GPT2Tokenizer, GPT2Model

# Initialize GPT-2 medium model
set_seed(42)
tokenizer = GPT2Tokenizer.from_pretrained('gpt2-medium')
model = GPT2Model.from_pretrained('gpt2-medium')
generator = pipeline('text-generation', model=model, tokenizer=tokenizer)

def sanitize_data(text):
    prompt = f"Sanitize the following sensitive information and replace it with similar, but fake data, while keeping rest of the information exactly the same. Sensitive information which needs to be replaced, can be a company's name, a person's name, a database, server or application's name, a date, time, addresses, I.P. addresses, Port Numbers, keys, etc.:\n\n{text}\n\n---\n\nSanitized text:"

    generated_text = generator(prompt, max_length=1024, num_return_sequences=1)

    sanitized_text = generated_text[0]["generated_text"]
    return sanitized_text

def sanitize_button_click():
    input_text = input_textbox.get("1.0", "end-1c")
    sanitized_text = sanitize_data(input_text)
    output_textbox.delete("1.0", tk.END)
    output_textbox.insert(tk.END, sanitized_text)

# GUI Setup
root = tk.Tk()
root.title("Sensitive Data Sanitizer")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

input_label = tk.Label(frame, text="Input Text:")
input_label.pack()

input_textbox = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=80, height=10)
input_textbox.pack()

sanitize_button = tk.Button(frame, text="Sanitize Data", command=sanitize_button_click)
sanitize_button.pack(pady=10)

output_label = tk.Label(frame, text="Sanitized Output:")
output_label.pack()

output_textbox = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=80, height=10)
output_textbox.pack()

root.mainloop()
