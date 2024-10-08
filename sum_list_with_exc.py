from random import sample
from typing import List


class OddNumberException(Exception):
    pass


class NegativeNumberException(Exception):
    pass


def sum(l: List[int]):
    s = 0
    for value in l:
        if value % 2 == 0:
            raise OddNumberException('Встретилось четное число')
        if value < 0:
            raise NegativeNumberException('Встретилось отрицательное число')
        s += value

    return s


data = sample(range(-3, 10), 5)

print(f'Список: {data}')
print(f'Сумма элементов: {sum(data)}')
