n = 10

Num1 = 0
Num2 = 1

if(n == 2):
    print(f"The Fibonacci series for",n,"is:")
    print(f"The",Num1+1,"number of the fibonacci series is",Num1)
    print("--------------------------------------------------")
    print(f"The",Num2+1,"number of the fibonacci series is",Num2)
    print("--------------------------------------------------")
else:
    print(f"The Fibonacci series for",n,"is :")
    print(f"The",Num1+1,"number of the fibonacci series is",Num1)
    print("--------------------------------------------------")
    print(f"The",Num2+1,"number of the fibonacci series is",Num2)
    print("--------------------------------------------------")
    i = 1

    while (i<=n-2):
        next_num = Num1+Num2
        i= i+1
        print(f"The",i+1,"number of the fibonacci series is",next_num)
        print("--------------------------------------------------")
        Num1 = Num2
        Num2 = next_num
