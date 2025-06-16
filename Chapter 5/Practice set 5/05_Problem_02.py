# 2. Write a program to input eight numbers from the user and display all the unique 
# numbers (once).
set_of_numbers=()    #class <tuple>
set_of_numbers=set() #class <set>   writing set before empty set is neccessary 
# print(type(set_of_numbers))
s1=int(input("Enter the first number:"))
s2=int(input("Enter the second number:"))
s3=int(input("Enter the third number:"))
s4=int(input("Enter the fourth number:"))
s5=int(input("Enter the fifth number:"))
s6=int(input("Enter the sixth number:"))
s7=int(input("Enter the seventh number:"))
s8=int(input("Enter the eighth number:"))
set_of_numbers.add(s1)
set_of_numbers.add(s2)
set_of_numbers.add(s3)
set_of_numbers.add(s4)
set_of_numbers.add(s5)
set_of_numbers.add(s6)
set_of_numbers.add(s7)
set_of_numbers.add(s8)
print(set_of_numbers)

