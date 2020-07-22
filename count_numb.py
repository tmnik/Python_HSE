#количество чисел до 0
n = int(input())
i = 0
while i > -1:
    if n == 0:
        break
    i += 1
    n = int(input())
print(i)
