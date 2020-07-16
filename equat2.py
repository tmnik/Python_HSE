from math import sqrt
a, b, c = float(input()), float(input()), float(input())

eps = 5e-7
if a != 0 and b == 0:
    if a * c <= 0:
        x1 = sqrt(- c / a)
        print('1', x1)
    else:
        print('0')
elif a != 0 and b != 0:
    D = b ** 2 - 4 * a * c
    if D >= 0:
        x1 = (- b + sqrt(D)) / (2 * a)
        x2 = (- b - sqrt(D)) / (2 * a)
        if x1 - x2 > eps:
            x1, x2 = x2, x1
        if D == 0:
            print('1', x1)
        else:
            print('2', x1, x2)
    else:
        print('0')
elif a == 0 and b != 0:
    x1 = - c / b
    print('1', x1)
elif a == b == c == 0:
    print('3')
else:
    print('0')
