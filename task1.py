def even_numbers():
    num = 0
    while True:
        yield num
        num += 2


print("First 10 even numbers:")
count = 0
for even in even_numbers():
    print(even)
    count += 1
    if count >= 10:
        break