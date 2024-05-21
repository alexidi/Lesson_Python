array = []
array_1 = []
n = int(input('Введите длину массива 1: '))
for _ in range(n):
    array.append(int(input()))
m = int(input('Введите длину массива 2: '))
for _ in range(m):
    array_1.append(int(input()))
new_array = []
for i in array:
    if i not in array_1:
        new_array.append(i)
print(new_array)
