X, Y = int(input()), int(input())
count = 1
if X > 0 and Y > 0:
    while True:
        if X < Y:
            X = 1.1 * X
            count = count + 1
        else:
            print(count)
            break
