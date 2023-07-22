def f():
    n = int(input())
    if n == 3:
        print("Команда выиграла")
        return f(n)
    elif n == 0:
        print("Команда проиграла")
        return f(n)
    elif n == 1:
        print("Команда сыграла в ничью")
        return f(n)
    else:
        print("Нет такого результата")
        return f(n)


f()
