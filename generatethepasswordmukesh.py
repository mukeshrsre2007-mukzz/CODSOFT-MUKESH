import random
import string
print("Welcome to the Password Generator!")
try:
    length = int(input("Enter the desired password length: "))
    letters = string.ascii_letters 
    digits = string.digits
    symbols = string.punctuation
    all_chars = letters + digits + symbols
    password = ''.join(random.choice(all_chars) for _ in range(length))
    print("\nYour generated password is:")
    print(password)
except:
    print("sorry! Please enter a valid number.")