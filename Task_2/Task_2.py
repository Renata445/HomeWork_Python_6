array = [1, 3, 6, 9, 11, 19, 25]
max_number = int(input('Введите максимальное число: '))
min_number = int(input('Введите минимальное число: '))
for i in range(len(array)):
    if min_number <= array[i] <= max_number:
        print(i)