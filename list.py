N = int(input())
numb = 1
i = 0
if N > 0:
    while i <= N:
        i = numb * numb
        if i <= N:
            numb = numb + 1
            print(i, end=' ')
elif N == 0:
    print(i)
