# window.py (gui)

import tkinter  as tk
from tkinter import ttk
import time
# import main

# root of the tkinter tree
root = tk.Tk()
root.title("Password Generator")
root.geometry("500x500")
root.configure(bg='black')


# title
title_text = ("Courier New", 25)
title_label = tk.Label(
    root, 
    text="PassWord Generator",
    fg="green",
    bg="black",
    font=title_text
)
title_label.pack(pady=20)


# progressbar widget
progress = ttk.Progressbar(
    root, 
    style="DarkGreen.Horizontal.TProgressbar", 
    orient="horizontal", 
    length=300, 
    mode="determinate",
    maximum=100
)
progress.pack(pady=95)


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
    troughcolor='black',                # background (empty area)
    bordercolor="black",                # for the border to match the background
    lightcolor = "#006400",           # removes 3D shading effect
    darkcolor = "#006400"
)


# view passwords button
view_pw = tk.Button(
    root, 
    text="View Passwords", 
    fg="darkgreen",
    bg="black",
    command=start_progress,
)
view_pw.pack(side="left", padx=55, pady=35)


# generate password button
start_button = tk.Button(root, 
    text="Generate Password", 
    fg="darkgreen",
    bg="black",
    command=start_progress,
)
start_button.pack(side="right", padx=55, pady=35)


root.mainloop()

