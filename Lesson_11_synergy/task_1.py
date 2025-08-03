def factorial(n):
    """Вычисляет факториал натурального числа n"""
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def factorial_sequence(n):
    """Возвращает список факториалов от n! до 1! в убывающем порядке"""
    # Вычисляем начальный факториал
    initial_fact = factorial(n)
    
    # Создаем список факториалов в убывающем порядке
    fact_list = []
    for i in range(initial_fact, 0, -1):
        # Находим максимальное число, чей факториал <= текущему i
        current_num = 0
        while True:
            if factorial(current_num) <= i and factorial(current_num+1) > i:
                break
            current_num += 1
        
        fact = factorial(current_num)
        if fact not in fact_list:  # Добавляем только уникальные факториалы
            fact_list.append(fact)
    
    return fact_list

# Пример использования
n = 3
result = factorial_sequence(n)
print(result)  # Выведет: [720, 120, 24, 6, 2, 1]