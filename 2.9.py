s = str(input("Введите число: "))
md = 0
mpfs = 0
mpfe = 0
for i in range(len(s)):
    d = int(s[i])
    pfs = i + 1
    pfe = len(s) - i
    if d > md:
        md = d
        mpfe = pfe
        mpfs = pfs
print("Номер максималой цифры с начала:", mpfs)
print("Номер максимальной цифры с конца:", mpfe)
