import sqlite3

def change(database, choice, log, passwd, new):
    connct = sqlite3.connect(database)
    cursor = connct.cursor()
    cursor.execute('SELECT * FROM users') 
    try:
        if choice == 1:
            cursor.execute('UPDATE users SET login = {} WHERE login LIKE ?'.format(new), [log])
            connct.commit()
        else:
            cursor.execute('UPDATE users SET password = {} WHERE login LIKE ?'.format(new), [log])
            connct.commit()
        flag = 1
    except Exception:
        flag = 0
    
    cursor.close()
    connct.close()
    
    return flag