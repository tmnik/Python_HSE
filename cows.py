#сколько коров пасется на лугу. Изменять окончания в зависимости от количества
n = int(input())
if 5 <= n <= 20 or n % 10 == 0:
    print(n, ' korov', sep='')
elif n % 10 == 1:
    print(n, ' korova', sep='')
elif 2 <= n % 10 <= 4:
    print(n, ' korovy', sep='')
else:
    print(n, ' korov', sep='')
