#площадь треугольника
a, b, c = float(input()), float(input()), float(input())
p = (a + b + c) / 2
S = (p * (p - a) * (p - b) * (p - c)) ** (1/2)
if int(S) == S:
    print(int(S))
else:
    print('{0:.6f}'.format(S))
