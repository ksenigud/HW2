n = float(input('Введите число: '))

while n % 1 != 0:
    n *= 10
print(n)

sum = 0
while n > 0:
    sum += n % 10
    n //= 10
print(int(sum))