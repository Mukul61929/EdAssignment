#Program to add 25 to a given number passed in as an argument

num = input("Give a number in which 25 will be added:")
num = int(num)
result=((lambda number: number + 25)(num))
print(f"The resulting number with 25 added into the given number is: {result}")
