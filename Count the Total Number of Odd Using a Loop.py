n = int(input("Enter a number: "))
odd_count = 0

for i in range(1, n+1):
    if i % 2 != 0:
        odd_count += 1

print("Total number of odd numbers from 1 to", n, "is:", odd_count)
