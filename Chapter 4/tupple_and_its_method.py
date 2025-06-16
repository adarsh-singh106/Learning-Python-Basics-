# tupple is kind off same as list but it is immutable (cant be update the same tupple once declared)
# it is written in simple bracket
t1=()  # empty tupple
t2=(1,)  # single element tupple
t3=(1,4,3,"ash",False,45.3,-9,7,9,7)  # Multi element tupple 
print("Type of t1 is :",type(t1))
print("Type of t2 is :",type(t2))
print("Type of t3 is :",type(t3))
print(t3.count(7)) # counts how mant time 7 appers in tupple 
print(t3.index(7)) # serches for index of 7 from starting 
                   # Ignoring all the 7 present after that in the tupple