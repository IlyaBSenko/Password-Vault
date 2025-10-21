# Password Generator & Vault

A Python desktop application built with **Tkinter** that allows you to generate secure passwords and store them safely using the system’s keychain via the `keyring` library.

This project includes:
- A multi-level password generator (Low, Medium, High security)
- A secure password vault that uses your operating system’s keychain
- A progress animation when generating passwords
- A clean dark-themed interface

---

## Features

| Category | Description |
|-----------|--------------|
| Low Security | Letters-only or alphanumeric passwords |
| Medium Security | Mixed case, special characters, or custom-length passwords |
| High Security | Complex, pattern-free, and non-repeating passwords |
| Vault Integration | Securely stores passwords using `keyring` |
| Modern UI | Dark theme and progress bar animations |

---

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/<IlyaBSenko>/<Password-Generator>.git
cd <repo-name>
2. Create and Activate a Virtual Environment
macOS / Linux
bash
Copy code
python3 -m venv venv
source venv/bin/activate
Windows
bash
Copy code
py -m venv venv
venv\Scripts\activate
3. Install Dependencies
All required packages are listed in requirements.txt.

bash
Copy code
pip install -r requirements.txt
4. Run the Application
macOS / Linux
bash
Copy code
python3 main.py
Windows
bash
Copy code
py main.py
Project Structure
bash
Copy code
PasswordVault/
├── main.py             # Main GUI (Tkinter)
├── generate.py         # Password generation logic
├── vault.py            # Keyring-based password storage
├── requirements.txt    # Dependencies
└── README.md           # Project documentation
How It Works
generate.py creates passwords using random combinations of letters, digits, and symbols.

main.py handles the user interface, screen navigation, and password generation visuals.

vault.py securely stores and retrieves passwords using the keyring library.

All operations happen locally; no data is sent to external servers.

Dependencies
Package	Purpose
keyring	Securely stores passwords in the system keychain
jaraco.*	Helper libraries used internally by keyring
more-itertools	Utility library used by dependencies
tkinter	GUI framework (included with Python)

Notes
On macOS, it is recommended to use a virtual environment since global pip installs are restricted.

On Windows, ensure that the “Add Python to PATH” option is checked during installation.

The default vault access password in this version is Place.

Future Improvements
Export and import vault entries

Copy-to-clipboard visual feedback

Light mode and custom themes

Entropy-based password generation

Author
