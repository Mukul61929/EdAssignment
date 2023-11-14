numbers = (1,2,3,4,5,6,7,8,9)
 
even = 0
odd = 0
 
# iterating each number in list
for num in numbers:
 
    # checking condition
    if num % 2 == 0:
        even += 1
 
    else:
        odd += 1
 
print("The series of given numbers is: ", numbers)
print("------------------------------------------------")
print("Total even numbers in the given numbers: ", even)
print("------------------------------------------------")
print("Total odd numbers in the given numbers: ", odd)
