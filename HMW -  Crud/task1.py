import requests

base_url = "https://crudcrud.com/api/e1a54b10e5ed4644ab633d1567a3566c/products"


Product_data = {
    "name": "Laptop",
    "price": 2500,
    "in_stock": True
}


try:
    response = requests.post(f'{base_url}', json=Product_data, timeout=10)
    response.raise_for_status() 

    print("Successfully added!")
    print(response.json())

except requests.exceptions.Timeout:
    print("Request timed out. Please try again later.")
except requests.exceptions.HTTPError as e:
    print(f"HTTP error occurred: {e}")
except requests.exceptions.RequestException as err:
    print(f"An error occurred: {err}")