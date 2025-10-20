import random

letters_only = 'abcdefghijklmnopqrstuvwxyz'         
nums_only = '1234567890'
special_only = '!@#$%^&*()?'                      
chars_and_nums = letters_only + nums_only
upper_lower = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
all_chars_cases = upper_lower + special_only + nums_only
all_chars = letters_only + nums_only + special_only


basic_types = ["Letters Only", "Alphanumeric"]                                        # low security
intermediate_types = ["Alphanumeric + Special", "Mixed Case Letters", "Length Based"] # Moderate security
advanced_types = ["Complex", "No Words/Patterns", "No Repeated Characters"]           # High Security


all_types = [basic_types, intermediate_types, advanced_types]

prompt = "What kind of password would you like? Options: "

option_list = [option for types in all_types for option in types] # each option in each type in all types list


print(prompt)
print(*option_list, sep="\n") # prints each option separated by new line
user_inp = input("What would you like?: ").strip()


# user input results

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
    mixed_chars = ''.join(random.sample(upper_lower, 15))
    print(result + mixed_chars)

elif user_inp == "Length Based":
    try:
        lenPut = int(input("What length?: "))
        if lenPut <= 5:
            print("Come on bro get real, pick a real password length. Thanks.")
        else:
            max_unique = len(set(all_chars_cases))
            len_res = ''.join(random.choice(all_chars_cases) for i in range(lenPut)) # allows repeats
            print(result + len_res)
    except ValueError:
        print("Please enter a valid length. Thank you!")

elif user_inp == "Complex":
    complex_res = ''.join(random.sample(all_chars_cases, 25))
    print(result + complex_res)

elif user_inp == "No Words/Patterns":
    # TODO: add checks to avoid dictionary substrings and simple sequences
    no_patts = ''.join(random.sample(all_chars_cases, 20))
    print(result + no_patts)

elif user_inp == "No Repeated Characters":
    no_reps = ''.join(random.sample(all_chars_cases, 20))
    print(result + no_reps)
    
else:
    print("Sorry, I don't recognize that option. Please choose one of the given options and type it exactly as displayed. Thank you.")