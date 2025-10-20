import tkinter  as tk
from tkinter import ttk
import time

# root of the tkinter tree
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.configure(bg='black')


# progressbar widget
progress = ttk.Progressbar(
    root, 
    style="DarkGreen.Horizontal.TProgressbar", 
    orient="horizontal", 
    length=300, 
    mode="determinate",
    maximum=100
)
progress.pack(pady=55)


def start_progress(i=0): # doesnt freeze window when you start progress
    if i <= 100:
        progress['value'] = i
        root.after(15, start_progress, i + 1)


# progress bar style ???
style = ttk.Style()
style.theme_use('clam')
style.configure(
    "DarkGreen.Horizontal.TProgressbar", 
    background='#006400',             # fill color
    troughcolor='black',               # background (empty area)
    bordercolor="black",                # for the border to match the background
    lightcolor = "#006400",           # removes 3D shading effect
    darkcolor = "#006400"
)


# button for progress
start_button = tk.Button(root, text="Generate Password", command=start_progress)
start_button.pack(pady=45)


root.mainloop()

