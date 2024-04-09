import string
import random

def generate_password(length):
    # Define the characters that can be used in the password
    characters = string.ascii_letters + string.digits + "?" + "_" 

    # Generate a password of the specified length
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# Prompt the user to specify the desired length of the password
password_length = int(input("Enter the desired length of the password: "))

# Generate a password and display it
generated_password = generate_password(password_length)
print(f"Generated password: {generated_password}")