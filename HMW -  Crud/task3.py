import requests

base_url = "https://crudcrud.com/api/6e439a0191df4fe486e21f7429e545b9/products"


Product_id = "6e439a0191df4fe486e21f7429e545b9" 


try:
    response = requests.get(f'{base_url}/{Product_id}', timeout=10)
    response.raise_for_status()

    print("Single Product Details:")
    print(response.json())



except requests.exceptions.Timeout:
    print("Request timed out. Please try again later.")
except requests.exceptions.HTTPError as e:
    print(f"HTTP error occurred: {e}")
except requests.exceptions.RequestException as err:
    print(f"An error occurred: {err}")