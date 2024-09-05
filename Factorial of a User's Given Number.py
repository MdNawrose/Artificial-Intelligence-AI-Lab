def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

Num = int(input("Enter a Number: "))
                   
if Num < 0:
    print("Factorial Is Not Defined For Negative Numbers.")
else:
    print(f"The Factorial Of {Num} is {factorial(Num)}")
