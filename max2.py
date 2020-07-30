n = int(input())
max_n = n
max2 = n
i = 1
while n != 0:
    n = int(input())
    if n == 0:
        break
    if i == 1:
        max2 = n
    if n > max_n:
        max2 = max_n
        max_n = n
    elif n > max2:
        max2 = n
    i += 1
print(max2)
