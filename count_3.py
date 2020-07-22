n = int(input())
i1 = 1
i2 = 1
k = 0
m = n
while n != 0:
    n = int(input())
    if n == 0:
        break
    if m > n:
        i1 += 1
    elif i1 > k and i1 > i2:
        k = i1
        i2 = 0
    elif m < n:
        i2 += 1
    elif i2 > k and i2 > i1:
        k = i2
        i1 = 0
    elif m == n:
        i1 = 0
        i2 = 0
    m = n
print(k)
