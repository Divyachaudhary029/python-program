nam=[]
t=[]
def empno():
    num=int(input("enter no of employees:"))
    empname(num)

def empname(a):
    i=1
    while(i<=a):
        nam.append(input("enter name of employee :"))
        month=int(input("enter no of months : "))
        salary(month)
        i=i+1

def salary(b):
    j=1
    total=0
    while(j<=b):
        salary=int(input("entr salary :"))
        increment=salary*15/100
        total=total+salary
        o=(total,'+',increment,'=',total+increment)
        j=j+1
    t.append(o)

def result():
    d=(nam,t)
    print(d)

empno()
result()
