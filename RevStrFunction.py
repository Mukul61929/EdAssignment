def RevStr(str1,str2):
    for i in str1:
        str2=i+str2
        print(f"The numer of elements reversed in the String is:", len(str2), "and the reversed string is: ",str2)
        
    print("---------------------------------------------------------------------------------------")
    print(f"the reversed string is","   ", str2)


my_str =("1234abcd")
rev_my_str=""
RevStr(my_str,rev_my_str)
