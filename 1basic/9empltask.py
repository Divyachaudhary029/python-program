a=int(input("Enter employees no.:"))
i=0
for i in range(a):
    price=int(input("enter salary:"))

    increment=price*15/100
    print(price,'+',increment,'=',price+increment)