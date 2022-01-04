p=[]
q=[]
for i in range(1,20):
    if i==2 or i==3 or i==5 or  i==7:
        p.append(i)
    elif i %2==0 or i %3==0 or i %5==0 or i %7==0:
        q.append(i)   
    elif i %2!=0 or i %3!=0 or i %5!=0 or i %7!=0:
        q.append(i)
print("prime no.",p)
print("Notprime no.",q)
