#Упр2. По найденному числу найти сумму ряда
n = int(input())
i = 0
s = 0
while i != n:
    i += 1
    s = s + 1/(i**2)
print(s)
