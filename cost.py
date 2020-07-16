#стоимость в руб и копейках
n = float(input())
a = float('{0:.2}'.format(n - int(n)))
d = (a * 100) // 1
print(int(n), int(d))
