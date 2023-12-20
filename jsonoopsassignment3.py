class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"Dog Name: {self.name}") 
        print(f"Age: {self.age}")

    def get_info(self):
        print(f"Coat Color: {self.coat_color}")


class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color, agility_level):
        super().__init__(name, age, coat_color)
        self.agility_level = agility_level

    def special_jack_russell_method(self):
        print(f"{self.name} is a Jack Russell Terrier with agility level: {self.agility_level}.")


class Bulldog(Dog):
    def __init__(self, name, age, coat_color, strength_level):
        super().__init__(name, age, coat_color)
        self.strength_level = strength_level

    def special_bulldog_method(self):
        print(f"{self.name} is a Bulldog with strength level: {self.strength_level}.")


# Create Dog objects
a=str(input("Enter the 1st Dog Name: "))
b=int(input("Enter Dog Age: "))
c=str(input("Enter Coat Color: "))
dog1 = Dog(a,b,c)

d=str(input("Enter the 2nd Dog Name: "))
e=int(input("Enter Dog Age: "))
f=str(input("Enter Coat Color: "))
g=int(input("Enter the strenght of the Dog: "))
dog2 = JackRussellTerrier(d,e,f,g)
h=str(input("Enter the 3rd Dog Name: "))
i=int(input("Enter Dog Age: "))
j=str(input("Enter Coat Color: "))
k=int(input("Enter the strenght of the Dog: "))
dog3 = Bulldog(h,i,j,k)

# Perform operations
print("The 1st Dog name and Descriptions are: \n")
dog1.description()
dog1.get_info()
print()

print("The 2nd Dog name and Descriptions are: \n")
dog2.description()
dog2.get_info()
dog2.special_jack_russell_method()
print()

print("The 3rd Dog name and Descriptions are: \n")
dog3.description()
dog3.get_info()
dog3.special_bulldog_method()
print()
