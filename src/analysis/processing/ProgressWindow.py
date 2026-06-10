import tkinter as tk
from tkinter import ttk
import time

class ProgressWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Log Analysis")
        self.window.geometry("500x200")
        self.window.resizable(False, False)

        # Timer
        self.start_time = time.time()
        self.time_label = tk.Label(
            self.window,
            text="Elapsed time: 00:00"
        )
        self.time_label.pack()

        self.status_label = tk.Label(
            self.window,
            text="Starting analysis..."
        )
        self.status_label.pack(pady=10)

        self.file_label = tk.Label(
            self.window,
            text=""
        )
        self.file_label.pack()

        self.progress = ttk.Progressbar(
            self.window,
            orient="horizontal",
            length=400,
            mode="determinate"
        )
        self.progress.pack(pady=15)
        
        self.window.update()
        self.window.lift()
        self.window.focus_force()

    def update_progress(
        self,
        current,
        total,
        filename
    ):
        self.progress["maximum"] = total
        self.progress["value"] = current

        self.status_label.config(
            text=f"Processing file {current}/{total}"
        )

        self.file_label.config(
            text=filename
        )

        # Update Timer
        elapsed = int(time.time() - self.start_time)

        minutes = elapsed // 60
        seconds = elapsed % 60

        self.time_label.config(
            text=f"Elapsed time: {minutes:02}:{seconds:02}"
        )

        self.window.update()

    def close(self):
        self.status_label.config(
            text="Analysis Complete"
        )

        self.window.update()
        self.window.after(500)

        self.window.destroy()