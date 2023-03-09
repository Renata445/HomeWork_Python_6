a1, diff, n = int(input('Введите 1-ый элемент: ')), int(input('Введите разность: ')), int(input('Введите кол-во элементов: '))
progressive = [a1 + (i - 1) * diff for i in range(1, n + 1)]
print(progressive)