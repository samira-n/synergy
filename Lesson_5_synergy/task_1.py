num = int(input("Введите целое число: "))

if num == 0:
    print("нулевое число")
else:
    #Определям положительное или отрицательное
    if num > 0:
        sign = "положительное"
    else:
        sign = "отрицательное"

    #Проверяем четность
    if num % 2 == 0:
        parity = "четное"
        print(sign, parity, "число")   
    else:
        parity = "нечетное"
        print(sign, parity, "число")  
        print("число не является четным")


