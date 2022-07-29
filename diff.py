from random import uniform
n=int(input('Введите количество элементов в списке: '))
frst=int(input('Введите нижний предел списка: '))
last=int(input('Введите верхний предел списка: '))
def get_nums (n, frst, last):
    return [round(uniform(frst,last),2) for i in range(n)]

def find_diff(my_nums):
    nums = [round(x - int(x), 2) for x in (my_nums)]
    return max(nums) - min(nums)

my_nums = get_nums(n, frst, last)

print (my_nums)
print(find_diff(my_nums))