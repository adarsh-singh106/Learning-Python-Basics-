# 2. Write a program to print third, fifth and seventh element from a list using enumerate 
# function. 
l=[1,2,"three",4,5,"six",False,True,56.22,"bhai"]
for n,items in enumerate(l) :
    if (n==2 or n==4 or n==6):
        print(n,items)

print("--------------------------------------------------------")
l=[1,2,"three",4,5,"six",False,True,56.22,"bhai"]
for n,items in enumerate(l) :
    if (n==2 or n==4 or n==6):
        print(n,items)