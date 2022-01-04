import random
a='1234567890'
b='!@#$%^&*()_+'
c='qwertyuioplkjhgfdaszxcvbnm'
k=''
length=int(input("Enter length:"))
aa=random.sample(a,3)
bb=random.sample(b,3)
cc=random.sample(c,2)
all = aa+bb+cc
temp=random.sample(all, length)
password =' '.join(temp)
print(password)

