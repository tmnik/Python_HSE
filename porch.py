#может ли быть так, что х номер певрой квартиры в подезде, а y последней
x = int(input())
y = int(input())
if x <= y:
    if (x - 1) % (y - x + 1) == 0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
