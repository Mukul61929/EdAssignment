n=10
Num1 = 0
Num2 = 1

if(n == 2):
    print(f"The Fibonacci series for",n,"is:")
    print(Num1)
    print("-----------")
    print(Num2)
    print("-----------")
else:
    print(f"The Fibonacci series for",n,"is :")
    print(Num1)
    print("-----------")
    print(Num2)
    print("-----------")
    
    for index in range(n-2):
        next_num = Num1+Num2
        print(next_num)
        print("-----------")
        Num1 = Num2
        Num2 = next_num
