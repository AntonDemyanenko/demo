# Считываем список чисел
numbers = list(map(int, input().split()))

# Считываем число, которое нужно удалить
delete = int(input())

# Формируем новый список без всех вхождений этого числа
result = [x for x in numbers if x != delete]

# Выводим оставшиеся числа через пробел
print(*result)