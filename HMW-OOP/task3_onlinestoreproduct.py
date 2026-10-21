class Product:
    shop_name = "MegaShop"

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def sell(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
            print(f"Sold {quantity} units of {self.name}. Remaining stock: {self.stock}")
        else:
            print(f"Not enough stock for {self.name}. Available stock: {self.stock}")

laptop = Product("Laptop", 1200, 10)

print(f"Product - {laptop.name} costs ${laptop.price} and has {laptop.stock} units in stock at {Product.shop_name}")

laptop.sell(2)
laptop.sell(8)
