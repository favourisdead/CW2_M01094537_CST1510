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

import sqlite3
import pandas as pd


conn = sqlite3.connect('DATA/telligenceE_platform.db')
def add_user(conn, name, hash):
    curr = conn.cursor()
    sql = ( """ INSERT INTO users (username, password_hash) VALUES (?, ?) """)
    param = ('sam', 'hash_password_123')
    curr.execute(sql)   
    conn.commit()

def get_user():
    curr = conn.cursor()
    sql = """SELECT * FROM users"""
    curr.execute(sql)
    curr.fetchall()
    conn.close()
    print(users)
    return users

def migrate_user_data():
    with open('/Users/samuelzionbaheten-ikeng/Documents/GitHub/CW2_M01094537_CST1510/users.txt', 'r') as f:
        users = f.readlines()
    for user in users:
        name, hash = users.strip().split(',')
        add_user(conn,name,hash)
    conn.close()
        

cyber = pd.read_csv('DATA/datasets_metadata.csv')
print(cyber)