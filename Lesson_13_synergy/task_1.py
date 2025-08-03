import random

def generate_matrix(rows, cols):
    """Генерация матрицы заданного размера со случайными числами"""
    return [[random.randint(-100, 100) for _ in range(cols)] for _ in range(rows)]

def add_matrices(matrix1, matrix2):
    """Сложение двух матриц одинакового размера"""
    # Проверка, что матрицы одинакового размера
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Матрицы должны быть одинакового размера для сложения")
    
    # Создание результирующей матрицы
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

# Создаем две матрицы 10x10
matrix_1 = generate_matrix(10, 10)
matrix_2 = generate_matrix(10, 10)

# Складываем матрицы
matrix_3 = add_matrices(matrix_1, matrix_2)

# Выводим результаты (можно закомментировать для больших матриц)
print("Матрица 1:")
for row in matrix_1:
    print(row)

print("\nМатрица 2:")
for row in matrix_2:
    print(row)

print("\nРезультат сложения (Матрица 3):")
for row in matrix_3:
    print(row)