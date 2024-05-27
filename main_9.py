a = int(input('Введите количество столбцов: '))
b = int(input('Введите количество строк: '))


def print_operation_table(operation, num_rows, num_columns):
    if num_rows and num_columns <= 2:
        print("ОШИБКА! Размерности таблицы должны быть больше 2!")
    else:
        y = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
        for i in y:
            print(*[f"{x:>3}" for x in i])


print_operation_table(lambda x, y: x * y, a, b)
