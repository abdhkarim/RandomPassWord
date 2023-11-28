#Générateur de mot de passe en python 

import random
import string

def generate_password(min_length, numbers=True, special_caracters= True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
            characters += digits

    if special_caracters:
            characters += special

    pwd=""
    meets_criteria = False
    has_numbers = False
    has_special = False


    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_numbers = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_numbers
        if special_caracters:
            meets_criteria = meets_criteria and has_special

    return pwd

min_length = int(input("Longueur du mot de passe: "))
has_numbers = input("Avec des chiffres ? (O/N) ").lower == "O"
has_special = input("Avec des caractères spéciaux ? (O/N) ").lower == "O"
pwd = generate_password(min_length, has_numbers, has_special)
print("The generated password is: " + pwd)

