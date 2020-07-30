#наибольшее число из 3
x1 = int(input())
x2 = int(input())
x3 = int(input())
if x1 >= x2 and x1 >= x3:
    print(x1)
elif x2 >= x1 and x2 >= x3:
    print(x2)
elif x3 >= x1 and x3 >= x2:
    print(x3)
