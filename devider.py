N = int(input())
i = 2
while i > 1:
    ost = N % i
    if ost == 0:
        print(i)
        break
    else:
        i = i + 1
