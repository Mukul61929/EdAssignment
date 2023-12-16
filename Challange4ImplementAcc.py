class Account:
    def __init__(self,title,balance) -> None:
        self.title=title
        self.balance=balance 

class SavingAccount(Account):
    def __init__(self,title,balance,interestrate):
        super().__init__(title,balance)

        self.interestrate=interestrate

a=str(input("Enter Accoun Holder Name: "))
b=int(input("Enter the Account Balance: "))
c=int(input("Enter the Interest Rate: "))
ashish=SavingAccount(a,b,c)
print("Account Holder name is:",ashish.title)
print("Account Balance is:",ashish.balance)
print(f"Interest rate is: {ashish.interestrate} %")
