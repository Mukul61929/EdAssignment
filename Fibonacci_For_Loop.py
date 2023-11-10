n = 10

Num1 = 0
Num2 = 1

if(n == 2):
    print(f"The Fibonacci series for",n,"is:")
    print(Num1)
    print(Num2)
else:
    print(f"The Fibonacci series for",n,"is :")
    print(Num1)
    print(Num2)

    for i in range(n-2):
        next_num = Num1+Num2
        print(next_num)
        Num1 = Num2
        Num2 = next_num
