X = int(input("Введите натуральное число X: "))
count = 0
sqrt_X = int(X ** 0.5)  # Корень из X для оптимизации

for i in range(1, sqrt_X + 1):
    if X % i == 0:
        if i * i == X:
            count += 1  # Квадратный корень — один делитель
        else:
            count += 2  # Пара делителей: i и X // i

print(f"Количество натуральных делителей числа {X}: {count}")