a, b, c = int(input()), int(input()), int(input())
if b < a:
    b, a = a, b
if c < a:
    c, a = a, c
if c < b:
    c, b = b, c
if a + b > c:
    if a * a + b * b == c * c:
        print("rectangular")
    elif a * a + b * b > c * c:
        print("acute")
    elif a * a + b * b < c * c:
        print("obtuse")
else:
    print("impossible")
