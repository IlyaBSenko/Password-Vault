import random
import requests

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
WORDS = response.content.splitlines()

all_chars = 'abcdefghijklmnopqrstuvwxyz!@#$%^&*()?' # len = 37
letters_only = 'abcdefghijklmnopqrstuvwxyz'         # 26
special_only = '!@#$%^&*()?'                        # 11


password = ''
for x in range(16):
    password += random.choice(all_chars)

basic_types = ["Letters Only", "Alphanumeric"]                                        # low security
intermediate_types = ["Alphanumeric + Special", "Mixed Case Letters", "Length-Based"] # Moderate security
advanced_types = ["Complex", "No words/patterns", "No Repeated Characters"]           # High Security

all_types = [basic_types, intermediate_types, advanced_types]

prompt = "What kind of password would you like? Options: "

option_list = [option for types in all_types for option in types] # each option in each type in all types list

print(prompt)
print(*option_list, sep="\n")
user_inp = print(input("What would you like?: "))



result = "Your Password Is: "

if user_inp == "Letters Only":
    chars_only = ''.join(random.sample(all_chars, 15)) # random group of chars only, 15 character limit
    print(result + chars_only)

if user_inp == "Alphanumeric":
    alpha_n = 
    

