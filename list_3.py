#степень двйки не превосходящая N
N = int(input())
i = 1
if N > 0:
    while True:
        if i >= N:
            if i == N:
                print("YES")
                break
            elif i > N:
                print("NO")
                break
        else:
            i = 2 * i

