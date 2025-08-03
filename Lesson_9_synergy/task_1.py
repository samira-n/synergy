n = int(input())
numbers = list(map(int, input().split()))
unique_numbers = set(numbers)  # Убираем дубликаты
print(len(unique_numbers))     # Количество уникальных чисел