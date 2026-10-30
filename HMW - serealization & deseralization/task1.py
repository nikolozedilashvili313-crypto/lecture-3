#task 1
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    in_stock: bool

product1 = Product(name="Laptop", price=2500.0, in_stock=True)
product2 = Product(name="Mouse", price=80.0, in_stock=True)
product3 = Product(name="Keyboard", price=150.0, in_stock=False)

print(product1)
print(product2)
print(product3)
