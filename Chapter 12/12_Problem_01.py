# 1. Write a program to open three files 1.txt, 2.txt and 3.txt
#  if any these files are not present, a message without exiting
#  the program must be printed prompting the same. 


#❌ The with block fails immediately if any of the files don't exist —
#  even before the try blocks start.
try:
    with open("f1.txt", "r") as f1:
        file1 = f1.read()
except FileNotFoundError:
    print("File f1.txt does not exist")

try:
    with open("f2.txt", "r") as f2:
        file2 = f2.read()
except FileNotFoundError:
    print("File f2.txt does not exist")

try:
    with open("f3.txt", "r") as f3:
        file3 = f3.read()
except FileNotFoundError:
    print("File f3.txt does not exist")
