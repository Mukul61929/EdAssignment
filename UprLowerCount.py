def my_str_check(s):
    lower=0
    upper=0
    for i in s:
	    if i.isupper():
		        upper+=1
	    elif i.islower():
		        lower+=1
    print(f"The given string is {s}")     
    print("---------------------------------------------")
    print("The number of uppercase characters is:",upper)
    print("---------------------------------------------")
    print("The number of lowercase characters is:",lower)
    
    

my_str=("The quick Brow Fox")
my_str_check(my_str)
