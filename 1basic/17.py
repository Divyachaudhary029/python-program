num=int(input("enter no.:"))
for i in range(2,num):
    if (num %i)==0:
        print(num,"is not prime no")
        break
    else:
        print(num,"is a prime no.")