import tkinter as tk
from tkinter import ttk
from vault import get_password, set_password, delete_password
from generate import generate_password


BG        = "black"
FG_GREEN  = "green"
FG_DGREEN = "darkgreen"
FG_LIME   = "lime"
FG_WARN   = "yellow"
FG_ERR    = "red"

TITLE_FONT = ("Courier New", 28)
H1_FONT    = ("Courier New", 20)
TEXT_FONT  = ("Courier New", 18)
SMALL_FONT = ("Courier New", 12)


# hiding error messages
hide_timer = {"id": None}



root = tk.Tk()
root.title("Password Generator")
root.geometry("500x500")
root.configure(bg=BG)

style = ttk.Style()
style.theme_use("clam")
style.configure(
    "DarkGreen.Horizontal.TProgressbar",
    background="#006400",
    troughcolor=BG,
    bordercolor=BG,
    lightcolor="#006400",
    darkcolor="#006400",
)



# =========================
# Utilities / Widgets
# =========================
def clear_root():
    for w in root.winfo_children():
        w.destroy()


def make_label(parent, text, font=TEXT_FONT, fg=FG_GREEN):
    return tk.Label(parent, text=text, fg=fg, bg=BG, font=font)


def make_button(parent, text, cmd, width=15, height=2, fg=FG_DGREEN):
    return tk.Button(parent, text=text, fg=fg, bg=BG, width=width, height=height, command=cmd)


def make_progress(parent):
    return ttk.Progressbar(
        parent,
        style="DarkGreen.Horizontal.TProgressbar",
        orient="horizontal",
        length=300,
        mode="determinate",
        maximum=100,
    )



def start_progress(bar: ttk.Progressbar, i: int = 0, on_done=None):
    """Animate a specific progressbar; call on_done() when finished."""
    if bar is None or not bar.winfo_exists():
        return
    if i <= 100:
        bar["value"] = i
        root.after(15, start_progress, bar, i + 1, on_done)
    else:
        if callable(on_done):
            on_done()



# =========================
# Generator screens
# =========================
def show_generated_screen(kind: str, length: int | None = None, back_to=None):
    """
    Unified 'generate -> animate -> reveal' screen.
    If length is provided, it's passed to generate_password.
    If back_to is provided, a 'Back' button returns to that screen.
    """
    clear_root()
    title = kind if length is None else f"{kind} ({length})"
    root.title(title)

    make_label(root, title, TITLE_FONT).pack(pady=(30, 10))

    status = make_label(root, "Generating Password...", TEXT_FONT, FG_LIME)
    status.pack(pady=(10, 10))

    bar = make_progress(root)
    bar.pack(pady=(5, 20))

    try:
        pw = generate_password(kind, length=length)
    except Exception as e:
        pw = f"Error: {e}"

    pw_label = make_label(root, "", TEXT_FONT, FG_LIME)
    pw_label.pack(pady=(10, 10))

    def reveal():
        bar.pack_forget()  # hide the bar when done
        status.config(text="Generated Password:")
        pw_label.config(text=pw)

    start_progress(bar, 0, on_done=reveal)

    if back_to:
        make_button(root, "Back", back_to, width=15, height=2, fg=FG_GREEN).pack(pady=(10, 0))
    make_button(root, "Back To Menu", main_screen, width=15, height=2, fg=FG_GREEN).pack(pady=(20, 0))



def length_based_screen():
    """Prompt for the length, then call the unified generator screen."""
    clear_root()
    root.title("Length Based")

    make_label(root, "Length Based", ("Courier New", 24)).pack(pady=(30, 10))
    make_label(root, "Choose a length (≥ 6):", ("Courier New", 14), FG_DGREEN).pack(pady=(10, 5))

    length_var = tk.StringVar(value="12")
    entry = tk.Entry(root, textvariable=length_var, bg="darkgrey",
                     width=8, font=("Courier New", 16), justify="center")
    entry.pack(pady=(0, 10))
    entry.focus_set()

    status = make_label(root, "", SMALL_FONT, FG_WARN)
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
        show_generated_screen("Length Based", length=n, back_to=length_based_screen)

    make_button(root, "Generate", go, width=12, height=1).pack(pady=(6, 6))
    make_button(root, "Back", generate_screen, width=12, height=1, fg=FG_GREEN).pack(pady=(0, 12))

    entry.bind("<Return>", go)



