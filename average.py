#найти среднее последовательности
n = int(input())
i = 0
s = n
while True:
    if n == 0:
        break
    n = int(input())
    i += 1
    s += n
av = s / i
print(av)
