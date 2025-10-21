import tkinter  as tk
from tkinter import ttk
from vault import get_password, set_password, delete_password
from generate import generate_password


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
    background='#006400',             
    troughcolor='black',                
    bordercolor="black",          
    lightcolor = "#006400",           
    darkcolor = "#006400"
)


progress = None




def generate_screen():
    clear_root()
    root.title("Security Types")

    main_frame = tk.Frame(root, bg="black")
    main_frame.pack(expand=True, fill="both")

    prompt_label = tk.Label(
        main_frame,
        text="What Security Type",
        bg="black",
        fg="darkgreen",
        font=("Courier New", 20)
    )
    prompt_label.pack(pady=((50, 15)))

    prompt_label2 = tk.Label(
        main_frame,
        text="Would You Like?",
        bg="black",
        fg="darkgreen",
        font=("Courier New", 20)
    )
    prompt_label2.pack(pady=((20, 5)))

    button_section = tk.Frame(main_frame, bg="black")
    button_section.pack(side="bottom", pady=30, anchor='s')  

    top_buttons = tk.Frame(button_section, bg="black")
    top_buttons.pack(pady=(0, 8))

    low_btn = tk.Button(top_buttons, text="Low Security", fg="darkgreen", bg="black",
                        width=15, height=2, command=low_sec)
    low_btn.pack(side="left", padx=20)

    med_btn = tk.Button(top_buttons, text="Medium Security", fg="darkgreen", bg="black",
                        width=15, height=2, command=low_sec)
    med_btn.pack(side="right", padx=20)

    high_btn = tk.Button(button_section, text="High Security", fg="darkgreen", bg="black",
                         width=12, pady=10, command=low_sec)
    high_btn.pack(pady=(10, 0))

    footer = tk.Frame(root, bg="black")
    footer.pack(side="bottom", pady=25, anchor='s')  

    back_button = tk.Button(
        footer,
        text="Back To Menu",
        fg="green",
        bg="black",
        height=2,
        width=15,
        font=("Courier New", 10),
        command=main_screen
    )
    back_button.pack()




def low_sec():
    clear_root()
    root.title("Low Security Types")

    main_frame = tk.Frame(root, bg="black")
    main_frame.pack(expand=True, fill="both")

    prompt_label = tk.Label(
        main_frame,
        text="Low Security Types",
        bg="black",
        fg="darkgreen",
        font=("Courier New", 20)
    )
    prompt_label.pack(pady=((50, 15)))

    prompt_label2 = tk.Label(
        main_frame,
        text="Which Option Will You Pick?",
        bg="black",
        fg="darkgreen",
        font=("Courier New", 20)
    )
    prompt_label2.pack(pady=((20, 5)))

    button_section = tk.Frame(main_frame, bg="black")
    button_section.pack(side="bottom", pady=30, anchor='s')  

    top_buttons = tk.Frame(button_section, bg="black")
    top_buttons.pack(pady=(0, 8))

    letters_only_btn = tk.Button(top_buttons, text="Letters Only", fg="darkgreen", bg="black",
                        width=15, height=2, command=letters_only)
    letters_only_btn.pack(side="left", padx=20)

    alphanumeric_btn = tk.Button(top_buttons, text="Alphanumeric", fg="darkgreen", bg="black",
                        width=15, height=2, command=letters_only) # alphanumeric
    alphanumeric_btn.pack(side="right", padx=20)

    footer = tk.Frame(root, bg="black")
    footer.pack(side="bottom", pady=25, anchor='s')  

    back_button = tk.Button(
        footer,
        text="Back To Menu",
        fg="green",
        bg="black",
        height=2,
        width=15,
        font=("Courier New", 10),
        command=main_screen
    )
    back_button.pack()




def letters_only():
    clear_root()
    root.title("Letters Only")

    tk.Label(
        root,
        text="Letters Only",
        fg="green",
        bg="black",
        font=("Courier New", 28)
    ).pack(pady=(50, 10))

    password = generate_password("Letters Only")
    pw_font=("Courier New", 18)
    
    tk.Label(
        root,
        text="Generated Password: ",
        fg="lime",
        bg="black",
        font=pw_font
    ).pack(pady=(50, 10))

    tk.Label(
        root,
        text=password,
        fg="lime",
        bg="black",
        font=pw_font
    ).pack(pady=(10))

    back_button = tk.Button(
        root,
        text="Back To Menu",
        fg="green",
        bg="black",
        height=2,
        width=15,
        font=("Courier New", 10),
        command=main_screen
    )
    back_button.pack()




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




