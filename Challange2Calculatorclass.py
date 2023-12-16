class Calculator:

    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        print("The input numbers are",num1, num2)

    def addition(self):
        print("Addition Operation Done:")
        print("Result is",abs(self.num1 + self.num2))
    def subtraction(self):
        print("Subtraction Operation Done:")
        print("Result is",abs(self.num1 - self.num2))
    def multiplication(self):
        print("Multiplication Operation Done:")
        print("Result is",abs(self.num1 * self.num2))
    def division(self):
        print("Division Operation Done:")
        print("Result is",abs(self.num2 / self.num1))

a=int(input("Enter the 1st number : "))
b=int(input("Enter the 2nd number : "))

myobj= Calculator(a,b)
print("Press 1 to do the Addition operation: ")
print("Press 2 to do the Subtraction operation: ")
print("Press 3 to do the Multiplication operation: ")
print("Press 4 to do the Division operation: ")
anyNumber= int(input('Enter your choice to perform following action between 1 to 4: '))
if anyNumber == 1:
    print(f"The addition of number: {a} and number: {b} are: {myobj.addition()}")
    
elif anyNumber == 2:
    print(f"The subtraction of number: {a} and number: {b} are: {myobj.subtraction()}")
    
elif anyNumber == 3:
    print(f"The multiplication of number: {a} and number: {b} are: {myobj.multiplication()}")
    
elif anyNumber == 4:
    print(f"The divison of number: {a} and number: {b} are: {myobj.division()}")
    
else:
    print("wrong Choice... Please try again")




