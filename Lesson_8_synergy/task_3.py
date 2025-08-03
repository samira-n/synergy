m = int(input())  # Максимальный вес лодки
n = int(input())  # Количество рыбаков
weights = [int(input()) for _ in range(n)]  # Веса рыбаков
weights.sort()  # Сортируем веса

left = 0
right = n - 1
boats = 0

while left <= right:
    if weights[left] + weights[right] <= m:
        left += 1  # Сажаем легкого и тяжелого
    right -= 1  # Тяжелого всегда везем
    boats += 1

print(boats)