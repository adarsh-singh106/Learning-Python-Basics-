# 5. Store the multiplication tables generated 
# in problem 3 in a file named Tables.txt. 
n=int(input("Enter a Number :"))
l=[]
for i in range(0,10):
    l1=f"{n} X {i+1} = {n*(i+1)}"
    l.append(l1)

print(l)
with open ("Tables.txt","w") as f:
    f.write(str(l))
    print("Tables added succesfully !!!")