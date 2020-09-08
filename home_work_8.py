import time
import random
import sys

# 1. Написать декоратор, замеряющий время выполнения декорируемой функции.
print()
print('Задание 1. Декоратор, замеряющий время выполнения декорируемой функции.')
print()

def show_time(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        f(*args, **kwargs)
        stop_time = time.time()
        print('Время выполнения функции: {}'.format(stop_time - start_time))
    return wrapper

@show_time
def get_ocean():
    ocean_board = []
    for x in range(60):
        ocean_board.append([])
        for y in range(15):
            if random.randint(0,1) == 0:
                ocean_board[x].append('/')
            else:
                ocean_board[x].append('#')
    for row in range(15):
        board_row = ''
        for column in range(60):
            board_row += ocean_board[column][row]
        print(board_row)

get_ocean()



#2. Сравнить время создания генератора и списка с элементами:
# натуральные числа от 1 до 1000000 (создание объектов оформить в виде функций).

# 4. Сравнить объем оперативной памяти для функции создания
# генератора и функции создания списка с элементами: натуральные числа от 1 до 1000000.
print()
print('Задание 2. Сравнить время создания генератора и списка.')
print('Задание 4. Сравнить объем оперативной памяти.')
print()


def time_list_of_numbers(n):
    list_of_numbers = [i for i in range(n)]
    return list_of_numbers

start_time = time.time()
func_list = time_list_of_numbers(1000001)
stop_time = time.time()
time_list = stop_time - start_time
memory_list = sys.getsizeof(func_list)
print('Время создания списка с элементами от 1 до 1000000: {}.\nОбъем оперативной памяти: {}'.format(time_list, memory_list))

def time_generator_of_numbers(n):
    for i in range(n):
        yield(i)

start_time = time.time()
func_gen = time_generator_of_numbers(1000001)
stop_time = time.time()
time_gen = stop_time - start_time
memory_gen = sys.getsizeof(func_gen)
print('Время создания генератора с элементами от 1 до 1000000: {}.\nОбъем оперативной памяти: {}'.format(time_gen, memory_gen))

if time_list - time_gen > 0:
    print('Генератор создался быстрее.')
else:
    print('Список создался быстрее.')

if memory_list - memory_gen > 0:
    print('Список занимает больше оперативной памяти.')
else:
    print('Генератор занимает больше оперативной памяти.')


# 3. Написать декоратор, замеряющий объем оперативной памяти, потребляемый декорируемой функцией.
print()
print('Задание 3. Декоратор, замеряющий объем оперативной памяти, потребляемый декорируемой функцией.')

def show_memory(f):
    def wrapper(*args, **kwargs):
        print(f(*args, **kwargs))
        print('Объем занимаемой памяти: ', sys.getsizeof(f))
    return wrapper

@show_memory
def random_number(a, b):
    '''
    :param a:
    :param b:
    :return: возвращает случайное натуральное число от a до b
    '''
    x = random.randint(a, b)
    return x

random_number(1, 1000000)
random_number(1, 1000000000)
random_number(1, 1000000000000000)