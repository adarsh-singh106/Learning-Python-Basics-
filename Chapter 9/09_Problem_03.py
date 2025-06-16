# 3. Write a program to generate multiplication tables from 2 to 20 and write it to the 
# different files. Place these files in a folder for a 13 – year old. 
def multiplication_table(n):
    a=""
    for i in range(1,11):
        a+=f"{n} X {i} = {n*i}\n"
        
    with open(f"13 - year old/table{n}.txt","w") as files:
        files.write(a)


        
for i in range(2,21):
    multiplication_table(i)