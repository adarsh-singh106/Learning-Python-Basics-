# 6. Write a program to calculate the factorial of a given number using for loop
while True:
    try:
        num = int(input("Enter a non-negative integer: "))
        if num < 0:
            print("Oops! Factorial is not defined for negative numbers. Please try again.")
        else:
            break  # Valid input, exit the loop
    except ValueError:
        print("That's not a valid integer. Please enter a non-negative integer.")

factorial = 1

for i in range(2, num + 1):
    factorial *= i

print(f"{num}! = {factorial}")
