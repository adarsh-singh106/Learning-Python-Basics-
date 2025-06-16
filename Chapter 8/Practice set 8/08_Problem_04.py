# 4. Write a recursive function to calculate the sum of first n natural numbers.

    # Recursive function to calculate sum of first n natural numbers
def sum_natural(n):
    if n == 1:  # Base case
        return 1
    else:
        return n + sum_natural(n - 1)  # Recursive call

# Taking user input
num = int(input("Enter a positive integer: "))

# Checking for valid input
if num < 1:
    print("Error: Please enter a positive integer.")
else:
    print(f"Sum of first {num} natural numbers is: {sum_natural(num)}")
