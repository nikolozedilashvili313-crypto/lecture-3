names = ["Laptop", "Phone", "Headphones", "Monitor"]
prices = [1200, 800, 150, 300]
ratings = [4.8, 4.5, 4.2, 4.9]

catalog = list(zip(names, prices, ratings))

sorted_by_price = sorted(catalog, key=lambda item: item[1], reverse=True)
print("Sorted by price (highest to lowest):")
print(sorted_by_price)

sorted_by_rating = sorted(catalog, key=lambda item: item[2])
print("\nSorted by rating (lowest to highest):")
print(sorted_by_rating)