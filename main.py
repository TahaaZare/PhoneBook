from functions.projcts_functions import *
import time

contacts = {}

# region Show Menu

show_menu()
while True:
    time.sleep(1)
    print(20 * '*')
    item = input('Choose an item : ')
    print(20 * '*')
    if item == '1':
        add_contact(contacts)
    elif item == '2':
        # region check contact list

        if contacts == {}:
            print('have no contact please add a new contact .')
            add_contact(contacts)
            print(f'you add {contacts.items()} As your contact')
        else:
            print(f'Your Contacts {list(contacts.keys())} {list(contacts.values())} ')

        # endregion
    elif item == '3':
        # region Search Contact
        name = input('please enter name for search : ')
        if name.lower() in contacts.keys() or name.upper() in contacts.keys():
            print(f'{name.lower()}  his/her number is ?')
        else:
            time.sleep(1)
            print(f'sorry theres no contact with this "{name}" name')
        # endregion
    elif item == '4':
        # region Update Contact
        update_item = input('1-Update Name 2-Update Number ? ')
        if update_item == '1':
            contact_name = input('Please enter a contact name for update : ')
            if contact_name in contacts:
                print(contact_name)
            else:
                time.sleep(1)
                print(18 * '/')
                print(f'sorry theres no contact with this "{contact_name}" name')
            print(28 * '/')
        elif update_item == '2':
            print('update number')
            print(28 * '/')
        else:
            print('Invalid Input !')
            # update_item = input('1-Update Name 2-Update Number ? ')
        # endregion
    elif item == '5':
        print('Delete')
    elif item == '0':
        # region Exit
        response = input('you wanna exit ? y/n  ')
        if response.lower() == 'y':
            print('Exiting . . .')
            time.sleep(1)
            exit()
        elif response.lower() == 'n':
            print('ok')
            print(20 * '/')

        # endregion
    elif item.lower() == 'help' or item.upper() == 'HELP':
        show_menu()
    else:
        print(20 * '/')
        print('Invalid Item !!!!')
        print(20 * '/')
        show_menu()

# endregion
