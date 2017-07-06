import sqlite3

def authentication(database, log, passwd):
    connct = sqlite3.connect(database)
    cursor = connct.cursor()
    cursor.execute('SELECT * FROM users')
    row = cursor.fetchone()
    flag = str(0)
    while row is not None:
        if row[0] == log and row[1] == passwd:
            flag = str(1)
        row = cursor.fetchone()
    cursor.close()
    connct.close()
    return flag



    