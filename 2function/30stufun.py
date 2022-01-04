nam=[]
t=[]
def stuno():
    num=int(input("enter no of student:"))
    stuname(num)

def stuname(a):
    i=1
    while(i<=a):
        nam.append(input("enter name of student :"))
        sub=int(input("enter no of subjects : "))
        subjects(sub)
        i=i+1

def subjects(b):
    j=1
    total=0
    while(j<=b):
        subname=input("enter name  of subject :")
        marks=int(input("entr marks :"))
        total=total+marks
        j=j+1
    t.append(total)

def result():
    d=(nam,t)
    print(d)

stuno()
result()