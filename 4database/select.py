import sqlite3

def connection():
    connection=sqlite3.connect('prod.db')
    return connection

def select(connection):
    i=connection.execute('select prize from productss ')
    total=0
    for record in i:
        a=(record)
        total+=record[0]
    print(total)
o=connection()
select(o)
o.commit()
o.close()