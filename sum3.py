# numbers = list(map(int, input().split()))
# numbers.sort(reverse = True)
# # summa = numbers[-1] + numbers[-2] + numbers[-3]
# print(sum(numbers[:3]))


s = input()

# Разбиваем строку по запятой, для каждого элемента:
# 1. убираем пробелы по краям (strip)
# 2. приводим к нижнему регистру (lower)
# 3. добавляем в множество (set), чтобы оставить только уникальные
unique_words = {word.strip().lower() for word in s.split(',') if word.strip()}

print(len(unique_words))
