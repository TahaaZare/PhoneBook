# region menu

def show_menu():
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

    contacts[name] = mobile


# endregion


