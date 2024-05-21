arr = [2, 4, 6, 8, 10]
max1 = 0
arr_mod = arr[-2:] + arr[:] + arr[:2]
for i in range(1, len(arr_mod) - 1):
    if arr_mod[i - 1] + arr_mod[i] + arr_mod[i + 1] > max1:
        max1 = arr_mod[i - 1] + arr_mod[i] + arr_mod[i + 1]
print(max1)
print(arr[-2:])
print(arr[:])
print(arr[:2])
print(arr[-2:] + arr[:] + arr[:2])
