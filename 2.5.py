import random


def f():
    a = "Орел"
    b = "Решка"
    s = random.randint(0, 2)
    if (n != 1 or n != 0): print("Конец игры...")
    elif (s == n):
        if s == 1:
            print("Верно.", b)
        elif s == 0:
            print("Верно.", a)
    elif (s != n):
        if s == 1:
            print("Неверно.", b)
        elif s == 0:
            print("Неверно.", a)


f()
