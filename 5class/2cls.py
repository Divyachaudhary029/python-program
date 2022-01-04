class one():
    def balance(self,a):
        self.a=a
        return self.a
    def deposit(self):
        self.a+=200
        return self.a
    def withdraw(self):
        self.a-=100
        return self.a
obj=one()
print(obj.balance(700))
print(obj.withdraw())
print(obj.deposit())
