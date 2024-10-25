from math import sqrt

x_int = 100
y_int = 50


def add_numbers(x_int, y_int):
    return int(x_int) + int(y_int)


def CalculateSquareRoot(Number):
    return sqrt(Number)


def calc(your_number):
    if your_number <= 0:
        your_number = 0
    total = CalculateSquareRoot(your_number)
    tot = (f'Мы вычислили квадратный корень из введённого Вами числа.'
           f'Это будет: {total}'
           )
    return tot


print('Сумма чисел:', add_numbers(x_int, y_int))
print(calc(25.5))
