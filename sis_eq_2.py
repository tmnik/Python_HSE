a, b = float(input()), float(input())
c, d = float(input()), float(input())
e, f = float(input()), float(input())
eps = 5e-7
if a == 0 and b == 0 and e == 0:
    if c == 0 and d == 0 and f == 0:
        print(5)
    else:
        print(0)
elif c == 0 and d == 0 and f == 0:
    if a == 0 and b == 0 and e == 0:
        print(5)
    else:
        print(0)
elif a == 0 and b == 0 and e != 0:
    print(0)
elif c == 0 and d == 0 and f != 0:
    print(0)
elif f == 0 and e == 0 and b != 0 and c != 0:
    if d / b - a / c <= eps:
        print(0)
    else:
        x0 = (e * d - b * f) / (a * d - b * c)
        y0 = (a * f - e * c) / (a * d - b * c)
        print(2, x0, y0)
elif f != 0 and e != 0:
    u1 = a / e - c / f
    u2 = b / e - d / f
    if b == 0 and d == 0 and u1 <= eps and a != 0:
        x0 = e / a
        print(3, x0)
    elif a == 0 and c == 0 and u2 <= eps and b != 0:
        y0 = e / b
        print(4, y0)
    elif a * d - b * c != 0:
        x0 = (e * d - b * f) / (a * d - b * c)
        y0 = (a * f - e * c) / (a * d - b * c)
        print(2, x0, y0)
    elif u1 <= eps and u2 <= eps:
        if b != 0 and e - f != 0:
            p = - a / b
            q = e / b
            print(1, p, q)
        else:
            print(0)
elif a * d - b * c != 0:
    x0 = (e * d - b * f) / (a * d - b * c)
    y0 = (a * f - e * c) / (a * d - b * c)
    print(2, x0, y0)
else:
    print(0)
