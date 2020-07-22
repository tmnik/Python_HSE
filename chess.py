#может ли король из первой клетки попасть во вторую, если кароль ходит только на одну клетку в любом направлении
n1 = int(input())
k1 = int(input())
n2 = int(input())
k2 = int(input())
hor1 = k1 + 1 == k2
hor2 = k1 - 1 == k2
hor3 = k1 == k2
hor = hor1 or hor2
upr1 = n1 + 1 == n2
upr2 = n1 - 1 == n2
upr3 = n1 == n2
upr = upr1 or upr2
st = upr3 and hor3
if 1 <= n1 <= 8 and 1 <= n2 <= 8 and 1 <= k1 <= 8 and 1 <= k2 <= 8:
    if (upr and (hor or hor3)) or (hor and (upr or upr3)) or st:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
