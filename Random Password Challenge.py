import random

length = int(input("Enter password length: "))

def generate_password(length):
    # all characters too use for password
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # A–Z
    characters += "abcdefghijklmnopqrstuvwxyz" # a–z
    characters += "0123456789"                 # 0–9
    characters += "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"  # symbols
    
    # Generate random password
    password = ''.join(random.choice(characters) for _int_ in range(length))
    
    return password


print("Generated Password:", generate_password(length))
