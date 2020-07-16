from math import sqrt
a, b, c = float(input()), float(input()), float(input())
D = b**2 - 4 * a * c
eps = 5e-7
if D >= 0:
    x1 = (- b + sqrt(D)) / (2 * a)
    x2 = (- b - sqrt(D)) / (2 * a)
    if x1 - x2 > eps:
        x1, x2 = x2, x1
        print(x1, x2)
    elif x2 - x1 > eps:
        print(x1, x2)
    else:
        print(x1)
