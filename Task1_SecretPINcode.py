correct_pin = "1439"
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    user_pin = input("Enter your 4-digit PIN:")
    attempts += 1

    if user_pin == correct_pin:
        print("Access granted!")
        break
    else:
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"incorrect PIN. Remaining attemmpts: {remaining}")
        else:
            print("Card blocked!")