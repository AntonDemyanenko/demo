x = int(input())
y = int(input())
xr = int(input())
yr = int(input())
r = int(input())

distance_sq = (x - xr) ** 2 + (y - yr) ** 2

if distance_sq <= r ** 2:
    print("Да")
else:
    print("Нет")