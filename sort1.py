#осортировка трех чисел только через if
a, b, c = int(input()), int(input()), int(input())
if b < a:
    b, a = a, b
if c < a:
    c, a = a, c
if c < b:
    c, b = b, c
print(a, b, c)
