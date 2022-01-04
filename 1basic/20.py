num=int(input("enter no."))
if num==2 or num==3 or num==5 or num==7:
    print("prime")
elif num %2==0 or num%3==0 or num%5==0 or num%7==0:
    print(num,"not prime")
else:
    print(num,"prime")