P, X, Y, K = int(input()), int(input()), int(input()), int(input())
s = 0
i = 0
while i != K:
    i += 1
    s = (X * 100 + Y) * (100 + P) / 100
    X = int(s // 100)
    Y = int(s - X * 100)
print(X, Y)
