def stu():
    n=int(input("How many students:"))
    name(n)
    return n
def name(n):
    i=1
    aa=[]
    while i<=n:
        name=input(("enter name:"))
        aa.append(name)
        i=i+1
    return aa
o=name(2)
print(o)