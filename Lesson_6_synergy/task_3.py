A = int(input("Введите A: "))
B = int(input("Введите B: "))

# Находим первое чётное число >= A
start = A if A % 2 == 0 else A + 1

# Выводим чётные числа от start до B с шагом 2
if start <= B:
    print(*range(start, B + 1, 2))
else:
    print("Нет чётных чисел в этом диапазоне")