def prime(num):


    if num < 2:
        return False


    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


num = int(input("Enter A Number: "))


if prime(num):
    print(f"{num} Is A Prime Number.")
else:
    print(f"{num} Is Not A Prime Number.")







Lab Assignment 1+2 (Q1)
