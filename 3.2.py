m = int(input("Введите число: "))


def fib(n):

    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_list = [0, 1]

        for i in range(2, n + 1):
            if fib_list[i - 1] + fib_list[i - 2] < n:
                fib_list.append(fib_list[i - 1] + fib_list[i - 2])
            else:
                break
    return fib_list


print((lambda k: fib(m))(m))
