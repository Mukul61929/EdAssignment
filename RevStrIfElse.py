my_string="Edyoda"

if len(my_string) != 0:
    Rev_string = my_string[::-1]
    print("The original string is : ", end="")
    print(my_string)

    print("The reversed string(using extended slice syntax) is : ", end="")
    print(Rev_string)
else:
    print(my_string)
    print("******String is empty******")