# =========================
# Category screens (Low/Med/High)
# =========================
def render_category_screen(title: str, items: list[tuple[str, callable]]):
    """
    Generic renderer for a list of (label, command) buttons.
    items: [("Label", lambda: ...), ...]
    """
    clear_root()
    root.title(title)

    main = tk.Frame(root, bg=BG)
    main.pack(expand=True, fill="both")

    make_label(main, title, H1_FONT).pack(pady=(50, 15))
    make_label(main, "Which Option Will You Pick?", H1_FONT).pack(pady=(20, 5))

    button_section = tk.Frame(main, bg=BG)
    button_section.pack(side="bottom", pady=30, anchor="s")

    # Lay out buttons in rows of 2
    row = tk.Frame(button_section, bg=BG)
    row.pack(pady=(0, 8))
    for i, (label, cmd) in enumerate(items, start=1):
        make_button(row, label, cmd).pack(side="left", padx=12)
        if i % 2 == 0 and i != len(items):
            row = tk.Frame(button_section, bg=BG)
            row.pack(pady=(0, 8))

    footer = tk.Frame(root, bg=BG)
    footer.pack(side="bottom", pady=25, anchor="s")
    make_button(footer, "Back", generate_screen, width=15, height=2, fg=FG_GREEN).pack()



def low_sec():
    items = [
        ("Letters Only",  lambda: show_generated_screen("Letters Only",  back_to=low_sec)),
        ("Alphanumeric",  lambda: show_generated_screen("Alphanumeric",  back_to=low_sec)),
    ]
    render_category_screen("Low Security Types", items)


def med_sec():
    items = [
        ("Alphanum + Special", lambda: show_generated_screen("Alphanumeric + Special", back_to=med_sec)),
        ("Mixed Case Letters",     lambda: show_generated_screen("Mixed Case Letters",     back_to=med_sec)),
        ("Length Based",           length_based_screen),
    ]
    render_category_screen("Medium Security Types", items)


def high_sec():
    items = [
        ("Complex",                lambda: show_generated_screen("Complex",                back_to=high_sec)),
        ("No Words/Patterns",      lambda: show_generated_screen("No Words/Patterns",      back_to=high_sec)),
        ("No Repeated Characters", lambda: show_generated_screen("No Repeated Characters", back_to=high_sec)),
    ]
    render_category_screen("High Security Types", items)



# =========================
# Vault / Add-Update / View
# =========================
def add_update_screen():
    clear_root()
    root.title("Add / Update Password")

    make_label(root, "Add / Update Password", H1_FONT).pack(pady=(30, 10))

    content = tk.Frame(root, bg=BG)
    content.pack(fill="both", expand=True, padx=20)

    make_label(content, "Website / Service name:", SMALL_FONT).pack(pady=(10, 4))
    site_var = tk.StringVar()
    site_entry = tk.Entry(content, textvariable=site_var, bg="darkgrey", width=24, font=("Courier New", 14))
    site_entry.pack(pady=(0, 12))
    site_entry.focus_set()

    make_label(content, "Password:", SMALL_FONT).pack(pady=(6, 4))
    pwd_var = tk.StringVar()
    pwd_entry = tk.Entry(content, textvariable=pwd_var, bg="darkgrey", width=24, font=("Courier New", 14), show="*")
    pwd_entry.pack(pady=(0, 12))

    site_entry.bind("<Return>", lambda e: pwd_entry.focus_set())
    root.bind("<Escape>", lambda e: main_screen())

    status = make_label(content, "", SMALL_FONT, FG_LIME)
    status.pack(pady=(6, 8))



    def save_password(event=None):
        site_raw = site_var.get().strip()
        site_key = site_raw.lower()
        if not site_raw:
            status.config(text="Please enter a website name", fg=FG_WARN)
            return
        pwd = pwd_var.get()
        if pwd == "":
            status.config(text="Please enter a password", fg=FG_WARN)
            return
        set_password(site_key, pwd)
        status.config(text=f"Saved password for {site_raw}", fg=FG_LIME)

    pwd_entry.bind("<Return>", save_password)

    btn_row = tk.Frame(root, bg=BG)
    btn_row.pack(side="bottom", pady=20, anchor="s")

    make_button(btn_row, "Save", save_password, width=12).pack(side="left", padx=10)
    make_button(btn_row, "Back To Menu", main_screen, width=15, fg=FG_GREEN).pack(side="left", padx=10)



