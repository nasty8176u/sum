n = int(input('Введите число: '))

def get_list(n):
    numbers = []
    a, b = 1, 1
    for i in range(n-1):
        numbers.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (n):
        numbers.insert(0, a)
        a, b = b, a - b
    return numbers

numbers = get_list(n)
print(get_list(n))
