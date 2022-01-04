a=open('data.txt','r')
l=a.readlines()
s=str(l)
x=input("enter :")
b=s.replace(x,'')
print(b)
a.close()

