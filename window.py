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
def start_progress(i=0): # doesn't freeze window when you start progress
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


hide_timer = {"id": None} # holder to cancel timers



def vault_screen():
    clear_root()
    root.title("The Vault")

    label = tk.Label(
        root,
        text="Saved Passwords",
        fg="green",
        bg="black",
        font=("Courier New", 20)
    )
    label.pack(pady=(30, 10))

    content = tk.Frame(root, bg="black")
    content.pack(fill='both', expand=True)

    enter_website = ("Courier New", 12)
    enter_website = tk.Label(
        content,
        text="Which password do you need?",
        fg="green",
        bg="black",
        font=enter_website
    )
    enter_website.pack(pady=(40, 10))

    search_var = tk.StringVar()
    search_entry = tk.Entry(content, textvariable=search_var, bg="darkgrey", width=20, show="*", font=("Courier New", 14))
    search_entry.pack(pady=(25, 50))

    footer = tk.Frame(root, bg="black")
    footer.pack(side='bottom', pady=20, anchor='s')

    back_button = tk.Button(footer, text="Back To Menu", fg="green", bg="black", height=2, width=15, font=("Courier New", 10), command=main_screen)
    back_button.pack()



# view passwords when button is pressed
def view_passwords():
    clear_root()
    root.title("View Passwords")

    label = tk.Label(
         root, 
         text="Saved Passwords", 
         fg="green", 
         bg="black", 
         font=("Courier New", 20)
    )
    label.pack(pady=(30, 10))

    content = tk.Frame(root, bg="black")
    content.pack(fill='both', expand=True)

    enter_pw = ("Courier New", 12)
    enter_pw = tk.Label(
         content, 
         text="Enter Ultra-Secure-Password to enter The Vault",
         fg="green",
         bg="black",
         font=enter_pw
    )
    enter_pw.pack(pady=(40, 10))

    search_var = tk.StringVar()
    search_entry = tk.Entry(content, textvariable=search_var, bg="darkgrey", width=20, show="*", font=("Courier New", 14))
    search_entry.pack(pady=(25, 50))
    search_entry.focus_set()

    error_label = tk.Label(
        content,
        text="",             
        fg="red",
        bg="black",
        font=("Courier New", 12)
    )



    def check_password(event=None):
        if hide_timer["id"] is not None:
            root.after_cancel(hide_timer["id"])
            hide_timer["id"] = None

        if search_var.get() == "Place":
            error_label.pack_forget()
            vault_screen()
        else:
            error_label.config(text="ACCESS DENIED")
            # show only once (if not already packed)
            if not error_label.winfo_ismapped():
                error_label.pack(pady=(0, 5))
            # auto-hide after 1500ms (optional)
            hide_timer["id"] = root.after(1500, lambda: error_label.pack_forget())
    
    search_entry.bind("<Return>", check_password)


    footer = tk.Frame(root, bg="black")
    footer.pack(side='bottom', pady=20, anchor='s')


    back_button = tk.Button(footer, text="Back To Menu", fg="green", bg="black", height=2, width=15, font=("Courier New", 10), command=main_screen)
    back_button.pack()



main_screen()
root.mainloop()

