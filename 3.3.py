s = int(input("Введите число: "))
print((lambda k: print("Четное") if s % 2 == 0 else print("Нечетное"))(s))
