import bcrypt
import os 

def hash_password(pwd):
    password_bytes = pwd.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed.decode('utf-8')


def validate_password(pwd, hashed):
    password_bytes = pwd.encode('utf-8')
    hashed_bytes = hashed.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_bytes)

def register_user():
    user_name = input('Enter a name: ').strip()
    password = input('Enter a password: ').strip()

def login_user():
    user_name = input('Enter your username: ').strip()
    password = input('Enter your password: ').strip()

