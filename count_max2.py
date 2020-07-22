#вывести наибольшая количество одинаковых чисел
n = int(input())
i1 = 1
k = 0
m = n
while n != 0:
    n = int(input())
    if m == n:
        i1 += 1
    if i1 > k:
        k = i1
    elif m != n:
        i1 = 1
    m = n
print(k)
