import sqlite3

def init(): 
    connection = sqlite3.connect('database.db')
    with open('schema.sql') as f:
        connection.executescript(f.read())
    connection.commit()
    connection.close()
    
def execute(sql, params = None, one = False):
    with sqlite3.connect('database.db') as connection:
        connection.row_factory = sqlite3.Row
        if params:
            result = connection.execute(sql, params)
        else:
            result = connection.execute(sql)
        if one:
            result = result.fetchone()
        else:
            result = result.fetchall()
        connection.commit()
    connection.close()
    return result

# returns id of inserted row
def insert(x):
    print(x)
    return 1