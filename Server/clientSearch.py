import sqlite3
import pickle

def find(database, log):
    connct = sqlite3.connect(database)
    cursor = connct.cursor()
    cursor.execute('SELECT * FROM users') 
    row = cursor.fetchone()
    while row is not None:
        if row[0] == log:
            flag = 1
        row = cursor.fetchone()
    cursor.close()
    connct.close()
    try:
        return str(flag)
    except UnboundLocalError:
        return None