#максимальный элемент поседователньости
numb = int(input())
max_el = numb
i = 1
while i > 0:
    numb = int(input())
    if numb > max_el:
        max_el = numb
    if numb == 0:
        print(max_el)
        break
    i = i + 1
