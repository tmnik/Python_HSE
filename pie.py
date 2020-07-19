#Дана цена пирожков в А руб.В коп. и сколько их надо купить N. Сколько нужно заплатить?
A = int(input())
B = int(input())
N = int(input())
cost = N * (A * 100 + B)
print(cost // 100, cost % 100)