def add_update_screen():
    clear_root()
    root.title("Add / Update Password")

    # Title
    tk.Label(root, text="Add / Update Password",
             fg="green", bg="black", font=("Courier New", 20)).pack(pady=(30, 10))

    content = tk.Frame(root, bg="black")
    content.pack(fill="both", expand=True, padx=20)

    # Site name
    tk.Label(content, text="Website / Service name:",
             fg="green", bg="black", font=("Courier New", 12)).pack(pady=(10, 4))
    site_var = tk.StringVar()
    site_entry = tk.Entry(content, textvariable=site_var, bg="darkgrey",
                          width=24, font=("Courier New", 14))
    site_entry.pack(pady=(0, 12))
    site_entry.focus_set()

    # Password (masked)
    tk.Label(content, text="Password:",
             fg="green", bg="black", font=("Courier New", 12)).pack(pady=(6, 4))
    pwd_var = tk.StringVar()
    pwd_entry = tk.Entry(content, textvariable=pwd_var, bg="darkgrey",
                         width=24, font=("Courier New", 14))
    pwd_entry.pack(pady=(0, 12))

    site_entry.bind("<Return>", lambda e: pwd_entry.focus_set())
    root.bind("<Escape>", lambda e: main_screen())

    # Result / status
    status = tk.Label(content, text="", fg="lime", bg="black", font=("Courier New", 12))
    status.pack(pady=(6, 8))



    def save_password(event=None):
        site_raw = site_var.get().strip()
        site_key = site_raw.lower()
        if not site_raw:
            status.config(text="Please enter a website name", fg="yellow")
            return
        pwd = pwd_var.get()
        if pwd == "":
            status.config(text="Please enter a password", fg="yellow")
            return

        # store (your vault.set_password normalizes lower/strip already; if not, do site_raw.lower())
        set_password(site_key, pwd)
        status.config(text=f"Saved password for {site_raw}", fg="lime")
        # Optional: clear fields or return to main
        # site_var.set(""); pwd_var.set("")
        # main_screen()


    # Bind Enter on the password field to save
    pwd_entry.bind("<Return>", save_password)


    # Buttons row
    btn_row = tk.Frame(root, bg="black")
    btn_row.pack(side="bottom", pady=20, anchor="s")

    tk.Button(btn_row, text="Save", fg="darkgreen", bg="black",
              width=12, command=save_password).pack(side="left", padx=10)

    tk.Button(btn_row, text="Back To Menu", fg="green", bg="black",
              width=15, command=main_screen).pack(side="left", padx=10)




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


    button_section = tk.Frame(root, bg="black")
    button_section.pack(side='bottom', pady=120, anchor='s')

    top_buttons = tk.Frame(button_section, bg="black")
    top_buttons.pack(pady=(0, 10))

    # two side-by-side buttons
    view_pw = tk.Button(top_buttons, text="View Passwords", fg="darkgreen", bg="black", width=15, height=2, command=view_passwords)
    view_pw.pack(side="left", padx=20)

    start_button = tk.Button(top_buttons, text="Generate Password", fg="darkgreen", bg="black", width=15, height=2, command=generate_screen)
    start_button.pack(side="right", padx=20)

    # centered Add/Update button below them
    add_update_btn = tk.Button(button_section, text="Add / Update Website or Password", fg="darkgreen", bg="black", width=30, pady=55, command=add_update_screen)
    add_update_btn.pack(pady=(.5, 0))


    progress = ttk.Progressbar(
        root, 
        style="DarkGreen.Horizontal.TProgressbar", 
        orient="horizontal", 
        length=300, 
        mode="determinate",
        maximum=100
    )
    progress.pack(pady=15)
    root.bind("<Escape>", lambda e: root.destroy())


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
    search_entry = tk.Entry(content, textvariable=search_var, bg="darkgrey", width=20, font=("Courier New", 14))
    search_entry.pack(pady=(25, 50))
    search_entry.focus_set()

    result_label = tk.Label(content, text='', fg="lime", bg="black", font=("Courier New", 12))
    result_label.pack(pady=(0, 10))
    root.unbind("<Escape>")



    def on_query_enter(event=None):
        site = search_var.get()
        key = site.strip().lower()

        if not key:
            result_label.config(text="Please enter a website where you have a password", fg="yellow")
            return

        
        pwd = get_password(key)

        if pwd:
            result_label.config(text=f"Password for {site}: {pwd}", fg="lime")
            # copy to clipboard, check to see if useful or not
            root.clipboard_clear()
            root.clipboard_append(pwd)
            root.update()
        else:
            result_label.config(text="Password not found for this website", fg="red")

    search_entry.bind("<Return>", on_query_enter)

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

    root.unbind("<Escape>")




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

