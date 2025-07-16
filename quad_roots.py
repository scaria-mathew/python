import cmath

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = b**2 - 4*a*c
root = -b + cmath.sqrt(d)/2*a
print("Answer", root)