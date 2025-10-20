import tkinter  as tk
from tkinter import ttk
import time

def start_progress():
    progress.start()

    for i in range(101):
        # for 'estheticz'
        time.sleep(0.015)
        progress['value'] = i
        root.update_idletasks()
    progress.stop()

root = tk.Tk()
root.title("Place")

# progressbar widget
progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress.pack(pady=20)

# button for progress
start_button = tk.Button(root, text="Start Progress", command=start_progress)
start_button.pack(pady=10)
root.mainloop()

