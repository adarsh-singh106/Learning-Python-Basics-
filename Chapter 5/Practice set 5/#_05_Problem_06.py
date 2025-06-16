# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique. 
frind_dict={}
#take there name and value as input to update the <dict>


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