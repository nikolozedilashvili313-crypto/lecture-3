n = int(input("Enter a positive integer n:"))
total_sum = 0


for num in range(2, n + 1, 2):
    total_sum += num

print(f"The sum of even numbers from 1 to {n} is: {total_sum}")