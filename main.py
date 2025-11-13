from apl import register_user, login_user



def menu():
    print('\nChoose an option: ')
    print('1. Register')
    print('2. Login')
    print('3. Exit')

def main():
    while True:
        menu()
        choice = input('Enter your choice 1-3: ').strip()
        if choice == '1':
            print('\n--------------user registration-----------------')
            user_name = input('enter a user name: ').strip()
            register_user()

        elif choice == '2':
            print('----------------user loging------------------------')
            user_name = input('Enter your username: ').strip()
            password = input('Enter your password: ').strip()
            print(login_user(user_name, password))

        elif choice == '3':
            
            print("\n\n\tExiting program...")
            print('program closed \n!!!!!')
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
