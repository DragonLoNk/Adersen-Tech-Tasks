print('Введите имя и выберите опции алгоритма. Для активации опции отвечайте "да"')
name = input()
print('Вы бы хотели обрезать пробелы по краям строки?')
answer = input()
if answer == 'Да' or answer == 'да':
    name = name.strip()
print('Вы бы хотели, чтобы алгоритм игнорировал кейс ввода?')
answer = input()
requiredName = 'Вячеслав'
if answer == 'Да' or answer == 'да':
    if name.lower() == requiredName.lower():
        print('Привет, Вячеслав')
    else:
        print('Нет такого имени')
else:
    if name == requiredName:
        print('Привет, Вячеслав')
    else:
        print('Нет такого имени')
