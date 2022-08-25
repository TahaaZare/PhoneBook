from functions.projcts_functions import *
import time

contacts = {}

# region Show Menu

show_menu()
while True:
    item = input('enter a item : ')
    if item == '1':
        add_contact(contacts)
    elif item == '2':
        # region check contact list

        if contacts == {}:
            print('have no contact please add a new contact .')
            add_contact(contacts)
            print(f'you add {list(contacts.keys())} {list(contacts.values())} As your contact')
        else:
            print(f'Your Contacts {list(contacts.keys())} {list(contacts.values())} ')

        # endregion
    elif item == '3':
        # print('search')
        name = input('please enter name for search : ')
        if name in contacts:
            print(f'{contacts.keys()} his/her number {contacts.values()}')
        else:
            print(f'sorry theres no contact with this {name} name')
    elif item == '4':
        print('update')
    elif item == '5':
        print('Delete')
    elif item == '0':
        response = input('you wanna exit ? y/n  ')
        if response.lower() == 'y':
            print('Exiting . . .')
            time.sleep(1)
            exit()
        elif response.lower() == 'n':
            print('ok')
            print(20 * '/')

    else:
        print(20 * '/')
        print('Invalid Item !!!!')
        print(20 * '/')
        show_menu()

# endregion
