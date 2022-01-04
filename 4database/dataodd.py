import sqlite3

def connection():
    a=sqlite3.connect('new4.db')
    return a

def create_t(a):
    a.execute(''' CREATE TABLE ODDEEVEN(NO INT)''')
    print("done")

def insert(a):
    num=int(input("enter a no."))
    q=int(input("enter 2 no."))
    x=num%2
    if x>0:
        e="odd"
    else:
        e="even"
    return e
    a.execute("INSERT INTO ODDEEVEN(NO) VALUES(? ,?)",(num,q))
    print("inserted")

o=connection()
insert(o)
o.commit()
o.close()