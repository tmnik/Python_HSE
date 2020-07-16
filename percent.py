#найти вклад через год, если дан вклад на данный момоент в руб и копейках и процент P
P, X, Y = int(input()), int(input()), int(input())
s = ((X * 100 + Y) * (100+P) / 100)
rub = s // 100
pen = s % 100
print(int(rub), int(pen))
