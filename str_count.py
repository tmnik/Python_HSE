s = input()
pos1 = s.find('f')
s1 = s[::-1]
pos2 = s1.find('f')
pos2 = len(s) - pos2 - 1
if pos1 == pos2 and pos1 != -1:
    print(pos1)
elif pos1 != -1 and pos2 != -1:
    print(pos1, pos2)
