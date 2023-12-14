import random
import string

def generate_password(length=12, use_digits=True, use_special_chars=True):
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits if use_digits else ''
    special_chars = string.punctuation if use_special_chars else ''

    # Combine character sets based on user preferences
    all_chars = lowercase_letters + uppercase_letters + digits + special_chars

    # Ensure the password length is at least 8
    length = max(length, 8)

    # Generate password
    password = ''.join(random.choice(all_chars) for _ in range(length))

    return password

# Get user input for password length and options
length = int(input("Enter the desired password length: "))
use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
use_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

# Generate and print the password
password = generate_password(length, use_digits, use_special_chars)
print("Generated Password:", password)