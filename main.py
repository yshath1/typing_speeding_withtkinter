import tkinter as tk
import requests
import time


class TypingSpeed:
    def __init__(self):
        self.bs_text = ""
        self.displayed_text = ""
        self.typed_chars = 0
        self.start = 0
        self.stop = 0
        self.incorrect = True

    def get_sample_text(self):
        """Gets the text to be displayed via https://github.com/sameerkumar18/corporate-bs-generator-api"""
        response = requests.get(url="https://corporatebs-generator.sameerkumar.website/")
        self.bs_text = response.json()["phrase"]
        return self.bs_text

    def display_text_and_entry(self):
        """Starts the timer and displays the text to be entered when Enter is pressed.
        Text color changes to red if there is a typo."""
        if self.start == 0:
            self.start = time.time()
        if self.displayed_text == "" or self.displayed_text == text_entry.get():
            self.typed_chars += len(text_entry.get())
            self.displayed_text = self.get_sample_text()
            text_display.config(text=self.displayed_text, fg="black")
            text_entry.delete(0, "end")
            text_entry.config(width=len(self.displayed_text))
            text_entry.grid(column=1, row=1, sticky="w")
            self.incorrect = False
            text_entry.focus()
        else:
            text_display.config(fg="red")
            self.incorrect = True

    def stop_typing(self):
        """Stops the timer when ESC is pressed and displays the results."""
        self.stop = time.time()
        if (self.incorrect == False and self.typed_chars != 0) or self.displayed_text == text_entry.get():
            self.typed_chars += len(text_entry.get())
        time_diff = self.stop - self.start
        text_display.config(text=f"Typed in {self.typed_chars} characters in {time_diff:.4} seconds.\n"
                                 f"This means your typing speed is {(self.typed_chars / time_diff):.2} chars a second.")


typing = TypingSpeed()
window = tk.Tk()
window.config(padx=20, pady=20)
window.title("Typing speed")
window.bind('<Return>', lambda event: typing.display_text_and_entry())
window.bind('<Escape>', lambda event: typing.stop_typing())
text_display = tk.Label(text="Press Enter to start\n"
                             "To submit the text and get a new press Enter\n"
                             "If the text changes to red there is a typo\n"
                             "To finish press ESC")
text_display.grid(column=1, row=0)
text_entry = tk.Entry(window)

window.mainloop()