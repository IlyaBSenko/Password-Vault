# generate.py
from secrets import choice
from string import ascii_lowercase, ascii_uppercase, digits

letters_only = ascii_lowercase
nums_only = digits
special_only = '!@#$%^&*()?'
chars_and_nums = letters_only + nums_only
upper_lower = ascii_lowercase + ascii_uppercase
all_chars_cases = upper_lower + special_only + nums_only
all_chars = letters_only + nums_only + special_only

basic_types = ["Letters Only", "Alphanumeric"]
intermediate_types = ["Alphanumeric + Special", "Mixed Case Letters", "Length Based"]
advanced_types = ["Complex", "No Words/Patterns", "No Repeated Characters"]

all_types = [basic_types, intermediate_types, advanced_types]

def get_options():
    """Flat list for your dropdown."""
    return [opt for group in all_types for opt in group]

def _rand_from(pool: str, n: int) -> str:
    return "".join(choice(pool) for _ in range(n))

def generate_password(kind: str, length: int | None = None) -> str:
    """
    Return a password string based on kind.
    If kind == 'Length Based', length is required (>= 6 recommended).
    """
    kind = (kind or "").strip()

    if kind == "Letters Only":
        return _rand_from(letters_only, 15)

    elif kind == "Alphanumeric":
        return _rand_from(chars_and_nums, 15)

    elif kind == "Alphanumeric + Special":
        return _rand_from(all_chars, 15)

    elif kind == "Mixed Case Letters":
        return _rand_from(upper_lower, 15)

    elif kind == "Length Based":
        if not isinstance(length, int) or length < 6:
            raise ValueError("Length Based requires length >= 6")
        return _rand_from(all_chars_cases, length)

    elif kind == "Complex":
        return _rand_from(all_chars_cases, 25)

    elif kind == "No Words/Patterns":
        # Placeholder; still just random strong mix
        return _rand_from(all_chars_cases, 20)

    elif kind == "No Repeated Characters":
        # Allow up to unique pool size, otherwise fall back to allowing repeats
        target = 20
        unique_pool = list(dict.fromkeys(all_chars_cases))
        if target <= len(unique_pool):
            from secrets import SystemRandom
            rng = SystemRandom()
            rng.shuffle(unique_pool)
            return "".join(unique_pool[:target])
        else:
            return _rand_from(all_chars_cases, target)

    else:
        raise ValueError("Unknown password kind")
