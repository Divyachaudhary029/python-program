def prime_notprime():
    num=int(input("entor no."))
    if num==2 or num==3 or num==5 or num ==7:
        e="prime"
    elif num %2==0 or num %3==0 or num%5==0 or num%7==0:
        e="notprime"
    else:
        e="prime"
    return e
a=prime_notprime()
print(a)
    
    