array = ["СТС", "ТНТ", "РОССИЯ", "ПЯТНИЦА"]
print(array)
s = str(input("Введите название канала: "))
poz = int(input("Введите позицию вашего канала: "))
array.insert(poz - 1, s)
print(array)
