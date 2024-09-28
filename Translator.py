import tkinter as tk
from tkinter import ttk, messagebox, Scrollbar, Frame

# Expanded translation dictionary
translation_dict = {
    "hello": {
        "Spanish": "hola",
        "French": "bonjour",
        "German": "hallo",
        "Italian": "ciao",
        "Portuguese": "olá"
    },
    "world": {
        "Spanish": "mundo",
        "French": "monde",
        "German": "Welt",
        "Italian": "mondo",
        "Portuguese": "mundo"
    },
    "goodbye": {
        "Spanish": "adiós",
        "French": "au revoir",
        "German": "auf Wiedersehen",
        "Italian": "arrivederci",
        "Portuguese": "adeus"
    },
    # More words...
}

class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Translator App")
        self.root.geometry("600x600")
        self.light_mode()

        # Title Label
        self.title_label = tk.Label(self.root, text="Mehtab's Translator", font=("Helvetica", 20), bg=self.bg_color, fg=self.fg_color)
        self.title_label.pack(pady=10)

        # Input Frame
        self.input_frame = Frame(self.root)
        self.input_frame.pack(pady=5)

        # Input Text Area with Scrollbar
        self.input_text_area = tk.Text(self.input_frame, height=10, width=50, bg=self.bg_color, fg=self.fg_color, font=("Arial", 12), borderwidth=2, relief="groove")
        self.input_text_area.grid(row=0, column=0)

        self.input_scroll = Scrollbar(self.input_frame, command=self.input_text_area.yview)
        self.input_scroll.grid(row=0, column=1, sticky='ns')
        self.input_text_area['yscrollcommand'] = self.input_scroll.set

        # Output Frame
        self.output_frame = Frame(self.root)
        self.output_frame.pack(pady=5)

        # Output Text Area with Scrollbar
        self.output_text_area = tk.Text(self.output_frame, height=10, width=50, bg=self.bg_color, fg=self.fg_color, font=("Arial", 12), borderwidth=2, relief="groove")
        self.output_text_area.grid(row=0, column=0)

        self.output_scroll = Scrollbar(self.output_frame, command=self.output_text_area.yview)
        self.output_scroll.grid(row=0, column=1, sticky='ns')
        self.output_text_area['yscrollcommand'] = self.output_scroll.set

        # Language Selection Dropdowns
        self.source_language = ttk.Combobox(self.root, values=["English", "Spanish", "French", "German", "Italian", "Portuguese"], font=("Arial", 12))
        self.source_language.set("Select Source Language")
        self.source_language.pack(pady=5)

        self.target_language = ttk.Combobox(self.root, values=["Spanish", "French", "German", "Italian", "Portuguese"], font=("Arial", 12))
        self.target_language.set("Select Target Language")
        self.target_language.pack(pady=5)

        # Style buttons
        self.button_style = {
            "font": ("Arial", 12),
            "padx": 10,
            "pady": 5,
            "relief": "raised",
            "borderwidth": 2
        }

        # Translate Button
        self.translate_button = tk.Button(self.root, text="Translate", command=self.translate, bg=self.btn_bg_color, fg=self.btn_fg_color, **self.button_style)
        self.translate_button.pack(pady=5)

        # Clear Button
        self.clear_button = tk.Button(self.root, text="Clear", command=self.clear, bg="#f44336", fg="white", **self.button_style)
        self.clear_button.pack(pady=5)

        # Dark/Light Mode Button
        self.toggle_button = tk.Button(self.root, text="Dark/Light Mode", command=self.toggle_mode, bg="#2196F3", fg="white", **self.button_style)
        self.toggle_button.pack(pady=5)

    def light_mode(self):
        self.bg_color = "#f0f0f0"
        self.fg_color = "#000000"
        self.btn_bg_color = "#4CAF50"
        self.btn_fg_color = "white"
        self.root.configure(bg=self.bg_color)

    def dark_mode(self):
        self.bg_color = "#2c2c2c"
        self.fg_color = "#ffffff"
        self.btn_bg_color = "#5cb85c"
        self.btn_fg_color = "white"
        self.root.configure(bg=self.bg_color)

    def toggle_mode(self):
        if self.bg_color == "#f0f0f0":
            self.dark_mode()
        else:
            self.light_mode()
        self.update_colors()

    def update_colors(self):
        self.title_label.configure(bg=self.bg_color, fg=self.fg_color)
        self.input_text_area.configure(bg=self.bg_color, fg=self.fg_color)
        self.output_text_area.configure(bg=self.bg_color, fg=self.fg_color)
        self.translate_button.configure(bg=self.btn_bg_color, fg=self.btn_fg_color)
        self.clear_button.configure(bg="#f44336", fg="white")
        self.toggle_button.configure(bg="#2196F3", fg="white")

        # Update dropdown colors
        self.source_language.configure(bg=self.bg_color, fg=self.fg_color)
        self.target_language.configure(bg=self.bg_color, fg=self.fg_color)

    def translate(self):
        input_text = self.input_text_area.get("1.0", tk.END).strip().lower()
        target_lang = self.target_language.get()
        
        if not input_text:
            messagebox.showwarning("Input Error", "Please enter text to translate.")
            return
        
        translated_text = []
        
        for word in input_text.split():
            translated_word = translation_dict.get(word, {}).get(target_lang, word)
            translated_text.append(translated_word)

        self.output_text_area.delete("1.0", tk.END)
        self.output_text_area.insert(tk.END, ' '.join(translated_text))

    def clear(self):
        self.input_text_area.delete("1.0", tk.END)
        self.output_text_area.delete("1.0", tk.END)

# Initialize the main window
root = tk.Tk()
app = TranslatorApp(root)

# Start the main loop
root.mainloop()
