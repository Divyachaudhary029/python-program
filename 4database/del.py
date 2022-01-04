import sqlite3
from sqlite3.dbapi2 import connect

def connection():
    connection=sqlite3.connect('proddb.py')
    return connection

def delete(connection):
    connection.execute('DELETE from products where prize=600')
    connection.comit
    print("total no. of deleted:",connection.total_changes)
    i=connection.execute('select * FROM PRODUCTS')
    for record in i:
        print(record)
o=connection()
delete(o)
o.commit()
o.close()