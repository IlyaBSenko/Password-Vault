import random

all_chars = 'abcdefghijklmnopqrstuvwxyz!@#$%^&*()?' # len = 37
letters_only = 'abcdefghijklmnopqrstuvwxyz'         # 26

password = ''
for x in range(16):
    password += random.choice(all_chars)

print(len(letters_only))
# user_inp = print(input("What kind of password would you like? Options: " \
                        "Letters Only" \
                        "Alphanumeric" \
                        ""))



