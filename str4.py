s = input()
pos1 = s.find(' ')
print(s[pos1 + 1:], s[:pos1], sep=' ')
