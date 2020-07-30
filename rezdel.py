n = int(input())
a = 0
b = 1
c = 0
i = 0
while a < n:
    c = b
    b = a + b
    a = c
    i += 1
if a == n:
    print(i)
else:
    print(-1)
