import tkinter as tk
from tkinter import messagebox, scrolledtext

from generate import generate_headlines

def on_generate():
    idea = idea_entry.get("1.0", tk.END).strip()
    platform = platform_var.get()
    if not idea:
        messagebox.showwarning("Input Required", "Please enter your raw idea.")
        return
    if not platform:
        messagebox.showwarning("Platform Required", "Please select a platform.")
        return
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, "Generating headlines...\n")
    root.update()
    headlines = generate_headlines(idea, platform)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, headlines)

root = tk.Tk()
root.title("Headline Generator 🧠✍️")
root.geometry("520x420")

frame = tk.Frame(root, padx=16, pady=16)
frame.pack(fill=tk.BOTH, expand=True)

title_label = tk.Label(frame, text="Enter your raw idea:", font=("Arial", 12, "bold"))
title_label.pack(anchor="w")


idea_entry = scrolledtext.ScrolledText(frame, height=4, font=("Arial", 11))
idea_entry.pack(fill=tk.X, pady=(0, 10))

# Platform dropdown
platform_label = tk.Label(frame, text="Select platform:", font=("Arial", 11))
platform_label.pack(anchor="w")
platform_var = tk.StringVar(value="Linkedin")
platform_options = ["Linkedin", "Facebook", "Instagram", "X (Twitter)"]
platform_menu = tk.OptionMenu(frame, platform_var, *platform_options)
platform_menu.config(font=("Arial", 11))
platform_menu.pack(fill=tk.X, pady=(0, 10))

generate_btn = tk.Button(frame, text="Generate Headlines", font=("Arial", 11, "bold"), command=on_generate)
generate_btn.pack(pady=(0, 10))

output_label = tk.Label(frame, text="Generated Headlines:", font=("Arial", 12, "bold"))
output_label.pack(anchor="w")

output_text = scrolledtext.ScrolledText(frame, height=7, font=("Arial", 11))
output_text.pack(fill=tk.BOTH, expand=True)

root.mainloop()
