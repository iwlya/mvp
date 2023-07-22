def f(n):
    n = int(input())
    if n < 10:
        print("Число меньше требуемого диапозона")
        print("Повторите попытку")
        return f(n)
    elif n > 20:
        print("Число больше требуемого диапозона")
        print("Повторите попытку")
        return f(n)
    elif ((n < 20) & (n > 10)):
        print("Спасибо")

        
print(f(0))
