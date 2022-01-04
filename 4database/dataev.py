import sqlite3

def connection():
    a=sqlite3.connect('new.db')
    return a

def create_t(a):
    a.execute(''' CREATE TABLE ODDEVEN(NUM INT, ODD INT, EVEN INT)''')
    print("done")

def insert(a):
    i=1
    n=int(input("Input any integer:"))
    while i<=n:
        if i%2==0:
            e="yes"
        else:
            e="no"
        a=sqlite3.connect('new.db')
        a.execute('''INSERT INTO ODDEVEN(NUM ,ODD,EVEN) VALUES(?,?,?)''',(n,e,e))
        i=i+1
    print("inserted")

o=connection()
insert(o)
o.commit()
o.close()