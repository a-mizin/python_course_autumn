a, b = map(int, input().split())

try:
    print(a / b)
except ZeroDivisionError:
    print('Деление на 0, введите корретные данные')
