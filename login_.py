import bcrypt

def hash_password(password):
    binary_password = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(binary_password, salt)
    return hashed.decode('utf-8')


def validate_password(password, stored_hash):
    bin_password = password.encode('utf-8')
    bin_stored = stored_hash.encode('utf-8')

    return bcrypt.checkpw(bin_password, bin_stored)


def register_user():
    name = input('enter a name: ').strip()
    pswrd = input('enter a password: ').strip()
    hashed = hash_password(pswrd)

    with open('users.txt', 'a') as f:
        f.write(f'{name},{hashed}\n')

    print('user registered successfully')


def login_user():
    name = input('enter a name: ').strip()
    pswrd = input('enter a password: ').strip()

    with open('users.txt', 'r') as f:
        users = f.readlines()

    for user in users:
        stored_name, stored_hash = user.strip().split(',')

        if stored_name == name:
            return validate_password(pswrd, stored_hash)

    return False
