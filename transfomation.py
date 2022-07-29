n = int(input('Введите число: '))
def transformation(n):
    number = ''
    while n > 1:
        number += str(n % 2)
        n = n // 2
    return number[::-1]

print('В десятичном варианте число равно',transformation(n))
