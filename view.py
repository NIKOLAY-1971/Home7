
def menu():
    return int(input('''
        Выберите действие:
        1 - Сгенерировать данные справочника;
        2 - Вывести справочник на экран;
        3 - Экспортировать справочник в файл;
        4 - Импортировать справочник из файла;
        0 - Выход из справоника.
        введите номер:  '''))
    

def number_contacts():
    return int(input('Введите количество контактов записей справочника:'))

def output_directory(lst_contact):
    print('id', 'фамилия', 'имя', 'год рождения', 'место работы', 'номер телефона')
    for value in lst_contact:
        print(value)