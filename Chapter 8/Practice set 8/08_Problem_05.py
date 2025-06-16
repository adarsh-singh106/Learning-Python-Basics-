# 5. Write a python function to print first n lines of the following pattern: 
# *** 
# **               
# *
def star_bolte(n):
    i=n
    for i in range(n,0,-1):
        if(n!=0):
            print("*"*i,end="") # When you use the range() function
            #in a for loop, it automatically handles the increment or decrement for you.
            print("")

n=int(input("Enter a Number of N star:"))
star_bolte(n)

'''Here’s what each parameter does:

n → Starting value (number of stars in the first row)
0 → Ending value (exclusive, so it stops at 1)
-1 → Step value (to count down)'''