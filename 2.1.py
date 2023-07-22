import random


def gc():
    colors = ["Красный", "Черный", "Белый", "Желтый", "Фиолетовый"]
    while True:
        print(colors, "\n", "Выберите цвет")
        random_color = random.choice(colors)
        while True:
            s = str(input())
            if s == random_color:
                print("Отлично")
                break
            else:
                print("Неверно. Цвет начинается с", random_color[0] + "...")


gc()
