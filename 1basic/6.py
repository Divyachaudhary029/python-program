a=int(input("enter no. of products:"))
total=0
for i in range(a):
    price=int(input("enter price:"))
    total=total+price
    i=i+1

print(total)

gst=total*18/100
print("gst is:",gst)

total=total+gst
print("total is :",total)