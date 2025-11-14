from login_ import register_user, login_user

def menu():
    print('\nChoose an option: ')
    print('1. Register')
    print('2. Login')
    print('3. Exit')

def main():
    while True:
        menu()
        choice = input('> ')

        if choice == '1':
            register_user()
        elif choice == '2':
            if login_user():
                print('login succesful')
            else:
                print('not succesful')
           
        elif choice == '3':
            print('preparig to exit...\n')
            print('good bye')
            break




main()
