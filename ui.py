import tkinter as tk
from tkinter import messagebox, scrolledtext
from tkinter import ttk

from generate import generate_headlines, parse_output, save_to_csv

def center_window(win, width, height):
    win.update_idletasks()
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    win.geometry(f"{width}x{height}+{x}+{y}")

def on_generate():
    idea = idea_entry.get("1.0", tk.END).strip()
    platform = platform_var.get()
    if not idea:
        messagebox.showwarning("Input Required", "Please enter your raw idea.")
        return
    if not platform:
        messagebox.showwarning("Platform Required", "Please select a platform.")
        return
    output_text.config(state="normal")
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, "Generating headlines...\n")
    root.update()
    headlines = generate_headlines(idea, platform)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, headlines)
    output_text.config(state="disabled")
    # Save to CSV
    headline, post, hashtags = parse_output(headlines)
    save_to_csv(idea, platform, headline, post, hashtags)

root = tk.Tk()
root.title("Headline Generator 🧠✍️")
window_width, window_height = 560, 480
center_window(root, window_width, window_height)
root.configure(bg="#f6f8fa")

style = ttk.Style()
style.theme_use("clam")
style.configure("TFrame", background="#f6f8fa")
style.configure("TLabel", background="#f6f8fa", font=("Segoe UI", 11))
style.configure("Header.TLabel", font=("Segoe UI", 16, "bold"), foreground="#22223b", background="#f6f8fa")
style.configure("TButton", font=("Segoe UI", 11, "bold"), padding=6)
style.configure("TMenubutton", font=("Segoe UI", 11), padding=4)
style.configure("Card.TFrame", background="#ffffff", relief="groove", borderwidth=1)

main_frame = ttk.Frame(root, padding=24, style="TFrame")
main_frame.pack(fill=tk.BOTH, expand=True)

# Header
header_frame = ttk.Frame(main_frame, style="TFrame")
header_frame.pack(fill=tk.X, pady=(0, 18))
icon_label = ttk.Label(header_frame, text="🧠✍️", font=("Segoe UI Emoji", 22), style="TLabel")
icon_label.pack(side=tk.LEFT, padx=(0, 8))
header_label = ttk.Label(header_frame, text="Headline Generator", style="Header.TLabel")
header_label.pack(side=tk.LEFT)

# Card-like container for input
card = ttk.Frame(main_frame, padding=18, style="Card.TFrame")
card.pack(fill=tk.BOTH, expand=False, pady=(0, 18))

title_label = ttk.Label(card, text="Raw Idea", font=("Segoe UI", 11, "bold"))
title_label.pack(anchor="w", pady=(0, 4))

idea_entry = scrolledtext.ScrolledText(card, height=4, font=("Segoe UI", 11), wrap=tk.WORD, relief="solid", borderwidth=1)
idea_entry.pack(fill=tk.X, pady=(0, 12))

platform_label = ttk.Label(card, text="Platform", font=("Segoe UI", 11, "bold"))
platform_label.pack(anchor="w", pady=(0, 4))

platform_var = tk.StringVar(value="Linkedin")
platform_options = ["Linkedin", "Facebook", "Instagram", "X (Twitter)"]
platform_menu = ttk.OptionMenu(card, platform_var, platform_options[0], *platform_options)
platform_menu.pack(fill=tk.X, pady=(0, 12))

generate_btn = ttk.Button(card, text="Generate Headlines", command=on_generate)
generate_btn.pack(pady=(0, 2), fill=tk.X)

# Output section
output_label = ttk.Label(main_frame, text="Generated Headlines", font=("Segoe UI", 12, "bold"))
output_label.pack(anchor="w", pady=(0, 4))

output_text = scrolledtext.ScrolledText(main_frame, height=8, font=("Segoe UI", 11), wrap=tk.WORD, relief="solid", borderwidth=1, state="disabled")
output_text.pack(fill=tk.BOTH, expand=True)

root.mainloop()
