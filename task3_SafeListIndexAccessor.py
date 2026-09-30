fruits = ["apple", "banana", "cherry", "orange"]

user_input = input("Enter an index number: ")

try:
    index = int(user_input)
    print(f"Selected fruit: {fruits[index]}")
except ValueError:
    print("Invalid input! Please enter a whole number.")
except IndexError:
    print(f"Index out of bounds! Choose an index between 0 and {len(fruits)-1}.")
else:
    print("Successfully retrieved item!")