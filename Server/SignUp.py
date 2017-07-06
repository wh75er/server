import sqlite3

def addUser(database, log, passwd):
    connct = sqlite3.connect(database)
    cursor = connct.cursor()
    try:
        cursor.execute("INSERT INTO users (login, password)\
                       VALUES ('%s', '%s')"%(log, passwd))
        connct.commit()
        flag = 1
    except Exception:
        flag = 0
    
    cursor.execute('SELECT * FROM users')
    cursor.close()
    connct.close()
    return str(flag)

#print(addUser('users_database.sqlite', 'Karina', '321'))