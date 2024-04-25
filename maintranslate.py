import tkinter as tk
from tkinter import ttk
from googletrans import Translator, LANGUAGES

# Main translation function
def translate_text():
    translator = Translator()
    translated = translator.translate(text_entry.get("1.0", tk.END), dest=language_var.get())
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, translated.text)

# Setup the GUI window
root = tk.Tk()
root.title("Language Translator")

# Configure layout
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# Text entry widget
text_entry = tk.Text(root, height=10)
text_entry.grid(row=0, column=0, pady=10, padx=10, sticky="ew")

# Language selection
language_var = tk.StringVar(root)
languages = list(LANGUAGES.values())
language_combo = ttk.Combobox(root, textvariable=language_var, values=languages)
language_combo.grid(row=1, column=0, pady=10, padx=10, sticky="ew")
language_combo.current(languages.index('english'))  # default to English

# Translate button
translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.grid(row=2, column=0, pady=10, padx=10, sticky="ew")

# Translation output widget
output_text = tk.Text(root, height=10)
output_text.grid(row=3, column=0, pady=10, padx=10, sticky="ew")

root.mainloop()
