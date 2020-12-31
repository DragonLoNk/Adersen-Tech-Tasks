def enter_number(accumulator):
    value = input()
    if value == '':
        print('Ввод закончен, массив:')
        print(*accumulator)
        return
    else:
        try:
            number = int(value)
            accumulator.append(number)
            enter_number(accumulator)
        except ValueError:
            print('Введено не целон число, попробуйте еще раз')
            enter_number(accumulator)


print('Поэлементно введите массив целых чисел. Для завершения ввода введите пустое значение')
entered = []
enter_number(entered)
result = 'Кратные трем числа:'
for item in entered:
    if item % 3 == 0:
        result = result + ' ' + str(item)
print(result)
