#известно размер прямоугольного отверстия и размер кирпича. Можно ли из отвесртия выкинуть кирпич? Только if, сортировка.
A, B, C = int(input()), int(input()), int(input())
D, E = int(input()), int(input())
if A > 0 and B > 0 and C > 0 and D > 0 and E > 0:
    if D < E:
        D, E = E, D
    if B < A:
        B, A = A, B
    if C < A:
        C, A = A, C
    if C < B:
        C, B = B, C
    if D >= C:
        if E >= B or E >= A:
            print("YES")
        else:
            print("NO")
    elif D >= B:
        if E >= A:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
else:
    print('NO')
