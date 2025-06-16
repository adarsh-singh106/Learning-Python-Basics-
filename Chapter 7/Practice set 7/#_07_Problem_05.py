# Program to find the summation of first 'n' natural numbers using:
# 1. For loop
# 2. While loop
# 3. Mathematical formula
# Try for yourself with very large number to see the output inn speed
# Take input from the user
n = int(input("Enter a number: "))

# ---------------------------
# 1. Using a FOR loop
# ---------------------------
print("\n--- Using for loop ---")
n_sum = 0
for i in range(1, n + 1):  # Loop from 1 to n (inclusive)
    n_sum += i
print(f"The summation of first {n} natural numbers is: {n_sum}")

# ---------------------------
# 2. Using a WHILE loop
# ---------------------------
print("\n--- Using while loop ---")
m_sum = 0
j = 1
while j <= n:              # Loop until j reaches n
    m_sum += j
    j += 1
print(f"The summation of first {n} natural numbers is: {m_sum}")

# ---------------------------
# 3. Using MATHEMATICAL FORMULA
# ---------------------------
print("\n--- Using formula ---")
sum_formula = n * (n + 1) // 2  # Efficient formula-based approach
print(f"The summation of first {n} natural numbers is: {sum_formula}")
