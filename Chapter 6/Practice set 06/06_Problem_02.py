# 2. Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user. 
p=int(input("Enter your physics marks:"))
c=int(input("Enter your chemistry marks:"))
m=int(input("Enter your maths marks:"))
total_marks=((p+c+m)/300)*100
if(total_marks>=40):
    if(p>=33 and c>=33 and m>=33):
        print(f"You are passed the exam with {total_marks}%")
    else:
        print(f"Fail hogaya bhai with {total_marks}%")
else:
    print(f"gandu hai app with {total_marks}%")

    