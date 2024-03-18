number = int(input('Введите число:'))
if (number % 2 == 0) and (number < 0):
    print('это чётное отрицательное число')
elif (number % 2 == 0) and (number > 0):
    print('это чётное положительное число')
elif (number != 0) and (number < 0):
    print('это нечётное отрицательное число')
elif (number % 2 != 0) and (number > 0):
    print('это нечётное положительное число')
else:
    print('это нулевое число')


