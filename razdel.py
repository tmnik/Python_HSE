A, B = int(input()), int(input())
while A != B:
    if A % 2 == 0 and A // 2 >= B:
        print(':2')
        A = A // 2
    else:
        A -= 1
        print('-1')
