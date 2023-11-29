len_of_list = int(input("Enter the length of the list: ")) # type the lenght of the list ex: 7
input_list= []  # type the inputs ex=[1,2,3,4,5,6,7]

for i in range(len_of_list):
    current_element = int(input(f"Enter the number at index {i+1}:"))
    input_list.append(current_element)
print("The given input list is: ", input_list)

result = list(map(lambda r:r*2, input_list))   #Resulting output = [2,4,6,8,10,12,14]
print("Resulting output with three times of the input number is: ",result )
