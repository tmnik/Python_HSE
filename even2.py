#определить есть ли среди чисел хотя бы одно четное и хотя бы одно нечетное число
a, b, c = int(input()), int(input()), int(input())
a1 = a % 2
b1 = b % 2
c1 = c % 2
d = a * b * c
if (a1 == 0 and b1 == 0 and c1 == 0) or d % 2 == 1:
    print("NO")
else:
    print("YES")
