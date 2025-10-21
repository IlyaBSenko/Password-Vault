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



# cool words because they are cool
words = [
    # Power vibes
    "Titan", "Vortex", "Phantom", "Inferno", "Blaze", "Shadow",
    "Specter", "Voltage", "Tempest", "Guardian", "Sentinel",
    "Spectral", "Apex", "Pulse", "Surge", "Nova", "Rogue",
    "Blitz", "Reactor", "Havoc", "Spectra", "Echo", "Mirage",
    "Radiant", "Nebula", "Obsidian", "Onyx", "Crimson", "Vigil",
    "Valor", "Super", "Falcon", "Raven", "Jaguar", "Cobalt",

    # Elements & Nature vibes
    "Storm", "Frost", "Ember", "Emberlight", "Tornado", "Cyclone",
    "Hurricane", "Avalanche", "Solar", "Lunar", "Eclipse",
    "Comet", "Meteor", "Quasar", "Plasma", "Atom", "Ion",
    "Glacier", "Infernal", "Terra", "Aether", "Zephyr",

    # Technology & Energy vibes
    "Quantum", "Neon", "Circuit", "Cipher", "Fusion", "Gamma",
    "Omega", "Sigma", "Delta", "Vector", "Volt", "Core",
    "Mach", "Proto", "Nano", "Cyber", "Zero", "EchoCore",

    # Mythic & Heroic vibes
    "Apollo", "Orion", "Valkyrie", "Artemis", "Achilles", "Prometheus",
    "Hercules", "Spartan", "Phoenix", "Draco", "Chronos", "Ares",
    "Helios", "Nyx", "Zeus", "Raiden", "Odin", "Erebus", "Atlas",

    # Mysterious and Stealth vibes
    "Silent", "Stealth", "Shade", "Wraith", "Cipher", "PhantomX",
    "Reaper", "Specter", "EchoShadow", "Nightfall", "Void",
    "Oblivion", "Abyss", "Drift", "Vanish", "Fade", "Darklight"
]



basic_types = ["Letters Only", "Alphanumeric"]
intermediate_types = ["Alphanumeric + Special", "Mixed Case Letters", "Length Based"]
advanced_types = ["Complex", "No Words/Patterns", "No Repeated Characters"]


all_types = [basic_types, intermediate_types, advanced_types]



def get_options():
    return [opt for group in all_types for opt in group]



def _rand_from(pool: str, n: int) -> str:
    return "".join(choice(pool) for _ in range(n))



base = choice(words).lower() # for words

def generate_password(kind: str, length: int | None = None) -> str:
    """
    Return a password string based on kind.
    If kind == 'Length Based', length is required (>= 6 recommended).
    """
    kind = (kind or "").strip()

    if kind == "Letters Only":
        start_idx = choice(range(len(ascii_lowercase) - 2))
        tail = ascii_lowercase[start_idx:start_idx + 3]
        return base + tail

    elif kind == "Alphanumeric":
        start_idx = choice(range(len(nums_only) - 2))
        tail = nums_only[start_idx:start_idx + 3]
        return base + tail

    elif kind == "Alphanumeric + Special":
        start_idx = choice(range(len(nums_only) - 2))
        tail_nums = nums_only[start_idx:start_idx + 3]
        tail_special = _rand_from(special_only, 3)
        return base + tail_nums + tail_special

    elif kind == "Mixed Case Letters":
        return _rand_from(upper_lower, 15)

    elif kind == "Length Based":
        if not isinstance(length, int) or length < 6:
            raise ValueError("Length Based requires length >= 6")
        return _rand_from(all_chars_cases, length)

    elif kind == "Complex":
        return _rand_from(all_chars_cases, 25)

    elif kind == "No Words/Patterns":
        # Placeholder 
        return _rand_from(all_chars_cases, 20)

    elif kind == "No Repeated Characters":
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
