special_chars = ['@', '!', '#', '$', '%', '¨', '&', '*', '(', ')', '-', '=', '+', '_']

while True:
    password = input("\nEnter password (or type 'exit' to exit): ")

    if password.lower() == 'exit':
        print("\nExiting the program.")
        break

    if not password:
        print("\nNo password was entered.")
        continue

    strength = 10

    if any(char in special_chars for char in password):
        strength += 20
    if any(char.isupper() for char in password):
        strength += 20
    if any(char.isdigit() for char in password):
        strength += 20
    if len(password) >= 12:
        strength += 20
    if len(password) >= 8:
        strength += 10

    print(f"Password strength: {strength}/100")




