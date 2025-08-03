N = int(input("Введите количество чисел: "))
count_zero = 0  # Счётчик нулей

for i in range(N):
    num = int(input("Введите число: "))
    if num == 0:
        count_zero += 1

print(f"Количество нулей: {count_zero}")