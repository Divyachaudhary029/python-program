a=[1,2,3,'a','b']
z=[]
y=[]
for i in a :
    if type(i)==int:
        z.append(i)
    elif type(i)==str:
        y.append(i)
print(z)
print(y)