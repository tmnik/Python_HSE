#схема Горнера
n, x = int(input()), float(input())
a = float(input())
i = 1
P = a
while i != n + 1:
    a = float(input())
    P = P * x + a
    i += 1
print(P)
