import tkinter as tk
from tkinter import ttk
from vault import get_password, set_password, delete_password
from generate import generate_password


root = tk.Tk()
root.title("Password Generator")
root.geometry("500x500")
root.configure(bg="black")


style = ttk.Style()
style.theme_use("clam")
style.configure(
    "DarkGreen.Horizontal.TProgressbar",
    background="#006400",
    troughcolor="black",
    bordercolor="black",
    lightcolor="#006400",
    darkcolor="#006400",
)


progress = None
hide_timer = {"id": None}  



def clear_root():
    for widget in root.winfo_children():
        widget.destroy()



def start_progress(bar: ttk.Progressbar, i: int = 0, on_done=None):
    if bar is None or not bar.winfo_exists():
        return

    if i <= 100:
        bar["value"] = i
        root.after(15, start_progress, bar, i + 1, on_done)

    else:
        if callable(on_done):
            on_done()



# display helpers
def show_generated(kind: str):
    clear_root()
    root.title(kind)

    tk.Label(root, text=kind, fg="green", bg="black",
             font=("Courier New", 28)).pack(pady=(30, 10))

    status = tk.Label(root, text="Generating Password...", fg="lime",
                      bg="black", font=("Courier New", 18))
    status.pack(pady=(10, 10))

    bar = ttk.Progressbar(
        root,
        style="DarkGreen.Horizontal.TProgressbar",
        orient="horizontal",
        length=300,
        mode="determinate",
        maximum=100,
    )
    bar.pack(pady=(5, 20))

    
    try:
        password = generate_password(kind)
    except Exception as e:
        password = f"Error: {e}"

    pw_label = tk.Label(root, text="", fg="lime", bg="black",
                        font=("Courier New", 18))
    pw_label.pack(pady=(10, 10))

    def reveal():
        bar.pack_forget()
        status.config(text="Generated Password:")
        pw_label.config(text=password)

    
    start_progress(bar, 0, on_done=reveal)

    tk.Button(root, text="Back", fg="green", bg="black",
              height=2, width=15, font=("Courier New", 10),
              command=generate_screen).pack(pady=(10, 0))

    tk.Button(root, text="Back To Menu", fg="green", bg="black",
              height=2, width=15, font=("Courier New", 10),
              command=main_screen).pack(pady=(20, 0))




# for length based passwords
def show_generated_with_length(kind: str, length: int):
    clear_root()
    root.title(f"{kind} ({length})")

    tk.Label(root, text=f"{kind}", fg="green", bg="black",
             font=("Courier New", 28)).pack(pady=(30, 10))

    status = tk.Label(root, text="Generating Password...", fg="lime",
                      bg="black", font=("Courier New", 18))
    status.pack(pady=(10, 10))

    bar = ttk.Progressbar(
        root,
        style="DarkGreen.Horizontal.TProgressbar",
        orient="horizontal",
        length=300,
        mode="determinate",
        maximum=100,
    )
    bar.pack(pady=(5, 20))

    try:
        password = generate_password(kind, length=length)
    except Exception as e:
        password = f"Error: {e}"

    pw_label = tk.Label(root, text="", fg="lime", bg="black",
                        font=("Courier New", 18))
    pw_label.pack(pady=(10, 10))

    def reveal():
        bar.pack_forget()
        status.config(text="Generated Password:")
        pw_label.config(text=password)

    start_progress(bar, 0, on_done=reveal)

    tk.Button(root, text="Back", fg="green", bg="black",
              height=2, width=15, font=("Courier New", 10),
              command=generate_screen).pack(pady=(10, 0))

    tk.Button(root, text="Back", fg="green", bg="black",
              height=2, width=15, font=("Courier New", 10),
              command=length_based_screen).pack(pady=(20, 0))




def length_based_screen():
    clear_root()
    root.title("Length Based")

    tk.Label(root, text="Length Based", fg="green", bg="black",
             font=("Courier New", 24)).pack(pady=(30, 10))

    tk.Label(root, text="Choose a length (≥ 6):", fg="darkgreen", bg="black",
             font=("Courier New", 14)).pack(pady=(10, 5))

    length_var = tk.StringVar(value="12")
    length_entry = tk.Entry(root, textvariable=length_var, bg="darkgrey",
                            width=8, font=("Courier New", 16), justify="center")
    length_entry.pack(pady=(0, 10))
    length_entry.focus_set()

    status = tk.Label(root, text="", fg="yellow", bg="black",
                      font=("Courier New", 12))
    status.pack(pady=(6, 6))

    def go(event=None):
        s = length_var.get().strip()
        if not s.isdigit():
            status.config(text="Please enter a number.")
            return
        n = int(s)
        if n < 6:
            status.config(text="Length must be ≥ 6.")
            return
        show_generated_with_length("Length Based", n)

    tk.Button(root, text="Generate", fg="darkgreen", bg="black",
              width=12, command=go).pack(pady=(6, 6))

    tk.Button(root, text="Back", fg="green", bg="black",
              width=12, command=generate_screen).pack(pady=(0, 12))

    length_entry.bind("<Return>", go)



