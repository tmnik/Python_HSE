s = input()
pos1 = s.find('h')
s1 = s[::-1]
pos2 = s1.find('h')
pos2 = len(s) - pos2 - 1
print(s[:pos2], s[pos1 + 1:], sep='')
