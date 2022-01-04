def num():
    a=[5,12,21,22,23,27,39,43,51,67,75,88,91]
    prime=[]
    Notprime=[]
    for i in a:
        if i==2 or i==3 or i==5 or  i==7:
            prime.append(i)
        elif i %2==0 or i %3==0 or i %5==0 or i %7==0:
            Notprime.append(i)   
        elif i %2!=0 or i %3!=0 or i %5!=0 or i %7!=0:
            prime.append(i)
    print("prime no.",prime)
    print("Notprime no.",Notprime)
num()

        
