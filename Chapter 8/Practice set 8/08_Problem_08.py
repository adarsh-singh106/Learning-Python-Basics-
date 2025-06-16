# 8. Write a python function to print multiplication table of a given number.
def multiplication_table(n):
    for i in range(1,11):
        print(f"{n}X{i}={n*i}")
def multiplication_reverse_table(n):
    for j in range (10,0,-1):
        print(f"{n}X{j}={n*j}")
num=int(input("Enter a Number : "))
multiplication_table(num)
print("--------------------------")
multiplication_reverse_table(num)