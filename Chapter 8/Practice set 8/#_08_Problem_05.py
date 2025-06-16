# 5. Write a python function to print first n lines of the following pattern: 
# *** 
# **               
# *
# Function to print the pattern
def print_pattern(n):
    for i in range(n, 0, -1):  # Loop from n down to 1
        print("*" * i)  # Print i stars

# Taking user input
num = int(input("Enter the number of lines: "))

# Checking for valid input
if num < 1:
    print("Error: Please enter a positive integer.")
else:
    print_pattern(num)