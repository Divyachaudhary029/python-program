import sqlite3

def connection():
    a=sqlite3.connect('query.db')
    return a

def create_t(a):
    a.execute(''' CREATE TABLE STUDENTS(ID INT ,NAME TEXT,SUBJECT TEXT , MARKS INT)''')
    print("done")

def insert(a):
    f=int(input("enter no."))
    i=1
    while i<=f:
        p=int(input("enert ID:"))
        q=input("enter name")
        r=input("enter subject:")
        s=int(input("enter marks:"))
        a.execute("INSERT INTO STUDENTS(ID,NAME,SUBJECT,MARKS) VALUES(?,?,?,?)",(p,q,r,s))
        i=i+1
    print("inserted")


o=connection()
insert(o)
o.commit()
o.close()