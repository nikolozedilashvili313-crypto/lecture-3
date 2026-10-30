\
import json
from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
    in_stock: bool

json_string = '{"name": "Laptop", "price": 2500, "in_stock": true}'

data = json.loads(json_string)

p = Product(**data)
print("Type:", type(p))
print("Product Object:", p)
print("Name:", p.name)
print("Price:", p.price)
print("In Stock:", p.in_stock)