import sqlite3

def connection():
    connection=sqlite3.connect('prod.db')
    return connection

def delete(connection):
    connection.execute('DELETE  from productss where prize=600')
    connection.commit
    print("total no of rows deleted:", connection.total_changes)
    i=connection.execute('select * FROM PRODUCTSS')
    for record in i:
        print(record)

o=connection()
delete(o)
o.commit()
o.close()