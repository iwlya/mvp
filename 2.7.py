k = 0
while True:
    n = int(input("Введите число: "))
    if (n > 0):
        print("Число не отрицательное")
        break
    k += n
    print("Сумма чисел равна:", k)
