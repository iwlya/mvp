alfa = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
p = dict.fromkeys(alfa)
i = 1
for c in alfa:
    p[c] = i
    i += 1
print(p)
