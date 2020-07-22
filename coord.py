#в одной ли координатной плоскости точки
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
x1x2 = x1 * x2
y1y2 = y1 * y2
if x1x2 >= 0:
    if y1y2 >= 0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
