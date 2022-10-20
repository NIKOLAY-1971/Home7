from random import randint
global result
lst_contact = []
def generate_contact(n):
    global lst_contact
    global result
    for i in range(n):
        num = str(i)
        surname = 'surname' + str(i)
        name = 'name' + str(i)
        birth = str(randint(1965, 2004))
        place_workinput = 'place_workinput' + str(i)
        phone_number = '+79' + str(randint(1000000, 9999999))
        lst_contact.append(num + ' ' + surname+' ' + name +
                            ' ' + birth+' ' + place_workinput+' ' + phone_number)
    return lst_contact

