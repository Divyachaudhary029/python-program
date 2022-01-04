class one():
    balance=1000
    def balance(self,a):
        self.a=a
        return self.a
    def deposit(self):
        self.a=int(input("enter amont:"))
        deposit= 1000+self.a
        return deposit
    def withdraw(self):
        self.a=int(input("enter amaount:"))
        withdraw=  1000-self.a 
        return withdraw
obj=one()
i=1
c=int(input("enter 1 for balance 2 for withdraw 3 for deposite:"))
if c==1:
    o=obj.balance(1000)
    print(o)
elif c==2:
    print(obj.withdraw())
elif c==3:
    print(obj.deposit())
i+=1
