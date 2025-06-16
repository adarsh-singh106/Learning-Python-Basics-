# 4. Write a program to display a/b where a and b are integers. If b=0, display infinite by 
# handling the ‘ZeroDivisionError’.
a=int(input("Enter a Number a :"))
b=int(input("Enter a Number b :"))
try:
    result = a / b
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero!")
