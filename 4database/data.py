import sqlite3

def connection():
    a=sqlite3.connect('new.db')
    return a

def create_t(a):
    a.execute(''' CREATE TABLE STUDENT(NAME TEXT, AGE INT)''')
    print("done")

def insert(a):
    a.execute("INSERT INTO STUDENT(NAME,AGE) VALUES('diya',20)")
    print("inserted")

o=connection()
insert(o)
o.commit()
o.close()