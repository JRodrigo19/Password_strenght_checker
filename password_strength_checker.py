special_chars = ['@', '!', '#', '$', '%', '¨', '&', '*', '(', ')', '-', '=', '+', '_']

print("Loading password dictionary, please wait...")
try:
    with open("passwords_list.txt", "r", encoding="latin-1") as passwords:
        wordlist = set(line.strip() for line in passwords)
except FileNotFoundError:
    print("⚠️ Wordlist file not found. Continuing without it.")
    wordlist = set()

while True:
    password = input("\nEnter password (or type 'exit' to quit): ")

    if password.lower() == 'exit':
        print("\nExiting the program.")
        break

    if not password:
        print("\nNo password was entered.")
        continue

    feedback = []
    strength = 0

    is_in_wordlist = password in wordlist

    match is_in_wordlist:
        case True:
            feedback.append("❌ Your password was found in a list of common passwords. Please choose another one.")

        case False:
            length = len(password)

            has_alpha = any(c.isalpha() for c in password)
            has_special = any(c in special_chars for c in password)
            has_upper = any(c.isupper() for c in password)
            has_lower = any(c.islower() for c in password)
            has_digit = any(c.isdigit() for c in password)
            has_length12 = length >= 12
            has_length8 = 8 <= length < 12

            # Check for alphabetic characters
            match has_alpha:
                case True:
                    strength += 10
                case False:
                    feedback.append("⚠️ Your password does not contain letters.")

            # Check for uppercase letters
            match has_upper:
                case True:
                    strength += 30
                case False:
                    feedback.append("⚠️ Your password does not contain uppercase letters.")

            # Check for lowercase letters
            match has_lower:
                case True:
                    strength += 10
                case False:
                    feedback.append("⚠️ Your password does not contain lowercase letters.")

            # Check for special characters
            match has_special:
                case True:
                    strength += 30
                case False:
                    feedback.append("⚠️ Your password does not contain special characters.")

            # Check for digits
            match has_digit:
                case True:
                    strength += 10
                case False:
                    feedback.append("⚠️ Your password does not contain digits.")

            # Evaluate password length
            match (has_length12, has_length8):
                case (False, False):
                    print("❌ Your password is shorter than the minimum of 8 characters.")
                case (False, True):
                    strength += 5
                    print("⚠️ Your password does not meet the recommended length of 12 characters.")
                case (True, False):
                    strength += 10

            # If all criteria met
            match (has_alpha, has_digit, has_lower, has_upper, has_special, has_length12):
                case (True, True, True, True, True, True):
                    feedback.append("✅ No changes necessary. Strong password.")

    for item in feedback:
        print(item)

    print(f"\n🔐 Password strength: {strength}/100")
