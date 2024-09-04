def calculate_circle(r):

    a = 3.1416 * r ** 2
    c = 2 * 3.1416 * r
    
    return a,c

r = float(input("Enter the radius of the circle: "))

a,c = calculate_circle(r)

print(f"Area of the circle: {a:.2f}")
print(f"Circumference of the circle: {c:.2f}")
