import tkinter as tk
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
        self.root.geometry("850x500")
        self.root.config(bg="#f0f4f7")
        self.root.resizable(False, False)

        self.show_welcome_screen()

    def show_welcome_screen(self):
        self.welcome_frame = tk.Frame(self.root, bg="#f0f4f7")
        self.welcome_frame.pack(fill="both", expand=True)

        tk.Label(self.welcome_frame, text="VSB ENGINEERING COLLEGE",
                 font=("Helvetica", 24, "bold"), fg="#1a237e", bg="#f0f4f7").pack(pady=20)

        tk.Label(self.welcome_frame, text="Welcome to Typing Speed Tester",
                 font=("Helvetica", 20), bg="#f0f4f7").pack(pady=10)

        tk.Label(self.welcome_frame,
                 text="Click the button below to start your typing test.\nTry to type accurately and quickly!",
                 font=("Arial", 14), bg="#f0f4f7").pack(pady=20)

        tk.Button(self.welcome_frame, text="Start Test", font=("Arial", 16),
                  bg="#4caf50", fg="white", padx=20, pady=10, command=self.show_typing_test).pack(pady=30)

    def show_typing_test(self):
        self.welcome_frame.destroy()

        self.sample_text = random.choice(sample_texts)
        self.start_time = None
        self.end_time = None

        # Typing Test Frame
        self.test_frame = tk.Frame(self.root, bg="#ffffff", padx=20, pady=20)
        self.test_frame.pack(fill="both", expand=True)

        tk.Label(self.test_frame, text="Typing Test", font=("Helvetica", 18, "bold"),
                 bg="#ffffff", fg="#333333").pack(pady=10)

        tk.Label(self.test_frame, text="Type this:", font=("Arial", 14), bg="#ffffff").pack(anchor="w")
        self.sample_label = tk.Label(self.test_frame, text=self.sample_text, wraplength=750,
                                     font=("Arial", 13), bg="#f9f9f9", fg="#555555", justify="left",
                                     relief="solid", padx=10, pady=10)
        self.sample_label.pack(pady=5, fill="x")

        self.text_entry = tk.Text(self.test_frame, height=6, font=("Arial", 13),
                                  wrap="word", relief="sunken", bd=2)
        self.text_entry.pack(pady=10, fill="x")
        self.text_entry.bind("<KeyPress>", self.start_typing)

        # Results Display
        self.result_label = tk.Label(self.test_frame,
                                     text="Start typing above to begin.",
                                     font=("Helvetica", 14),
                                     fg="#2e7d32", bg="#e8f5e9", pady=10, padx=10,
                                     anchor="center", relief="ridge")
        self.result_label.pack(pady=10, fill="x")

        # Buttons
        button_frame = tk.Frame(self.test_frame, bg="#ffffff")
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Reset", font=("Arial", 12),
                  bg="#f44336", fg="white", padx=15,
                  command=self.reset).pack()

    def start_typing(self, event):
        if self.start_time is None:
            self.start_time = time.time()
            self.text_entry.bind("<Return>", self.calculate_results)

    def calculate_results(self, event=None):
        self.end_time = time.time()
        if event:
            event.widget.mark_set("insert", "insert-1c")  # Prevent newline

        typed_text = self.text_entry.get("1.0", tk.END).strip()
        total_time = round(self.end_time - self.start_time, 2)
        total_time = max(total_time, 0.01)  # Avoid divide-by-zero

        word_count = len(typed_text.split())
        wpm = round((word_count / total_time) * 60, 2)

        correct_chars = sum(1 for i, c in enumerate(typed_text)
                            if i < len(self.sample_text) and c == self.sample_text[i])
        accuracy = round((correct_chars / len(self.sample_text)) * 100, 2)

        self.result_label.config(
            text=f"⏱ Time: {total_time}s    |    📄 WPM: {wpm}    |    ✅ Accuracy: {accuracy}%",
            fg="#1b5e20", bg="#dcedc8"
        )

        self.text_entry.unbind("<KeyPress>")
        self.text_entry.unbind("<Return>")
        return "break"

    def reset(self):
        self.sample_text = random.choice(sample_texts)
        self.sample_label.config(text=self.sample_text)
        self.start_time = None
        self.end_time = None
        self.text_entry.delete("1.0", tk.END)
        self.result_label.config(text="Start typing above to begin.",
                                 fg="#2e7d32", bg="#e8f5e9")
        self.text_entry.bind("<KeyPress>", self.start_typing)

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTester(root)
    root.mainloop()
