def my_str_check(s):
    d={"UPPER_CASE":0,"LOWER_CASE":0} 
    for each_char in s:
        if each_char.isupper():
           d["UPPER_CASE"]+=1
        elif each_char.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print("Original String : ", s)
    print("-----------------------------------------------")
    print("No. of Upper case characters : ",d["UPPER_CASE"])
    print("-----------------------------------------------")
    print("No. of Lower case Characters : ",d["LOWER_CASE"])

my_str=("The quick Brow Fox")
my_str_check(my_str)
