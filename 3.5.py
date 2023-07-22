def s(a):
    k = 0
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            k = k + 1
    if k <= 0:
        return a


m = [s(i) for i in range(1, 100)]
print(m)
