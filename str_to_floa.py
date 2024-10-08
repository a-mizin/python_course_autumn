user_input = input()

float_value = None
try:
    float_value = float(user_input)
except ValueError:
    print(f'Переданную строку {user_input} нельзя преобразовать в float')

if float_value is not None:
    print('Преобразованное число: ', float_value)
