import json

addresses = {'Jan Kowalski': ('884123321', 'jankowalski@wp.pl'),
             'Halina Nowak': ('600500900', 'H.Nowak@onet.pl'),
             'John Doe': ('225572091', 'doe@yahoo.com')}


def display_contact():
    print("Imię \t\tNumer kontaktowy \t\tAdres Email")
    for key in addresses:
        print('{}\t\t{}'.format(key, addresses.get(key)))


while True:
    choice = int(input(
        " 1. Nowy kontakt \n 2. Edytuj kontakt \n 3. Usuń kontakt \n 4. Wyswietl wszystkie kontakty \n 5. Wyjście \n"))
    if choice == 1:
        name = input('Podaj imię i nazwisko: ')
        phone = int(input('Podaj numer telefonu: '))
        mail = input('Podaj adres e-mail: ')
        addresses[name] = phone, mail
    elif choice == 2:
        edit_contact = input("Podaj który kontakt chcesz edytować: ")
        if edit_contact in addresses:
            phone = int(input('Podaj nowy numer telefonu: '))
            mail = input('Podaj nowy adres e-mail: ')
            addresses[edit_contact] = phone, mail
            print('Kontakt zaaktualizowany!')
            display_contact()
    elif choice == 3:
        delete_contact = input('Podaj który kontakt usunąć: ')
        if delete_contact in addresses:
            confirm = input('Czy na pewno chcesz usunąć kontakt t/n?')
            if confirm == 'T' or confirm == 't':
                addresses.pop(delete_contact)
            display_contact()
        else:
            print('Imię nie znalezione w książce adresów')

    elif choice == 4:
        display_contact()
        break
    else:
        break
