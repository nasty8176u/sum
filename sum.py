from random import randint
n=int(input('Введите количество символов, которое вы хотите получить в списке: '))
ft = int(input('Введите нижний предел чисел, из которых будет составлен список: '))
lt = int(input('Введите верхний предел чисел, из которых будет составлен список: '))
def new_list(n, ft, lt):
    return [randint(ft, lt) for i in range(n)]

def sum_position(my_list):
    return sum(my_list[1::2])
my_list = new_list(n, ft, lt)
print(my_list)
print('Сумма элементов на нечетных позициях равна ',sum_position(my_list))

