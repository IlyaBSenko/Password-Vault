# window.py (gui)

import tkinter  as tk
from tkinter import ttk
# import main


# root of the tkinter tree
root = tk.Tk()
root.title("Password Generator")
root.geometry("500x500")
root.configure(bg='black')


# progress bar style 
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


progress = None


# progress bar animation
def start_progress(i=0): # doesnt freeze window when you start progress
    if not isinstance(progress, ttk.Progressbar) or not progress.winfo_exists():
        return
     
    if i <= 100:
        progress['value'] = i
        root.after(15, start_progress, i + 1)
    else:
        progress.pack_forget()
        progress['value'] = 0
        progress.pack(pady=95)
    


# clear window
def clear_root():
    for widget in root.winfo_children():
            widget.destroy()



# remake main window when back button is pressed
def main_screen():
    global progress
    clear_root()

    root.title("Password Generator")

    # title
    title_text = ("Courier New", 30)
    title_label = tk.Label(
        root, 
        text="PassWord Generator",
        fg="green",
        bg="black",
        font=title_text
    )
    title_label.pack(pady=20)

    prompt_text = ("Courier New", 18)
    prompt_text = tk.Label(
         root, 
         text="What would you like to do?",
         fg="green",
         bg="black",
         font=prompt_text
    )
    prompt_text.pack(pady=30)


    button_row = tk.Frame(root, bg="black")
    button_row.pack(side='bottom', pady=150, anchor='s')


    # view passwords button
    view_pw = tk.Button(button_row, text="View Passwords", fg="darkgreen", bg="black", width=15, height=2, command=view_passwords)
    view_pw.pack(side="left", padx=30)


    # generate password button
    start_button = tk.Button(button_row, text="Generate Password", fg="darkgreen", bg="black", width=15, height=2, command=start_progress)
    start_button.pack(side="right", padx=30)

    progress = ttk.Progressbar(
        root, 
        style="DarkGreen.Horizontal.TProgressbar", 
        orient="horizontal", 
        length=300, 
        mode="determinate",
        maximum=100
    )
    progress.pack(pady=15)



# view passwords when button is pressed
def view_passwords():
    clear_root()
    root.title("View Passwords")

    label = tk.Label(root, text="Saved Passwords", fg="green", bg="black", font=("Courier New", 20))
    label.pack(pady=30)

    back_button = tk.Button(root, text="Back", fg="green", bg="black", font=("Courier New", 20), command=main_screen)
    back_button.pack(pady=20)



main_screen()
root.mainloop()

