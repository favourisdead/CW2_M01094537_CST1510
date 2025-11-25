import sqlite3
import pandas as pd

def create_user_table():

    curr = conn.cursor()

    sql = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL
    )
    """

    curr.execute(sql)
    conn.commit()


def add_user(conn, name, hash_password):
    curr = conn.cursor()
    sql = """ INSERT OR REPLACE INTO users (username, password_hash) VALUES (?, ?) """
    param = (name, hash_password)
    
    curr.execute(sql, param)
    conn.commit()



def migrate_users():
    with open('DATA/users.txt','r') as f:
        users = f.readlines()

    for user in users:
        name, hash = user.strip().split(',')
        add_user(conn, name, hash)



def get_all_users():

    curr = conn.cursor()
    sql = "SELECT * FROM users"
    curr.execute(sql)
    users = curr.fetchall()
    conn.close()
    return users

def migrate_cyber_incidents():
    cyber = pd.read_csv('DATA/cyber_incidents.csv')
    print(cyber.head(5))
    conn = sqlite3.connect('DATA/telligenceE_platform.db')
    cyber.to_sql('cyber_incidents', conn, if_exists='append', index=False)
    print('all dadta migrated for cyber_incidents ')


def read_all_cyber_incidents_pandas():
    conn = sqlite3.connect('DATA/telligenceE_platform.db')
    querry = "SELECT * FROM cyber_incidents"
    cyber_table = pd.read_sql(querry, conn)
    print(cyber_table.head(5))

read_all_cyber_incidents_pandas()
