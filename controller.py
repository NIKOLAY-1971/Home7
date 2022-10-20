from secrets import choice
import model
import view

def button_click():
    pos = 1
    while pos:
        pos = view.menu()
        match pos:
            case 1: #генерация сведений по контактам
                n = view.number_contacts()
                result = model.generate_contact(n)
            case 2: #просмотр справочника
                view.output_directory(result)
            case 3: #экспорт справочника
                with open('telephone_directory.csv', 'w', encoding='utf-8') as file:
                    for value in model.lst_contact:
                        file.write(str(value))
                file.close()
            case 4: #импорт справочника и вывод на экран
                with open('telephone_directory.csv', 'r', encoding='utf-8') as lst_contact:
                    lst_contact = lst_contact.readlines()
                    view.output_directory(lst_contact)
                    