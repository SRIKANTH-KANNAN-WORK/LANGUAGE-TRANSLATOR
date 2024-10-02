import tkinter as tk
from tkinter import ttk
from googletrans import Translator

def translate_text():
    input_text = input_entry.get("1.0", "end-1c")
    source_lang = source_lang_combobox.get()
    target_lang = target_lang_combobox.get()
    
    translator = Translator()
    translated_text = translator.translate(input_text, src=source_lang, dest=target_lang)
    
    output_entry.delete("1.0", "end")
    output_entry.insert("1.0", translated_text.text)

root = tk.Tk()
root.title("AI-powered Language Translator")
root.geometry("550x350")
root.configure(bg="#000000")

style = ttk.Style()
style.theme_use("clam")

# Pure black mode colors
background_color = "#000000"
foreground_color = "#ffffff"
button_background_color = "#00FF00"  
button_foreground_color = "#000000"
entry_background_color = "#333333"
entry_foreground_color = "#ffffff"


style.configure("Title.TLabel", font=("Helvetica", 16, "bold"), background=background_color, foreground=foreground_color)
style.configure("Label.TLabel", font=("Helvetica", 12), background=background_color, foreground=foreground_color)
style.configure("TButton", font=("Helvetica", 12, "bold"), background=button_background_color, foreground=button_foreground_color)
style.configure("TCombobox", fieldbackground=entry_background_color, background=entry_background_color, foreground=entry_foreground_color)

title_label = ttk.Label(root, text="AI-powered Language Translator", style="Title.TLabel")
title_label.grid(row=0, column=1, columnspan=3, padx=10, pady=20, sticky="n")

input_label = ttk.Label(root, text="Enter text:", style="Label.TLabel")
input_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
input_entry = tk.Text(root, height=5, width=50, font=("Helvetica", 12), bg=entry_background_color, fg=entry_foreground_color)
input_entry.grid(row=1, column=1, columnspan=3, padx=10, pady=5)

source_lang_label = ttk.Label(root, text="Source Language:", style="Label.TLabel")
source_lang_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
source_lang_combobox = ttk.Combobox(root, values=["English"], font=("Helvetica", 12))
source_lang_combobox.grid(row=2, column=1, padx=10, pady=5, sticky="w")
source_lang_combobox.set("English")  # Set default value

target_lang_label = ttk.Label(root, text="Target Language:", style="Label.TLabel")
target_lang_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
target_lang_combobox = ttk.Combobox(root, values=["Tamil", "Malayalam","Hindi","Telugu","Kannada","Spanish","French"], font=("Helvetica", 12))
target_lang_combobox.grid(row=3, column=1, padx=10, pady=5, sticky="w")
target_lang_combobox.set("Tamil")  # Set default value

translate_button = ttk.Button(root, text="Translate", command=translate_text, style="TButton")
translate_button.grid(row=4, column=1, padx=10, pady=5, sticky="w")

output_label = ttk.Label(root, text="Translated text:", style="Label.TLabel")
output_label.grid(row=5, column=0, padx=10, pady=5, sticky="e")
output_entry = tk.Text(root, height=5, width=50, font=("Helvetica", 12), bg=entry_background_color, fg=entry_foreground_color)
output_entry.grid(row=5, column=1, columnspan=3, padx=10, pady=5)

root.mainloop()


