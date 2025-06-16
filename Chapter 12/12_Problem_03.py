# 3. Write a list comprehension to print a list 
# which contains the multiplication table of a 
# user entered number.
n=int(input("Enter a Number :"))
l=[]
for i in range(0,10):
    l1=f"{n} X {i+1} = {n*(i+1)}"
    l.append(l1)

print(l)

# harrys code
'''n = int(input("Enter a number: "))

table = [n*i for i in range(1, 11)]
print(table)'''