# 1. Write a program using functions to find greatest of three numbers. 
def greatest_function(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        print(f"{n1} is Greatest")
    elif n2 >= n1 and n2 >= n3:
        print(f"{n2} is Greatest")
    else:
        print(f"{n3} is Greatest")

# Function Call
n1=int(input("Enter First Number:"))
n2=int(input("Enter second Number:"))
n3=int(input("Enter third Number:"))
greatest_function(n1,n2,n3)


"""

# Function to find the greatest number
def find_greatest(a, b, c):
    return max(a, b, c)  # Using max() function to get the highest value

# Taking user input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

# Calling the function and displaying the result
print("The greatest number is:", find_greatest(num1, num2, num3))

"""
