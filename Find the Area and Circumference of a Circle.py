def calculate_circle(r):

    a = 3.1416 * r ** 2
    c = 2 * 3.1416 * r
    return a,c
               
r = float(input("Enter The Radius Of The Circle: "))
a,c = calculate_circle(r)

print(f"Area Of The Circle: {a:.2f}")
print(f"Circumference Of The Circle: {c:.2f}") 
