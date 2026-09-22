n = int(input())

# Сумма всех чисел от 1 до n по формуле арифметической прогрессии
total_sum = n * (n + 1) // 2

# Суммируем номера оставшихся карточек
remaining_sum = 0
for _ in range(n - 1):
    card_number = int(input())
    remaining_sum += card_number

# Потерянная карточка — разница между полной и текущей суммой
missing_card = total_sum - remaining_sum
print(missing_card)

