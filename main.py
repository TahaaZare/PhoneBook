from functions.projcts_functions import *
import time

contacts = {}
fake_data(contacts)
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
        # BUGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG :/
        if contacts == {}:
            print('have no contact please add a new contact .')
            add_contact(contacts)
            print(f'you add {list(contacts.items())} As your contact')
        else:
            print(f'Your Contacts {list(contacts.keys())} {list(contacts.values())} ')

        # endregion
    elif item == '3':
        # region Search Contact
        name = input('please enter name for search : ')
        search_name(contacts, name)
        # result = search_name(contacts, name)
        # if not result:
        #     print('no contact')
        # endregion
    elif item == '4':
        # region Update Contact
        update_item = input('1-Update Name 2-Update Number ? ')
        if update_item == '1':
            # region Change Contact Name
            contact_name = input('Please enter a contact name for update : ')
            update_contact_name(contacts, contact_name)

            print(28 * '/')
            # endregion
        elif update_item == '2':
            # region Change Phone Number
            contact_name_number = input('Please enter a contact name for update : ')
            update_contact_number(contacts, contact_name_number)
            print(28 * '/')

            # endregion
        else:
            print('Invalid Input !')
            update_item = input('1-Update Name 2-Update Number ? ')
            if update_item != '1' or update_item != '2':
                print('Invalid Input !')
                update_item = input('1-Update Name 2-Update Number ? ')
                if update_item == '1':
                    # region Change Contact Name
                    contact_name = input('Please enter a contact name for update : ')
                    update_contact_name(contacts, contact_name)
                    print(28 * '/')
                    # endregion
                elif update_item == '2':
                    # region Change Phone Number
                    contact_name_number = input('Please enter a contact name for update : ')
                    update_contact_number(contacts, contact_name_number)
                    print(28 * '/')

                    # endregion
        # endregion
    elif item == '5':
        # region Delete Contact
        delete_contact_name = input('Please Enter a contact name for delete : ')
        delete(contacts, delete_contact_name)
        # endregion
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
    elif item.lower() == 'exit' or item.upper() == 'EXIT':
        exit()
    else:
        print(20 * '/')
        print('Invalid Item !!!!')
        print(20 * '/')
        show_menu()

# endregion
