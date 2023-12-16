class Account:
    def __init__(self,title,balance) -> None:
        self.title=title
        self.balance=balance 
    def getbalance(self):
        return self.balance
    def deposit(self,amount):
        self.amount=amount
        self.balance = self.balance+self.amount
    def withdrawl(self,amount):
       self.amount=amount
       self.balance = self.balance-self.amount
 

class SavingAccount(Account):
    def __init__(self,title,balance,interestrate):
        super().__init__(title,balance)
        self.interestrate=interestrate
    def interstamount(self):
        self.interstamount=(self.interestrate * self.balance)/100
        return abs(self.interstamount)
        
a=str(input("Enter Accoun Holder Name: "))
b=int(input("Enter the Account Balance: "))
c=int(input("Enter the Interest Rate: "))
ash=SavingAccount(a,b,c)
print("Press 1 to see the account balance")
print("Press 2 to deposite any amount to the existing account balance")
print("Press 3 to withdraw any amount from the existing account balance")
print("Press 4 to see the interest amount on the account balance")
anyNumber= int(input('Enter your choice to perform following action between 1 to 4: '))

if anyNumber == 1:
    print(f"Current baalnce of the account is : {ash.balance}")
       
elif anyNumber == 2:
    ash.deposit(int(input("Enter the amount you want to deposite: ")))
    print("Deposite amount is :",ash.amount)
    print(f"Now after deposite of {ash.amount} Total Balance is :",ash.getbalance())
    
elif anyNumber == 3:
    print(f"Current baalnce of the account is : {ash.balance}")
    ash.withdrawl(int(input("Enter the amount you want to withdrawl: ")))
    print(f"Now after Withdrawl of {ash.amount} Total Balance is:",ash.getbalance())
    
elif anyNumber == 4:
    print(f"Total amount is {ash.balance},and interest rate is {ash.interestrate}%")
    print(f"Total interest amount is : {round(ash.interstamount())}")        
else:
    print("wrong Choice... Please try again")
    
    
