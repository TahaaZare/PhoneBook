import time


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

    if mobile.isalpha():
        while mobile.isalpha():
            print(20 * '!')
            print('please just enter a valid number !!!')
            print(20 * '!')
            mobile = input('New Contact Phone Number : ')
            if mobile.isalnum() and len(mobile) < 11 or len(mobile) > 11:
                while len(mobile) < 11 or len(mobile) > 11:
                    print(20 * '!')
                    print('please just enter a valid number  !!!')
                    print(20 * '!')
                    mobile = input('New Contact Phone Number : ')
                    if mobile.isalnum() and len(mobile) == 11:
                        contacts[name] = mobile
                        print('Please Wait . . .')
                        time.sleep(2)
                        print('Success to add your contact :) ')
# endregion
