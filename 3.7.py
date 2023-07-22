a = str(input("введите строку: "))
p = dict.fromkeys(a)
for i in a:
    if i in "приаолвы":
        p[i] = "True"
    elif i in "авлопилы":
        p[i] = "False"
    else:
        del p[i]
print(p)
