import random

all_chars = 'abcdefghijklmnopqrstuvwxyz!@#$%^&*()?1234567890' 
letters_only = 'abcdefghijklmnopqrstuvwxyz'         
nums_only = '1234567890'
special_only = '!@#$%^&*()?'                      
chars_and_nums = 'abcdefghijklmnopqrstuvwxyz1234567890'
all_chars_cases = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz!@#$%^&*()?1234567890'


password = ''
for x in range(16):
    password += random.choice(all_chars)

basic_types = ["Letters Only", "Alphanumeric"]                                        # low security
intermediate_types = ["Alphanumeric + Special", "Mixed Case Letters", "Length Based"] # Moderate security
advanced_types = ["Complex", "No words/patterns", "No Repeated Characters"]           # High Security

all_types = [basic_types, intermediate_types, advanced_types]

prompt = "What kind of password would you like? Options: "

option_list = [option for types in all_types for option in types] # each option in each type in all types list

print(prompt)
print(*option_list, sep="\n") # prints each option seperated by new line
user_inp = input("What would you like?: ").strip()



result = "Your Password Is: "

if user_inp == "Letters Only":
    chars_only = ''.join(random.sample(letters_only, 15)) # random group of selected chars only, character limit
    print(result + chars_only)

elif user_inp == "Alphanumeric":
    alpha_n = ''.join(random.sample(chars_and_nums, 15))
    print(result + alpha_n)

elif user_inp == "Alphanumeric + Special":
    alpha_num_and_s = ''.join(random.sample(all_chars, 15))
    print(result + alpha_num_and_s)

elif user_inp == "Mixed Case Letters":
    mixed_chars = ''.join(random.sample(all_chars_cases, 15))
    print(result + mixed_chars)

elif user_inp == "Length Based":
    lenPut = int(input("What length?: "))
    len_res = ''.join(random.sample(all_chars_cases, lenPut))
    print(result + len_res)

elif user_inp == "Complex":
    complex_res = ''.join(random.sample(all_chars_cases, 25))
    print(result + complex_res)

elif user_inp == "No Words/Patterns":
    no_patts = ''.join(random.sample(all_chars_cases, 20))
    print(result + no_patts)

elif user_inp == "No Repeated Characters":
    no_reps = ''.join(random.sample(all_chars_cases, 20))
    print(result + no_reps)
    

