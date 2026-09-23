# 1.
correct_pin = 1439
balance = 500.0

# 2.
user_pin_input = input("Enter your PIN: ")
entered_pin = int(user_pin_input)

# 3.
if entered_pin == correct_pin:
    
    user_amount_input = input("Enter withdrawal amount: $")
    requested_amount = float(user_amount_input)
    
    if requested_amount <= balance:
        balance -= requested_amount
        print(f"Withdrawal successful! Remaining balance: ${balance:.2f}")
    else:
        print("Amount of your balance isn't enough.")

else:
    print("Incorrect PIN. Access Denied!.")