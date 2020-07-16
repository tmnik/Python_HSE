#округление по русским правилам
from math import floor, ceil
n = float(input())
r = n - int(n)
a = float('{0:.1}'.format(0.5))
if r >= a:
    print(ceil(n))
elif r < a:
    print(floor(n))
