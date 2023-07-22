a, b = map(int, input("Введите значения чисел: ").split())
k = 0
for i in range(a, b + 1):
    k += i
print("Сумма чисел равна:", k)
