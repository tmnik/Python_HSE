s = input()
pos1 = s.find('f')
if pos1 == -1:
    print(-2)
else:
    pos2 = s.find('f', pos1 + 1)
    print(pos2)
