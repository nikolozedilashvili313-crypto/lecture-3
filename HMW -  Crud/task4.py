import requests

base_url = "https://crudcrud.com/api/6e439a0191df4fe486e21f7429e545b9/products"


Product_id = "6e439a0191df4fe486e21f7429e545b9" 

updated_data = {
    "name": "Laptop",
    "price": 3200,
    "in_stock": True
}
try:
    response = requests.put(f'{base_url}/{Product_id}', json=updated_data, timeout=10)
    response.raise_for_status()
    print("Successfully updated!")

    verify_response = requests.get(f'{base_url}/{Product_id}', timeout=10)
    verify_response.raise_for_status()
    print("Updated Product Details:")
    print(verify_response.json())

except requests.exceptions.Timeout:
    print("Request timed out. Please try again later.")
except requests.exceptions.HTTPError as e:
    print(f"HTTP error occurred: {e}")
except requests.exceptions.RequestException as err:
    print(f"An error occurred: {err}")