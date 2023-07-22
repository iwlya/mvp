array = ["СТС", "ТНТ", "РОССИЯ", "ПЯТНИЦА"]
print(array)
s = str(input("Введите название канала:\n"))
poz = int(input("Введите позицию вашего канала:\n"))
array.insert(poz - 1, s)
print(array)
