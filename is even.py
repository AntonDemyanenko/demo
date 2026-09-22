#def is_even(n):
#    if not isinstance(n, int):
#        return False
#    return n % 2 == 0

#try:
#    num = int(input())
#    print(is_even(num))
#except ValueError:
#    print("Ошибка: введено не целое число")

def is_even(num):
    return num % 2 == 0
print(is_even(3))
print(is_even(4))
print(is_even(5))