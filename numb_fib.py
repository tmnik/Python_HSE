n = int(input())
a = 0
b = 1
c = 0
i = 0
while i != n:
    c = b
    b = a + b
    a = c
    i += 1
print(a)
