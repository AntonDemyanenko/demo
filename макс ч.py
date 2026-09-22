def max2(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return a if not isinstance(b, (int, float)) else b
    return a if a >= b else b

try:
    num1 = float(input())
    num2 = float(input())
    result = max2(num1, num2)
    if result.is_integer():
        print(int(result))
    else:
        print(result)
except ValueError:
    print("Ошибка: введено не число")