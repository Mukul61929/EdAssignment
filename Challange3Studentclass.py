class Student:
    def __init__(self, Student_Name,Roll_no) -> None:
        self.__name = Student_Name
        self.__rollNumber = Roll_no
    
    def setName(self,Sname): #Setter
        self.__name = Sname
    def getName(self): #Getter
        return self.__name
    def setRollNumber(self,rnum):
        self.__rollNumber = rnum 
    def getRollNumber(self):
        return self.__rollNumber
    
    def StudentNameEntry(self,Sname,rnum):
        self.setName(Sname)
        self.setRollNumber(rnum)
    
a=str(input("Enter the student name: "))
b=str(input("Enter the students Roll_No: "))

Myname=Student(a,b)
print("Press 1 to do the see the students name: ")
print("Press 2 to do the see the Roll No of the student: ")

anyNumber= int(input('Enter your choice to perform following action between 1 to 2: '))
if anyNumber == 1:
    print(f"Name of the Student is: {Myname.getName()}")
    
elif anyNumber == 2:
    print(f"Roll No of the Student is: {Myname.getRollNumber()}")
 
