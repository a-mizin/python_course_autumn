from math import sqrt

user_value = float(input())

try:
    print(f'Квадратный корень из числа {user_value} равен {sqrt(user_value)}')
except ValueError:
    print(f'Невозможно вычислить корень из числа {user_value}')
except NameError:
    print(f'Не получилось найти функцию sqrt')
