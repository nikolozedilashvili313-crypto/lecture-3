cart_total = float(input("Enter cart total: $"))

is_vip = input("Are you a VIP member? (yes/no): ").lower() == "yes"
is_guest = input("Are you a guest user? (yes/no): ").lower() == "yes"

promo_code = input("Enter promo code (or press Enter to skip): ")

# Free shipping
if cart_total >= 50 or is_vip:
    print("You get FREE SHIPPING!")
else:
    print("You have to pay for shipping.")

# Discount
if promo_code and not is_guest and promo_code == "SAVE10":
    discount = cart_total * 0.10
    final_total = cart_total - discount
    print("10% discount applied!")
    print(f"Final total price: ${final_total:.2f}")
else:
    final_total = cart_total
    print("No discount applied.")
    print(f"Final total price: ${final_total:.2f}")
