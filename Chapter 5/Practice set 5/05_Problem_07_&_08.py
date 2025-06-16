# 7. If the names of 2 friends are same; what will happen to the program in problem 
# 6?
#----------------------------------------------------------------------------
# name in this dictinory is acting as key .
# we know that key has to be uique , there cant be 2 same keys in one dict
# thus using the same again will update the value pair to newly assign element
# thiugh there could be same values to diffrent keys 
frind_dict={}
print("Friend 1")
f1=input("Enter your name:")
l1=input("Enter your favourite language:")
print("Friend 2")
f2=input("Enter your name:")
l2=input("Enter your favourite language:")
print("Friend 3")
f3=input("Enter your name:")
l3=input("Enter your favourite language:")
print("Friend 4")
f4=input("Enter your name:")
l4=input("Enter your favourite language:")
frind_dict.update({f1:l1,f2:l2,f3:l3,f4:l4}) 
print(frind_dict)