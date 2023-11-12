new_string = "Edyoda"
rev_string =""
print(f"Given original string is","********", new_string, "********")
print("-------------------------")
for index in new_string:
    rev_string = index + rev_string
    print(f"The numer of elements reversed in the String is:", len(rev_string), "and the reversed string is: ", rev_string)
print(f"the reversed string is","   ", rev_string)
    
