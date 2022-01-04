s=int(input("Hoe many students:"))
n=[]
t=[]
i=0
while i< s:
    name=input("Enter the name:")
    n.append(name)
    sub=int(input("Enter the sub Numbers:"))
    i+=1
    total=0
    j=0
    while j < sub:
        subname=input("Enter subject name: ")
        marks=int(input(f"Enter {subname} the marks"))
        j+=1
        total+=marks
    print("total:",total)
    t.append(total)
print("name",n)
print("total",t)

