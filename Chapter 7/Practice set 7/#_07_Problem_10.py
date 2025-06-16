# 10. Write a program to print multiplication table of n using for loops in reversed 
# order.
num1 = int(input("Enter a Number: "))

print("--- Multiplication Table in Reverse (Using for loop) ---")
for i in range(10, 0, -1):
    print(f"{num1} x {i} = {num1 * i}")

num2 = int(input("Enter a Number: "))

print("--- Multiplication Table in Reverse (Using while loop) ---")
j = 10
while j >= 1:
    print(f"{num2} x {j} = {num2 * j}")
    j -= 1
