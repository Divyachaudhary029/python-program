def fact(n):
    f=1
    i=1
    while(i<=n):
        f=f*i
        i+=1
    return f
n=int(input("enter number:"))
o=fact(n)
print(o)

