#соотношение двух коробок (можно ли поместить одну внутри другой)
a1, b1, c1 = int(input()), int(input()), int(input())
a2, b2, c2 = int(input()), int(input()), int(input())
if c1 > 0 and c2 > 0 and b1 > 0 and b2 > 0 and a1 > 0 and a2 > 0:
    if b1 < a1:
        b1, a1 = a1, b1
    if c1 < a1:
        c1, a1 = a1, c1
    if c1 < b1:
        c1, b1 = b1, c1
    if b2 < a2:
        b2, a2 = a2, b2
    if c2 < a2:
        c2, a2 = a2, c2
    if c2 < b2:
        c2, b2 = b2, c2
    if c2 == c1 and a2 == a1 and b1 == b2:
        print("Boxes are equal")
    elif c2 >= c1 and b2 >= b1 and a2 >= a1:
        print("The first box is smaller than the second one")
    elif c1 >= c2 and b1 >= b2 and a1 >= a2:
        print("The first box is larger than the second one")
    else:
        print("Boxes are incomparable")
else:
    print("Boxes are incomparable")
