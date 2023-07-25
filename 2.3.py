def f():
    while True:
        arm = str(input("Введите число для проверки: "))
        k = 0
        for i in range(len(arm)):
            k += int(arm[i]) ** len(arm)
        if k == int(arm):
            print("Число является числом Армстронга\n")
        else:
            print("Число не является числом Армтстронга\n")


f()
