a, b, c = map(int, input().split())
s = [a,b,c]
print("Максимальный элемент:",  max(s))
s = sorted(s)
s.reverse()
print(s)
