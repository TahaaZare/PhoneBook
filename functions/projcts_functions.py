import time


# region Fake Data

def fake_data(contacts):
    contacts['ali'] = '093333333333'
    contacts['taha'] = '98317868767'
    contacts['HA'] = '12312312312'


# endregion

# region menu

def show_menu(item=None):
    if item == '5':
        print('5-Delete')

    print('Welcome !')
    print(24 * '*')
    print('1-Add')
    print('2-ShowAll')
    print('3-Search')
    print('4-Update')
    print('5-Delete')
    print('0-Exit')
    print(24 * '*')


# endregion

# region Add Contact

def add_contact(contacts):
    name = input('New Contact Name : ')
    mobile = input('New Contact Phone Number : ')

    if mobile.isalnum() and len(mobile) < 11 or len(mobile) > 11:
        while mobile.isalnum() and len(mobile) < 11 or len(mobile) > 11:
            print(20 * '!')
            print('please just enter a valid number  !!!')
            print(20 * '!')
            mobile = input('New Contact Phone Number : ')
            if mobile.isalnum() and len(mobile) >= 11:
                contacts[name] = mobile
                print('Please Wait . . .')
                time.sleep(2)
                print('Success to add your contact :) ')
    elif mobile.isalpha():
        while mobile.isalpha():
            print(20 * '!')
            print('please just enter a valid number !!!')
            print(20 * '!')
            mobile = input('New Contact Phone Number : ')
            if mobile.isalnum() and len(mobile) < 11 or len(mobile) > 11:
                while mobile.isalnum() and len(mobile) < 11 or len(mobile) > 11:
                    print(20 * '!')
                    print('please just enter a valid number  !!!')
                    print(20 * '!')
                    mobile = input('New Contact Phone Number : ')
                    if mobile.isalnum() and len(mobile) >= 11:
                        contacts[name] = mobile
                        print('Please Wait . . .')
                        time.sleep(2)
                        print('Success to add your contact :) ')


# endregion

# region Search

def search_name(contacts, name):
    if name.lower() in contacts.keys() or name.upper() in contacts.keys():
        print(f'"{name.lower()}"  his/her number is "{contacts.get(name)}"')
    else:
        time.sleep(1)
        print(f'sorry theres no contact with this "{name}" name')


# endregion

# region Update

def update_contact_name(contacts, name):
    if name in contacts:
        phoneNumber = contacts.get(name)
        del contacts[name]
        change_name = input('Please Enter a new name for your contact : ')
        contacts[change_name] = phoneNumber
        print(f'Success to change Contact name !')
    else:
        time.sleep(1)
        print(18 * '/')
        print(f'sorry theres no contact with this "{name}" name')


def update_contact_number(contacts, contact_name_number):
    if contact_name_number in contacts:
        change_number = input('Please Enter a new number for your contact : ')
        contacts[contact_name_number] = change_number
        print(f'Success to change phone number !')


# endregion

# region Delete

def delete(contacts, delete_contact_name):
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

# endregion
