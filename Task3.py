import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 characters for better security.")
        return None
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters),
    ]

        return ''.join(password)

def main():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the desired password length: "))
        password = generate_password(length)
        if password:
            print(f"\nYour generated password is: {password}")
    except ValueError:
        print("Invalid input. Please enter a numerical value for the password length.")

if __name__ == "__main__":
    main()
