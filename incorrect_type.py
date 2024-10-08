try:
    a, b = map(int, input().split())
    print(a / b)
except ValueError:
    print('Введите два числа')
except ZeroDivisionError:
    print('Деление на 0, введите корретные данные')
