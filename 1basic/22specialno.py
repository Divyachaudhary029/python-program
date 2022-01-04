n=int(input("enter no.:"))
if(n < 10 or n > 99):
    print("invalid input","should have 2 digits only")
else:
        first=n//10
        last =n%10
        sum = first +last
        pro= first*last
if ((sum+pro)== n):
        print(n,"is a ","special two digit number")
else:
        print(n,"is not a ","special two digit number")