print('Введите последовательность и выберите опции алгоритма. Для активации опции отвечайте "да"')
line = input()
print('Вы бы хотели обрезать пробелы по краям строки?'
      + ' В случае обрезания позиции ошибок будут указаны без учета пробелов.')
answer = input()
if answer == 'Да' or answer == 'да':
    line = line.strip()
print('Игнорировать другие символы в последовательности?')
answer = input()
if answer == 'Да' or answer == 'да':
    ignore = True
else:
    ignore = False
circles = []
squares = []
result = True
for position in range(0, len(line)):
    character = line[position]
    if not ignore and character != '(' and character != ')' and character != '[' and character != ']':
        print('Обнаружен некорректный символ на позиции ' + str(position + 1) + '. Исправьте и попробуйте заново.')
        result = False
    elif character == '(':
        circles.append(position)
    elif character == '[':
        squares.append(position)
    elif character == ')':
        if len(circles) == 0:
            print('Обнаружена закрывающая круглая скобка на позиции ' + str(position + 1)
                  + ' без открывающей. Исправьте и попробуйте заново.')
            result = False
        elif len(squares) != 0 and circles[-1] < squares[-1]:
            print('Обнаружена закрывающая круглая скобка на позиции ' + str(position + 1)
                  + '. При этом внутри нее есть незакрытые квадратные. Исправьте и попробуйте заново.')
            result = False
            circles.pop()
        else:
            circles.pop()
    elif character == ']':
        if len(squares) == 0:
            print('Обнаружена закрывающая квадратная скобка на позиции ' + str(position + 1)
                  + ' без открывающей. Исправьте и попробуйте заново.')
            result = False
        elif len(circles) != 0 and squares[-1] < circles[-1]:
            print('Обнаружена закрывающая квадратная скобка на позиции ' + str(position + 1)
                  + '. При этом внутри нее есть незакрытые круглые. Исправьте и попробуйте заново.')
            result = False
            squares.pop()
        else:
            squares.pop()
if len(circles) > 0:
    print('Обнаружены незакрытые круглые скобки. Удалите или закройте их. Их позиции:')
    circles = [position + 1 for position in circles]
    print(*circles)
    result = False
if len(squares) > 0:
    print('Обнаружены незакрытые квадратные скобки. Удалите или закройте их. Их позиции:')
    squares = [position + 1 for position in squares]
    print(*squares)
    result = False
if result:
    print('Последовательность правильная')
else:
    print('Последовательность неправильная')
