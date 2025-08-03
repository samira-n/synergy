# Чтение первого списка
n = int(input())
list1 = [int(input()) for _ in range(n)]

# Чтение второго списка
m = int(input())
list2 = [int(input()) for _ in range(m)]

# Преобразование в множества и нахождение пересечения
set1 = set(list1)
set2 = set(list2)
common_elements = set1 & set2

# Вывод количества общих элементов
print(len(common_elements))