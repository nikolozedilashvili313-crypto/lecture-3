try:
    price_input = input("Enter item price: ")
    quantity_input = input("Enter quantity: ")
    
    price = float(price_input)
    quantity = int(quantity_input)
    
    total = price * quantity
except ValueError:
    print("Error: Both price and quantity must be valid numbers!")
else:
    print(f"Total price: ${total:.2f}")