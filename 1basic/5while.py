a=int(input("how many products:"))
i=1
total=0
while i<=a:
    price=int(input("Enter price:"))
    total=total+price
    i=i+1
print(total)
gst=total*18/100

print("gst is:",gst)

total=total+gst
print("total is :",total)