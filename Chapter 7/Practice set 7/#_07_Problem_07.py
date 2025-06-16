# 7. Write a program to print the following star pattern. 
#   * 
#  *** 
# ***** for n = 3
'''The Given Star Pattern Follows The Formula 2N-1
'''
# Input from user
n = int(input("Enter the value of n to print star pattern: "))
print(f"Pyramid Star Pattern With n = {n}")
# Outer loop for rows
for i in range(1, n + 1):
    # Print spaces before stars
    print(" " * (n - i), end="")

    # Print stars: (2 * i - 1) stars in each row
    print("*" * (2 * i - 1))

