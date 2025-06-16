# 5. Write a program to find the maximum of the numbers in a list using the reduce 
# function. 
from functools import reduce
l=[1,5,11,8]
sum_num = lambda a,b:a+b 
greatest=lambda a,b: a if a > b else b
'''def greater(a, b):
    if a > b:
        return a
    return b
'''
 
print(f"Reduction of list is '{reduce(sum_num,l)}'")
print("--------------------------------------------------------")
print(f"Maximum of the numbers in a list is '{reduce(greatest,l)}'")