nam=[]
t=[]
def stu():
    s=int(input("How many students:"))
    name(s)
def name(s):
    i=1
    while i<= s:
        name=input("Enter thre name:")
        nam.append(name)
        subject=int(input("Enter the sub Numbers:"))
        subname(subject)
        i+=1
        
def subname(subject):
    j=1
    total=0
    while j<=subject:
        subname=input("Enter subject name: ")
        marks=int(input("Enter the marks"))
        total=total+marks
        j+=1
    t.append(total)

def result():
    d=(nam,t)
    print(d)
    
stu()
result()