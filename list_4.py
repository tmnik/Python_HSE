N = int(input())
i = 1
k = 0
if N > 0:
    while True:
        if i < N:
            i = 2 * i
            k = k + 1
        else:
            print(k)
            break
