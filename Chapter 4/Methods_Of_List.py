'''
l1 = [1,8,7,2,21,15] 

• l1.sort(): updates the list to [1,2,7,8,15,21] 
• l1.reverse(): updates the list to [15,21,2,7,8,1] 
• l1.append(8): adds 8 at the END of the list  
• l1.insert(3,8): This will add 8 at 3 index  
• l1.pop(2): Will delete element at index 2 and return its value. 
• l1.remove(21): Will remove 21 from the list.  
'''
#--------------------------NOTE-------------------------------
# 1. Sort Can only be used with int & float
# 2. List_variable_name.insert(index,element)  >>> insert and
#  the element at that idex move 1 index to right 
# 3. List_variable_name.pop(index)          >>> pop
#-------------------------------------------------------------

Num_list=[1,211,56,-2,0,78,9899,-556,12.3]
print(f"Original list is {Num_list}")
Num_list.sort()
print(f"After Using Sort {Num_list}")
Num_list.reverse()
print(f"After using reverse {Num_list}")
Num_list.append(69)
print(f"After using append {Num_list}")
Num_list.insert(2,112)
print(f"After using insert {Num_list}")
Num_list.pop(1)
print(f"After Using pop {Num_list}")
Num_list.remove(9899)
print(f"After using remove(9899) {Num_list}")