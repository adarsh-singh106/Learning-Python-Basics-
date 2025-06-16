# 3. A spam comment is defined as a text containing following keywords: 
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
# to detect these spams.
comment = input("Enter Your Comment :")
p1 = "Make a lot of money"
p2 = "buy now"
p3 = "click this"
p4 = "subscribe this"
if((p1 in comment) or(p2 in comment) or (p3 in comment) or (p4 in comment)):
    print("The comment is invalid")
else:
    print("The comment is valid")