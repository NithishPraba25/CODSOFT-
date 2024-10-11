import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=length))

length = int(input("Enter password length: "))
password = generate_password(length)
print("Generated Password:", password)
