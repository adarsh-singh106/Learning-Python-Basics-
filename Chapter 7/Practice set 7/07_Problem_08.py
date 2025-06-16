# 8. Write a program to print the following star pattern: 
# * 
# ** 
# ***      for n = 3 
n = int(input("Enter the value of n to print star pattern: "))
print(f"Star Pattern With n = {n}")

# Loop through rows and print stars
for i in range(1, n + 1):
    print('*' * i)# newline Character is already in it by default 