def letters_only():
    show_generated("Letters Only")


def alphanumeric():
    show_generated("Alphanumeric")


def Alpha_special():
    show_generated("Alphanumeric + Special")


def mixed_case_letters():
    show_generated("Mixed Case Letters")


def complex():
    show_generated("Complex")


def no_words_patterns():
    show_generated("No Words/Patterns")


def no_rep_chars():
    show_generated("No Repeated Characters")



# security types
def low_sec():
    clear_root()
    root.title("Low Security Types")

    main_frame = tk.Frame(root, bg="black")
    main_frame.pack(expand=True, fill="both")

    tk.Label(main_frame, text="Low Security Types", bg="black",
             fg="darkgreen", font=("Courier New", 20)).pack(pady=(50, 15))

    tk.Label(main_frame, text="Which Option Will You Pick?", bg="black",
             fg="darkgreen", font=("Courier New", 20)).pack(pady=(20, 5))

    button_section = tk.Frame(main_frame, bg="black")
    button_section.pack(side="bottom", pady=30, anchor="s")

    top_buttons = tk.Frame(button_section, bg="black")
    top_buttons.pack(pady=(0, 8))

    tk.Button(top_buttons, text="Letters Only", fg="darkgreen", bg="black",
              width=15, height=2, command=letters_only).pack(side="left", padx=20)

    tk.Button(top_buttons, text="Alphanumeric", fg="darkgreen", bg="black",
              width=15, height=2, command=alphanumeric).pack(side="right", padx=20)

    footer = tk.Frame(root, bg="black")
    footer.pack(side="bottom", pady=25, anchor="s")

    tk.Button(footer, text="Back", fg="green", bg="black",
              height=2, width=15, font=("Courier New", 10),
              command=generate_screen).pack()



def med_sec():
    clear_root()
    root.title("Medium Security Types")

    main_frame = tk.Frame(root, bg="black")
    main_frame.pack(expand=True, fill="both")

    tk.Label(main_frame, text="Medium Security Types", bg="black",
             fg="darkgreen", font=("Courier New", 20)).pack(pady=(50, 15))

    tk.Label(main_frame, text="Which Option Will You Pick?", bg="black",
             fg="darkgreen", font=("Courier New", 20)).pack(pady=(20, 5))

    button_section = tk.Frame(main_frame, bg="black")
    button_section.pack(side="bottom", pady=30, anchor="s")

    top_row = tk.Frame(button_section, bg="black")
    top_row.pack(pady=(0, 8))

    tk.Button(top_row, text="Alphanumeric + Special", fg="darkgreen", bg="black",
              width=20, height=2, command=Alpha_special).pack(side="left", padx=12)

    tk.Button(top_row, text="Mixed Case Letters", fg="darkgreen", bg="black",
              width=20, height=2, command=mixed_case_letters).pack(side="right", padx=12)

    tk.Button(button_section, text="Length Based", fg="darkgreen", bg="black",
              width=16, pady=8, command=length_based_screen).pack(pady=(10, 0))

    footer = tk.Frame(root, bg="black")
    footer.pack(side="bottom", pady=25, anchor="s")

    tk.Button(footer, text="Back", fg="green", bg="black",
              height=2, width=15, font=("Courier New", 10),
              command=generate_screen).pack()



