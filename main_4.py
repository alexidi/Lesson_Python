def get_sum(n):
    my_sum = 1
    for el in range(2, n // 2 + 1):
        if n % el == 0:
            my_sum += el
    return my_sum


def get_friendlies(k):
    lst = []
    for n in range(1, k + 1):
        if n not in lst:
            m = get_sum(n)
            if n == get_sum(m) and n != m:
                lst.append(n)
                lst.append(m)
    return lst


print(get_friendlies(2000))
