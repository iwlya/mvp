a, b, c = map(int, input("Введите значения коэффицнетов a, b, c:\n").split())
d = b ** 2 - 4 * a * c
if d < 0:
    print("Нет корней")
elif d == 0:
    x = - b / (2 * a)
    print("Один корень\n", "Корень уравнения:", x)
else:
    x1 = (- b - sqrt(d)) / (2 * a)
    x2 = (- b + sqrt(d)) / (2 * a)
    print("Два корня уравнения\n", "Корни уравнения:", x1, x2)
