s = input()
pos1 = s.find('h')
s1 = s[::-1]
pos2 = s1.find('h')
pos2 = len(s) - pos2 - 1
print(s[:pos1], s[pos2 + 1:], sep='')
