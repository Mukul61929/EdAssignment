class Point:

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        print("The input numbers are",x,y,z)

    def sqSum(self):
        n= (self.x**2+self.y**2+self.z**2)
        print("Sum of Squared numbers is",n)

a=int(input("Enter the 1st number to be squared: "))
b=int(input("Enter the 2nd number to be squared: "))
c=int(input("Enter the 3rd number to be squared:"))

Numbers_to_be_Squared=Point(a,b,c)
Numbers_to_be_Squared.sqSum()
