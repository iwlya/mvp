import csv

s = ["Книга", "Автор", "Год выпуска"]
books = [
    ["Не мешай себе жить", "Марк Гоулстон", "1996"],
    ["Аленький цветочек", "Сергей Аксаков", "1857"],
    ["Богатый папа, бедный папа", "Роберт Кийосаки", "2001"],
    ["Песня о соколе", "Максим Горький", "1895"],
    ["Мцыри", "М.Ю.Лермонтов", "1840"],
]
with open("books.csv", "w", encoding="utf-8-sig", newline='') as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(s)
for book in books:
    with open("books.csv", "a", encoding="utf-8-sig", newline='') as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(
            book
        )
