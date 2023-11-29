len_of_list = int(input("Enter the length of the list: ")) # type the lenght of the list ex: 4
input_list= []  # type the inputs ex=[4,5,2,9]

for i in range(len_of_list):
    current_element = int(input(f"Enter the number at index {i+1}:"))
    input_list.append(current_element)
print("The given input list is: ", input_list)

result = list(map(lambda r:r*r, input_list))   #Resulting output = [16,25,4,81]
print("Resulting output with square of the input number is: ",result )
