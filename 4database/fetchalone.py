import sqlite3

def connection():
    connection=sqlite3.connect('prod.db')
    return connection

def fetch(connection):
    cur=connection.cursor()
    cur.execute('select * from productss ')
    #raws=cur.fetchone()
    raws=cur.fetchmany(3)
    for raw in raws:
        print(raw)
o=connection()
fetch(o)
o.commit()
o.close()