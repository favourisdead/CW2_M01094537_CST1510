import bcrypt

password = 'Password123'

def hash_password(password):
    binary_password = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash_password = bcrypt.hashpw(binary_password,salt)
    return hash_password.decode('utf-8')


def validate_password(password):
    hash_password = hash.encode('utf-8')
    bin_password = password.encode('utf-8')

    return(bcrypt.checkpw(bin_password, hash_password))

def register_user():
    name = input('enter a name: ').strip()
    pswrd = input('enter a password: ').strip()
    hash = hash_password(pswrd)
    with open('users.txt', 'a') as f:
        f.write((f'{name},{hash}\n'))
    print('user registered succesfully')


def login_user():
    name = input('enter a name').strip()
    pswrd = input('enter a password').strip()
    with open('users.txt','r') as f:
        user = f.readlines()
    
    for user in user:
        name_, hash = user.strip().split(',')

        if name_ == name:
            return validate_hash(password, hash)
    return False

