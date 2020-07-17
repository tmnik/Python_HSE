#Дана блина мкада 109 км. Машина стартуем со скорость V с нулевой отметки. На какой отметке она будет через t
V = int(input())
t = int(input())
dist = V * t
n = V // V
point = n * dist % 109
print(point)
