import random
import string

def generate_password(length,uppercase,lowercase,digits,symbols):
    characters =""
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if symbols:
        characters += string.punctuation
    if not characters:
        print("Error,no characters found :")
        
    password = "".join(random.choice(characters) for i in range(length))
    return password

length = int(input("Enter the Password Length : "))
uppercase = input("Do you want Uppercase Letters in your Password? (yes/no) : ").lower() == 'yes'
lowercase = input("Do you want Lowercase Letters in your Password? (yes/no) : ").lower() == 'yes'
digits = input("Do you want Digits Letters in your Password? (yes/no) : ").lower() == 'yes'
symbols = input("Do you want Symbols Letters in your Password? (yes/no) : ").lower() == 'yes'

password = generate_password(length,uppercase,lowercase,digits,symbols)
print(password)