def high_sec():
    clear_root()
    root.title("High Security Types")

    main_frame = tk.Frame(root, bg="black")
    main_frame.pack(expand=True, fill="both")

    tk.Label(main_frame, text="High Security Types", bg="black",
             fg="darkgreen", font=("Courier New", 20)).pack(pady=(50, 15))

    tk.Label(main_frame, text="Which Option Will You Pick?", bg="black",
             fg="darkgreen", font=("Courier New", 20)).pack(pady=(20, 5))

    button_section = tk.Frame(main_frame, bg="black")
    button_section.pack(side="bottom", pady=30, anchor="s")

    top_row = tk.Frame(button_section, bg="black")
    top_row.pack(pady=(0, 8))

    tk.Button(top_row, text="Complex", fg="darkgreen", bg="black",
              width=15, height=2, command=complex).pack(side="left", padx=12)

    tk.Button(top_row, text="No Words/Patterns", fg="darkgreen", bg="black",
              width=20, height=2, command=no_words_patterns).pack(side="right", padx=12)

    tk.Button(button_section, text="No Repeated Characters", fg="darkgreen", bg="black",
              width=24, pady=8, command=no_rep_chars).pack(pady=(10, 0))

    footer = tk.Frame(root, bg="black")
    footer.pack(side="bottom", pady=25, anchor="s")

    tk.Button(footer, text="Back", fg="green", bg="black",
              height=2, width=15, font=("Courier New", 10),
              command=generate_screen).pack()



def add_update_screen():
    clear_root()
    root.title("Add / Update Password")

    tk.Label(root, text="Add / Update Password",
             fg="green", bg="black", font=("Courier New", 20)).pack(pady=(30, 10))

    content = tk.Frame(root, bg="black")
    content.pack(fill="both", expand=True, padx=20)

    tk.Label(content, text="Website / Service name:",
             fg="green", bg="black", font=("Courier New", 12)).pack(pady=(10, 4))
    site_var = tk.StringVar()
    site_entry = tk.Entry(content, textvariable=site_var, bg="darkgrey",
                          width=24, font=("Courier New", 14))
    site_entry.pack(pady=(0, 12))
    site_entry.focus_set()

    tk.Label(content, text="Password:",
             fg="green", bg="black", font=("Courier New", 12)).pack(pady=(6, 4))
    pwd_var = tk.StringVar()
    pwd_entry = tk.Entry(content, textvariable=pwd_var, bg="darkgrey",
                         width=24, font=("Courier New", 14), show="*")
    pwd_entry.pack(pady=(0, 12))

    site_entry.bind("<Return>", lambda e: pwd_entry.focus_set())
    root.bind("<Escape>", lambda e: main_screen())

    status = tk.Label(content, text="", fg="lime", bg="black", font=("Courier New", 12))
    status.pack(pady=(6, 8))


    # save password into OS keychain
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
        set_password(site_key, pwd)
        status.config(text=f"Saved password for {site_raw}", fg="lime")

    pwd_entry.bind("<Return>", save_password)

    btn_row = tk.Frame(root, bg="black")
    btn_row.pack(side="bottom", pady=20, anchor="s")

    tk.Button(btn_row, text="Save", fg="darkgreen", bg="black",
              width=12, command=save_password).pack(side="left", padx=10)

    tk.Button(btn_row, text="Back To Menu", fg="green", bg="black",
              width=15, command=main_screen).pack(side="left", padx=10)



def vault_screen():
    clear_root()
    root.title("The Vault")

    tk.Label(root, text="Saved Passwords", fg="green", bg="black",
             font=("Courier New", 20)).pack(pady=(30, 10))

    content = tk.Frame(root, bg="black")
    content.pack(fill="both", expand=True)

    tk.Label(content, text="Which password do you need?",
             fg="green", bg="black", font=("Courier New", 12)).pack(pady=(40, 10))

    search_var = tk.StringVar()
    search_entry = tk.Entry(content, textvariable=search_var, bg="darkgrey",
                            width=20, font=("Courier New", 14))
    search_entry.pack(pady=(25, 50))
    search_entry.focus_set()

    result_label = tk.Label(content, text="", fg="lime", bg="black",
                            font=("Courier New", 12))
    result_label.pack(pady=(0, 10))
    root.unbind("<Escape>")



    # look up password for website
    def on_query_enter(event=None):
        site = search_var.get()
        key = site.strip().lower()
        if not key:
            result_label.config(text="Please enter a website where you have a password", fg="yellow")
            return
        pwd = get_password(key)
        if pwd:
            result_label.config(text=f"Password for {site}: {pwd}", fg="lime")
            root.clipboard_clear()
            root.clipboard_append(pwd)
            root.update()
        else:
            result_label.config(text="Password not found for this website", fg="red")

    search_entry.bind("<Return>", on_query_enter)

    footer = tk.Frame(root, bg="black")
    footer.pack(side="bottom", pady=20, anchor="s")

    tk.Button(footer, text="Back To Menu", fg="green", bg="black",
              height=2, width=15, font=("Courier New", 10),
              command=main_screen).pack()



