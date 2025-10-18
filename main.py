import random

chars = 'abcdefghijklmnopqrstuvwxyz!@#$%^&*()?' # len = 37

password = ''
for x in range(16):
    password += random.choice(chars)

print(input("What kind of password would you like: "))
print(password)
