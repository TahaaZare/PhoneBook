from functions.projcts_functions import *
import time

contacts = {'taha': '09333130432'}

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
            # region Change Contact Name

            contact_name = input('Please enter a contact name for update : ')
            if contact_name in contacts:
                phoneNumber = contacts.get(contact_name)
                del contacts[contact_name]
                change_name = input('Please Enter a new name for your contact : ')
                contacts[change_name] = phoneNumber
                print(f'Success to change Contact name !')
            else:
                time.sleep(1)
                print(18 * '/')
                print(f'sorry theres no contact with this "{contact_name}" name')
            print(28 * '/')

            # endregion
        elif update_item == '2':
            # region Change Phone Number
            contact_name_number = input('Please enter a contact name for update : ')
            if contact_name_number in contacts:
                change_number = input('Please Enter a new number for your contact : ')
                contacts[contact_name_number] = change_number
                print(f'Success to change phone number !')
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
                    if contact_name in contacts:
                        change_name = input('Please Enter a new name for your contact : ')
                        contacts[contact_name] = change_name
                        print(f'Success to change Contact name !')
                    else:
                        time.sleep(1)
                        print(18 * '/')
                        print(f'sorry theres no contact with this "{contact_name}" name')
                    print(28 * '/')

                    # endregion
                elif update_item == '2':
                    # region Change Phone Number
                    contact_name_number = input('Please enter a contact name for update : ')
                    if contact_name_number in contacts:
                        change_number = input('Please Enter a new number for your contact : ')
                        contacts[contact_name_number] = change_number
                        print(f'Success to change phone number !')
                    print(28 * '/')

                    # endregion
        # endregion
    elif item == '5':
        # region Delete Contact
        delete_contact_name = input('Please Enter a contact name for delete : ')
        if delete_contact_name in contacts:
            delete_contact = input(f'Are u Sure to delete this {delete_contact_name} contact y/n ?')
            if delete_contact.lower() == 'y' or delete_contact.upper() == 'Y':
                del contacts[delete_contact_name]
                print(f'deleting {delete_contact_name} Contact ! Please Wait . . .')
                time.sleep(2)
                print('The deletion was successful !')
            elif delete_contact.lower() == 'n' or delete_contact.upper() == 'N':
                print('Ok i Keep this contact for Y !')
                time.sleep(1)
                show_menu()
            else:
                print('Invalid Input !')
                print('Please tyr Later !')
                time.sleep(2)
                show_menu()
        else:
            print(f'Theres no contact with this {delete_contact_name} name !')
            # if delete_contact_name
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
    else:
        print(20 * '/')
        print('Invalid Item !!!!')
        print(20 * '/')
        show_menu()

# endregion
