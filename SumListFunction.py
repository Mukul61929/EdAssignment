def SumList(l,s):
    for i in l:
        s= s+i
        print(f"The {i} element are added in the Sum of the list is {s}")
    print("-----------------------------------------------")
    print(f"The final Sum of the List is {s}")

my_list = (8,2,3,0,7)
Sum=0

SumList(my_list,Sum)
