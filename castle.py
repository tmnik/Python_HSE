#известно размер прямоугольного отверстия и размер кирпича. Можно ли из отвесртия выкинуть кирпич? Только if
A, B, C = int(input()), int(input()), int(input())
D, E = int(input()), int(input())
if A > 0 and B > 0 and C > 0 and D > 0 and E > 0:
    if D >= A:
        if E >= B or E >= C:
            print("YES")
        else:
            print("NO")
    elif D >= B:
        if E >= A or E >= C:
            print("YES")
        else:
            print("NO")
    elif D >= C:
        if E >= A or E >= B:
            print("YES")
        else:
            print("NO")
    elif E >= A:
        if D >= B or D >= C:
            print("YES")
        else:
            print("NO")
    elif E >= B:
        if D >= A or D >= C:
            print("YES")
        else:
            print("NO")
    elif E >= C:
        if D >= A or D >= B:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
else:
    print('NO')