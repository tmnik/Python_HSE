s = input()
pos1 = s.find('h')
pos2 = s.rfind('h')
s2 = s[pos1 + 1:pos2]
r2 = s2.replace('h', 'H')
print(s[:pos1 + 1], r2, s[pos2:], sep='')
