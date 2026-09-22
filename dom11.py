import math

a = int(input())
b = int(input())
c = int(input())

perimeter = a + b + c

p = perimeter / 2

area = math.sqrt(p * (p - a) * (p - b) * (p - c))

print(perimeter)
print(f"{area:.2f}")