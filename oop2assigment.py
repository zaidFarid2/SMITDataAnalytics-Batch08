class Bank():
    authentication = False
    def __init__(self,name,pin):
        self.name = name.lower()
        self.pin = pin
        self.balance = 0

    def withdraw(self):
        self.amount = int(input("Ente a amount to deposite"))
        if(self.pin == "12345" and self.name == "zaid"):
            if(self.balance>0 and self.amount<self.balance):
                self.balance -= self.amount
                print(f"you currnt balance is {self.balance}")
            else:
                print(f"There is any issue in your balance or withdrawl funds ")

    def deposite(self):
        self.amount = int(input("Ente a amount to deposite"))
        self.balance += self.amount
        print(f"you current balance is {self.balance}")

    def display(self):
        return(f"{self.name} your current fund balance is {self.balance}")

        
        
p1 = Bank("Zaid",12345)
p1.withdraw()
print(Bank.display(p1))
