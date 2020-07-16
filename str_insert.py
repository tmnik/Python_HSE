s = input()
i = 0
k = 0
while i <= (len(s) - 1):
    i += 3
    print(s[k + 1:i], end='')
    k = i