def vault_screen():
    clear_root()
    root.title("The Vault")

    make_label(root, "Saved Passwords", H1_FONT).pack(pady=(30, 10))

    content = tk.Frame(root, bg=BG)
    content.pack(fill="both", expand=True)

    make_label(content, "Which password do you need?", SMALL_FONT).pack(pady=(40, 10))

    search_var = tk.StringVar()
    search_entry = tk.Entry(content, textvariable=search_var, bg="darkgrey", width=20, font=("Courier New", 14))
    search_entry.pack(pady=(25, 50))
    search_entry.focus_set()

    result_label = make_label(content, "", SMALL_FONT, FG_LIME)
    result_label.pack(pady=(0, 10))
    root.unbind("<Escape>")



    def on_query_enter(event=None):
        site = search_var.get()
        key = site.strip().lower()
        if not key:
            result_label.config(text="Please enter a website where you have a password", fg=FG_WARN)
            return
        pwd = get_password(key)
        if pwd:
            result_label.config(text=f"Password for {site}: {pwd}", fg=FG_LIME)
            root.clipboard_clear()
            root.clipboard_append(pwd)
            root.update()
        else:
            result_label.config(text="Password not found for this website", fg=FG_ERR)

    search_entry.bind("<Return>", on_query_enter)

    footer = tk.Frame(root, bg=BG)
    footer.pack(side="bottom", pady=20, anchor="s")

    make_button(footer, "Back To Menu", main_screen, width=15, fg=FG_GREEN).pack()



def view_passwords():
    clear_root()
    root.title("View Passwords")

    make_label(root, "Saved Passwords", H1_FONT).pack(pady=(30, 10))

    content = tk.Frame(root, bg=BG)
    content.pack(fill="both", expand=True)

    make_label(content, "Enter Ultra-Secure-Password to enter The Vault", SMALL_FONT).pack(pady=(40, 10))

    search_var = tk.StringVar()
    search_entry = tk.Entry(content, textvariable=search_var, bg="darkgrey", width=20, show="*", font=("Courier New", 14))
    search_entry.pack(pady=(25, 50))
    search_entry.focus_set()

    error_label = make_label(content, "", SMALL_FONT, FG_ERR)

    root.unbind("<Escape>")

    def check_password(event=None):
        if hide_timer["id"] is not None:
            root.after_cancel(hide_timer["id"])
            hide_timer["id"] = None

        if search_var.get() == "Place":  # Playboi Carti - Place (Prod. Pi'erre) listen to this song if your reading this, trust
            error_label.pack_forget()
            vault_screen()
        else:
            error_label.config(text="ACCESS DENIED")
            if not error_label.winfo_ismapped():
                error_label.pack(pady=(0, 5))
            hide_timer["id"] = root.after(1500, lambda: error_label.pack_forget())

    search_entry.bind("<Return>", check_password)

    footer = tk.Frame(root, bg=BG)
    footer.pack(side="bottom", pady=20, anchor="s")

    make_button(footer, "Back To Menu", main_screen, width=15, fg=FG_GREEN).pack()



# =========================
# Generate / Main menus
# =========================
def generate_screen():
    clear_root()
    root.title("Security Types")

    main = tk.Frame(root, bg=BG)
    main.pack(expand=True, fill="both")

    make_label(main, "What Security Type", H1_FONT, FG_DGREEN).pack(pady=(50, 15))
    make_label(main, "Would You Like?", H1_FONT, FG_DGREEN).pack(pady=(20, 5))

    button_section = tk.Frame(main, bg=BG)
    button_section.pack(side="bottom", pady=30, anchor="s")

    top = tk.Frame(button_section, bg=BG)
    top.pack(pady=(0, 8))

    make_button(top, "Low Security", low_sec).pack(side="left", padx=20)
    make_button(top, "Medium Security", med_sec).pack(side="right", padx=20)

    make_button(button_section, "High Security", high_sec, width=12, height=2).pack(pady=(10, 0))

    footer = tk.Frame(root, bg=BG)
    footer.pack(side="bottom", pady=25, anchor="s")

    make_button(footer, "Back To Menu", main_screen, width=15, fg=FG_GREEN).pack()



def main_screen():
    clear_root()
    root.title("Password Generator")

    make_label(root, "PassWord Generator", ("Courier New", 30)).pack(pady=20)
    make_label(root, "What would you like to do?", ("Courier New", 18)).pack(pady=30)

    button_section = tk.Frame(root, bg=BG)
    button_section.pack(side="bottom", pady=120, anchor="s")

    top = tk.Frame(button_section, bg=BG)
    top.pack(pady=(0, 10))

    make_button(top, "View Passwords", view_passwords).pack(side="left", padx=20)
    make_button(top, "Generate Password", generate_screen).pack(side="right", padx=20)

    make_button(button_section, "Add / Update Website or Password", add_update_screen,
                width=30, height=3).pack(pady=(.5, 0))

   



main_screen()
root.mainloop()
