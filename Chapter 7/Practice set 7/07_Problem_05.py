# 5. Write a program to find the sum of first n natural numbers using while loop.
n=int(input("Enter a number:"))
n_sum=0
i=1
print("---Using for loop----")
for i in range(1,n+1):
    if(i!=n+1):
        n_sum=n_sum+i
    else:
        break
i=i+1
print(f"The sumation Of First {n}Natural Number Is \n{n_sum}")

print("---Using while loop----")
m_sum=0
j=1
while(j<=n):
    m_sum+=j
    j+=1
print(f"The sumation Of First {n} Natural Number Is \n{m_sum}")
