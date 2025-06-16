# 9. Write a program to print the following star pattern. 
# * * * 
# *   *   for n = 3 
# * * * 
n = int(input("Enter the value of n: "))

if n < 3:
    print("Error: Pattern not possible for n less than 3. Please enter a valid value.")
else:
    for i in range(n): # range(n) == range(0,n)
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()  # Move to the next line

