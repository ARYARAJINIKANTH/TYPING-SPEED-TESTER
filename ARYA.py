import tkinter as tk
from tkinter import messagebox
import time
import random

sample_texts = [
    "The quick brown fox jumps over the lazy dog.",
    "Typing is a fundamental skill that is useful in many jobs.",
    "Practice makes perfect, especially when it comes to typing.",
    "Python is a great language for building a variety of applications.",
    "Artificial Intelligence is changing the way we interact with technology.",
    "A journey of a thousand miles begins with a single step.",
    "Keep your face always toward the sunshine—and shadows will fall behind you.",
    "Success usually comes to those who are too busy to be looking for it.",
    "Typing fast and accurately is a valuable skill in the digital world."
]

class TypingSpeedTester:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Tester")
        self.root.geometry("800x400")
        self.root.resizable(False, False)

        self.sample_text = random.choice(sample_texts)
        self.start_time = None
        self.end_time = None

        self.text_label = tk.Label(root, text="Type this:", font=("Arial", 16))
        self.text_label.pack(pady=10)

        self.sample_label = tk.Label(root, text=self.sample_text, wraplength=700, font=("Arial", 14), fg="gray")
        self.sample_label.pack(pady=5)

        self.text_entry = tk.Text(root, height=6, font=("Arial", 14), wrap="word")
        self.text_entry.pack(pady=10)
        self.text_entry.bind("<KeyPress>", self.start_typing)

        
        self.result_frame = tk.Frame(root, bg="#e0ffe0", bd=2, relief="groove")
        self.result_frame.pack(pady=10, padx=20, fill="x")

        self.result_label = tk.Label(
            self.result_frame,
            text="",
            font=("Helvetica", 16, "bold"),
            fg="#004d00",
            bg="#e0ffe0",
            pady=10,
            anchor="center"
        )
        self.result_label.pack(fill="x")


        self.reset_button = tk.Button(root, text="Reset", font=("Arial", 12), command=self.reset)
        self.reset_button.pack(pady=5)

    def start_typing(self, event):
        if self.start_time is None:
            self.start_time = time.time()
            self.text_entry.bind("<Return>", self.calculate_results)

    def calculate_results(self, event=None):
        self.end_time = time.time()
        typed_text = self.text_entry.get("1.0", tk.END).strip()

        total_time = round(self.end_time - self.start_time, 2)
        word_count = len(typed_text.split())
        wpm = round((word_count / total_time) * 60, 2)

        correct_chars = sum(1 for i, c in enumerate(typed_text)
                            if i < len(self.sample_text) and c == self.sample_text[i])
        accuracy = round((correct_chars / len(self.sample_text)) * 100, 2)

        self.result_label.config(
            text=f"⏱ Time: {total_time}s    |    📄 WPM: {wpm}    |    ✅ Accuracy: {accuracy}%",
            fg="#004d00"
        )


        self.text_entry.unbind("<KeyPress>")
        self.text_entry.unbind("<Return>")

    def reset(self):
        self.sample_text = random.choice(sample_texts)
        self.sample_label.config(text=self.sample_text)
        self.start_time = None
        self.end_time = None
        self.text_entry.delete("1.0", tk.END)
        self.result_label.config(text="")
        self.text_entry.bind("<KeyPress>", self.start_typing)

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTester(root)
    root.mainloop()
