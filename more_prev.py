#сколько членов последовательности больше предыдущих. 0  не считаем
n = int(input())
p = 0
i = 0
while i != -1:
    if n == 0:
        break
    p = n
    n = int(input())
    if n != 0 and n > p:
        i += 1
print(i)
