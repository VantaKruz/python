import math

a=int(input("Enter Coefficient of x²: "))
b=int(input("Enter Coefficient of x: "))
c=int(input("Enter Constant term: "))

d=(b**2)-(4*a*c)

X1=(-b+math.sqrt(d))/(2*a)
X2=(-b-math.sqrt(d))/(2*a)

print(f"Roots of Quadratic Equation: {a}x² + {b}x + {c} are: {X1} and {X2}")