def view_passwords():
    clear_root()
    root.title("View Passwords")

    tk.Label(root, text="Saved Passwords", fg="green", bg="black",
             font=("Courier New", 20)).pack(pady=(30, 10))

    content = tk.Frame(root, bg="black")
    content.pack(fill="both", expand=True)

    tk.Label(content, text="Enter Ultra-Secure-Password to enter The Vault",
             fg="green", bg="black", font=("Courier New", 12)).pack(pady=(40, 10))

    search_var = tk.StringVar()
    search_entry = tk.Entry(content, textvariable=search_var, bg="darkgrey",
                            width=20, show="*", font=("Courier New", 14))
    search_entry.pack(pady=(25, 50))
    search_entry.focus_set()

    error_label = tk.Label(content, text="", fg="red", bg="black",
                           font=("Courier New", 12))

    root.unbind("<Escape>")



    def check_password(event=None):
        if hide_timer["id"] is not None:
            root.after_cancel(hide_timer["id"])
            hide_timer["id"] = None

        if search_var.get() == "Place": # Playboi Carti - Place (Prod. Pi'erre)
            error_label.pack_forget()
            vault_screen()
        else:
            error_label.config(text="ACCESS DENIED")
            if not error_label.winfo_ismapped():
                error_label.pack(pady=(0, 5))
            hide_timer["id"] = root.after(1500, lambda: error_label.pack_forget())


    search_entry.bind("<Return>", check_password)

    footer = tk.Frame(root, bg="black")
    footer.pack(side="bottom", pady=20, anchor="s")

    tk.Button(footer, text="Back To Menu", fg="green", bg="black",
              height=2, width=15, font=("Courier New", 10),
              command=main_screen).pack()



def generate_screen():
    clear_root()
    root.title("Security Types")

    main_frame = tk.Frame(root, bg="black")
    main_frame.pack(expand=True, fill="both")

    tk.Label(main_frame, text="What Security Type", bg="black",
             fg="darkgreen", font=("Courier New", 20)).pack(pady=(50, 15))

    tk.Label(main_frame, text="Would You Like?", bg="black",
             fg="darkgreen", font=("Courier New", 20)).pack(pady=(20, 5))

    button_section = tk.Frame(main_frame, bg="black")
    button_section.pack(side="bottom", pady=30, anchor="s")

    top_buttons = tk.Frame(button_section, bg="black")
    top_buttons.pack(pady=(0, 8))

    tk.Button(top_buttons, text="Low Security", fg="darkgreen", bg="black",
              width=15, height=2, command=low_sec).pack(side="left", padx=20)

    tk.Button(top_buttons, text="Medium Security", fg="darkgreen", bg="black",
              width=15, height=2, command=med_sec).pack(side="right", padx=20)

    tk.Button(button_section, text="High Security", fg="darkgreen", bg="black",
              width=12, pady=10, command=high_sec).pack(pady=(10, 0))

    footer = tk.Frame(root, bg="black")
    footer.pack(side="bottom", pady=25, anchor="s")

    tk.Button(footer, text="Back To Menu", fg="green", bg="black",
              height=2, width=15, font=("Courier New", 10),
              command=main_screen).pack()



def main_screen():
    global progress
    clear_root()

    root.title("Password Generator")

    title_font = ("Courier New", 30)
    prompt_font = ("Courier New", 18)

    tk.Label(root, text="PassWord Generator", fg="green",
             bg="black", font=title_font).pack(pady=20)

    tk.Label(root, text="What would you like to do?", fg="green",
             bg="black", font=prompt_font).pack(pady=30)

    button_section = tk.Frame(root, bg="black")
    button_section.pack(side="bottom", pady=120, anchor="s")

    top_buttons = tk.Frame(button_section, bg="black")
    top_buttons.pack(pady=(0, 10))

    tk.Button(top_buttons, text="View Passwords", fg="darkgreen", bg="black",
              width=15, height=2, command=view_passwords).pack(side="left", padx=20)

    tk.Button(top_buttons, text="Generate Password", fg="darkgreen", bg="black",
              width=15, height=2, command=generate_screen).pack(side="right", padx=20)

    tk.Button(button_section, text="Add / Update Website or Password", fg="darkgreen",
              bg="black", width=30, pady=55, command=add_update_screen).pack(pady=(.5, 0))

    progress = ttk.Progressbar(
        root,
        style="DarkGreen.Horizontal.TProgressbar",
        orient="horizontal",
        length=300,
        mode="determinate",
        maximum=100,
    )
    progress.pack(pady=15)
    root.bind("<Escape>", lambda e: root.destroy())



main_screen()
root.mainloop()
