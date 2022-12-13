n = int(input('Enter: '))
sum = 0
a = []
for i in range(1, n + 1):
    a.append((1 + 1/i)** i)
    sum += (1 + 1/i)** i
print(a)
print(round(sum, 3))