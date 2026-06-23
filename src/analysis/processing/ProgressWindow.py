import tkinter as tk
from tkinter import ttk
import time

class ProgressWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Log Analysis")
        self.window.geometry("450x150")
        self.window.resizable(False, False)

        self.start_time = time.time()
        self.running = True

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

        self._update_timer()

        self.window.lift()
        self.window.focus_force()

    def _update_timer(self):
        if not self.running:
            return

        elapsed = int(time.time() - self.start_time)

        minutes = elapsed // 60
        seconds = elapsed % 60

        self.time_label.config(
            text=f"Elapsed time: {minutes:02}:{seconds:02}"
        )

        self.window.after(
            1000,
            self._update_timer
        )

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

    def close(self):
        self.running = False

        self.status_label.config(
            text="Analysis Complete"
        )

        self.window.after(
            500,
            self.window.destroy
        )