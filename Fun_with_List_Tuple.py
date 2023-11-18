my_list = [(2,5),(1,2),(4,4),(2,3),(2,1)]
print("------------------------------------------------------")
print(f"The given list {my_list}")

my_list.sort(key= lambda r:r[1])

print("------------------------------------------------------")
print(f"The sorted list is {my_list}")
