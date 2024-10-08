from random import randint
from random import sample
from typing import List


def get_value(l: List[int], index: int):
    try:
        return l[index]
    except IndexError:
        print(f'Выход за пределы списка: всего элементов - {len(l)}, индекс - {index}')


LIST_SIZE = 10

data = sample(range(-3, 10), LIST_SIZE)
index = randint(0, LIST_SIZE + 3)

print(f'Число по индексу {index} из списка {data} это: {get_value(data, index)}')
