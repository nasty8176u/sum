from random import randint
import math
n=int(input('Введите количество элементов в списке: '))
frst=int(input('Введите нижний предел списка: '))
last=int(input('Введите верхний предел списка: '))
def new_numbers(n, frst, last):
    return [randint(frst, last) for i in range(n)]

def mult(my_list):
    return [my_list[i] * my_list[-i - 1] for i in range(math.ceil(len(my_list)/2))]
my_list = new_numbers(n, frst, last)
print(my_list)
print(mult(my_list))

