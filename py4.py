# Задание 1

n = int(input('Введите кол-во чисел: '))
count = 0
for i in range(n):
    y = int(input())
    if y == 0:
        count += 1
print(count)

# Задание 2 

x = int(input())
count_1 = 0
for i in range(1, x+1):
    if x % i == 0:
        count_1 += 1
print(count_1)

# Задание 3

a = int(input('Введите меньшее число: '))
b = int(input('Введите большее число: '))

for i in range(a, b+1):
    if (i % 2 == 0):
        print(i, end=' ')

input()