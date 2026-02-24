class Bank:
    name="KBC"
    loc="Haldia"
    ifcs=1437
    time="9-5"
    def __init__(self,branch,cash,emp):
        self.branch=branch
        self.cash=cash
        self.emp=emp
    def get_detail(self):
        print(f'{self.name}  {self.branch}  {self.cash}')
    def withdraw(self,amt):

        if self.cash>=amt and amt>0 and amt<1000:
            self.cash-=amt
            print(f'{amt} withdrawn successfully')
        else:
            print("Insufficient balance")
    def deposit(self,amt):
        self.cash+=amt
        print(f'{amt} deposited successfully')
    @classmethod
    def change_name(cls,new_name):
        cls.name=new_name

c1=Bank("Khudiram",100,4)
c2=Bank("gandhinagar",101,5)
c3=Bank("Township",10,6)    
c2.get_detail()
c2.withdraw(10)
c2.get_detail()
c2.deposit(100)
c2.get_detail()
c2.change_name("SBI")
print(c2.name)
print(Bank.name)

# b1=Bank()
# b2=Bank()
# b3=Bank()
# b1.branch="Khudiram"
# b1.cash=100
# b1.emp=4
# b2.branch="gandhinagar"
# b2.cash=101
# b2.emp=5
# b3.branch="Township"
# b3.cash=10
# b3.emp=6
# Bank.get_detail(b2)

