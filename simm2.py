a = int(input())
a1 = a // 1000
a4 = a % 10
a2 = (a // 100) % 10
a3 = (a % 100) // 10
n1 = (a1 * 10 + a2) % 100
n2 = (a4 * 10 + a3) % 100
at = n1 - n2 + 1
print(at)
