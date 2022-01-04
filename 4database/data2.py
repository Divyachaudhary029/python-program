import sqlite3

def connection():
    a=sqlite3.connect('new3.db')
    return a

def create_t(a):
    a.execute(''' CREATE TABLE STUDENT(NAME TEXT, AGE INT)''')
    print("done")

def insert(a):
    f=int(input("enter no."))
    i=1
    while i<=f:
        z=input("enert name:")
        q=int(input("enter age"))
        a.execute("INSERT INTO STUDENT(NAME,AGE) VALUES(?,?)",(z,q))
        i=i+1
    print("inserted")

o=connection()
insert(o)
o.commit()
o.close()