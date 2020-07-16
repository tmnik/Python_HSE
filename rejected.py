from math import sqrt
x = int(input())
i = 0
n_sum = 0
n_sum2 = 0
while x != 0:
    i += 1
    n_sum += x
    n_sum2 += x * x
    x = int(input())
s = n_sum * n_sum / i
sigma = sqrt((n_sum2 - s) / (i - 1))
print(sigma)
