# Password Generator

import random
import string

print("🔑 Welcome to Password Generator!")

while True:
    length = int(input("Enter password length: "))

    # Characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password
    password = "".join(random.choice(characters) for _ in range(length))

    print(f"Your secure password: {password}")

    again = input("Do you want to generate another password? (yes/no): ").lower()
    if again != "yes":
        print("Goodbye! 👋")
        break
