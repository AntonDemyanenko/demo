def my_abs(x):
    if not isinstance(x, (int, float)):
        return x
    else:
        return abs(x)  # или: return x if x >= 0 else -x
print(my_abs(-5))
print(my_abs(5))
print(my_abs(0))
