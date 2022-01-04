n=int(input("enter number:"))
f=1
i=0
for i in range(n):
    f=f*n
    print("fact is",f)
    n=n-1
    print("num is",n)
    i=i+1
print("factorial of",n,"is",f)