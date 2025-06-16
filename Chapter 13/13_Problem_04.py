# 4. Write a program to filter a list of numbers which are divisible by 5.

l=[1,5,10,8,20,106,5560,250,6]
divisbility= lambda x: x%5 == 0
print(f"The Numbers from The given List, which are divisble by 5 are\n{list(filter(divisbility,l))}")
filtered_list=filter(divisbility,l)
print("----------------------------------------------------------------------")
print(f"The Numbers from The given List, which are divisble by 5 are\n{list(filtered_list)}")


