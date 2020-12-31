print('Введите целое число')
try:
    number = int(input())
    if number > 7:
        print('Привет')
except ValueError:
    print('Введено не число')
