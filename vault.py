import keyring

SERVICE = "Vault"

def set_password(site: str, password: str):
    """Store or update a password in the OS keychain."""
    keyring.set_password(SERVICE, site.lower().strip(), password)

def get_password(site: str):
    """Retrieve a password from the OS keychain. Returns None if not found."""
    return keyring.get_password(SERVICE, site.lower().strip())

def delete_password(site: str):
    """Delete a stored password (optional helper)."""
    keyring.delete_password(SERVICE, site.lower().strip())
