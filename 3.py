i = str(input("введите элементы через пробел: "))
l = i.split(" ")
print(l)
for i in range(0, len(l) - 2, 2):
    k = l[i]
    l[i] = l[i + 2]
    l[i + 2] = k
    i += 1
for i in range(0, len(l) - 2, 1):
    k = l[i]
    l[i] = l[i + 2]
    l[i + 2] = k
    i += 1
print(l)