import sqlite3

def connection():
    connection=sqlite3.connect('second.db')
    return connection

def fetch(connection):
    cur=connection.cursor()
    cur.execute('select * from report ')
    #raws=cur.fetchall()
    raws=cur.fetchone()
    for raw in raws:
        print(raw)
o=connection()
fetch(o)
o.commit()
o.close()