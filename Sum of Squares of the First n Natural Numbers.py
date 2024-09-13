def sum_of_squares(n):
  
    return (n * (n + 1) * (2 * n + 1)) // 6
n = int(input("Enter the value of n: "))
result = sum_of_squares(n)

print(f"The sum of squares of the first {n} natural numbers is: {result}")
