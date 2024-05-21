array = []
n = int(input('Введите длину массива: '))
for _ in range(n):
    array.append(int(input()))
print(array)
count = 0
for i in range(1, len(array) - 1):
    if array[i] > array[i - 1] and array[i] > array[i + 1]:
        count += 1
print(f'Число совпадений: {count}')
