n = int(input())
arr = list(map(int, input().split()))
if n > 1:
    last = arr.pop()  # Удаляем последний элемент
    arr.insert(0, last)  # Вставляем его в начало
print(' '.join(map(str, arr)))