# 2. Write a program to accept marks of 6 students and display them in a sorted 
# manner.
marks_of_student=[]
m1=int(input("Enter marks of student no.1 :"))
m2=int(input("Enter marks of student no.2 :"))
m3=int(input("Enter marks of student no.3 :"))
m4=int(input("Enter marks of student no.4 :"))
m5=int(input("Enter marks of student no.5 :"))
m6=int(input("Enter marks of student no.6 :"))
m7=int(input("Enter marks of student no.7 :"))
marks_of_student.append(m1)
marks_of_student.append(m2)
marks_of_student.append(m3)
marks_of_student.append(m4)
marks_of_student.append(m5)
marks_of_student.append(m6)
marks_of_student.append(m7)
marks_of_student.sort()
print(marks_of_student)