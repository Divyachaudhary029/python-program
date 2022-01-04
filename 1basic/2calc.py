a=int(input("enter number"))
b=int(input("enter number"))
c=int(input("enter 1 for add and 2 for subs:"))
if c==1:
    print(a+b)
elif c==2:
    print(a-b)
elif c==3:
    print(a*b)
elif c==4:
    print(a/b)
elif c==5:
    print(a%b)
elif c==6:
     print(a**b)
elif c==7:
     print(a//b)
else:
     print("enter valid input")