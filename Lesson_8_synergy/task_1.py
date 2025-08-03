N = int(input())
numbers = [int(input()) for _ in range(N)]
reversed_numbers = numbers[::-1] 
print('\n'.join(map(str, reversed_numbers)))