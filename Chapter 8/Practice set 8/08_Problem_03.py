# 3. How do you prevent a python print() function to print a new line at the end.
print("Hello, world!", end="")
print("This is on the same line.")
# By default, print() uses end="\n", but you can 
# change it to any string, including a space (" ") or a comma (",").
print("---------------------------------")
print("Hello, world!",end="")
print("This is on the same line.")