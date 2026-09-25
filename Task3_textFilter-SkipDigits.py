text = input("Enter a string: ")

result = ""

for char in text:

    if char.isdigit():
        continue

    result += char

print(result)