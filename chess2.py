#одного ли цвета клетки шахматной доски
n1, k1 = int(input()), int(input())
n2, k2 = int(input()), int(input())
n2n1 = (n2 + n1) % 2
k2k1 = (k2 + k1) % 2
if 1 <= n1 <= 8 and 1 <= n2 <= 8 and 1 <= k1 <= 8 and 1 <= k2 <= 8:
    if (n2n1 == 0 and k2k1 == 0) or (k2k1 == 1 and n2n1 == 1):
        print('YES')
    else:
        print('NO')
else:
    print('NO')
