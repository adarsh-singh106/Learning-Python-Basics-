# 3. A list contains the multiplication table of 7. write a program to convert it to vertical 
# string of same numbers.
list_l=[]
def table(n):
    for i in range (0,10):
        ld=f"{n} X {i+1} = {n*(i+1)}"
        list_l.append(ld)
    print("Table is Uplated in list")
n=int(input("Enter a Number : "))
table(n)
print("------------------------------------")
print("The Elements inside the list is joined with\nNEWLINE CHARACTER to make vertical")
vertical_table="\n".join(list_l)
print("------------------------------------")
print(vertical_table)