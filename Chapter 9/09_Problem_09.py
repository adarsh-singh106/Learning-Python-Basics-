# 9. Write a program to find out whether a file is identical & matches the content of 
# another file.
print("starting\n.\n.\n.")
def file_x_file():
    with open("log_file.txt") as file1:
        content1=file1.read()
    with open("this.txt") as file2:   # same content as file 1
        content2=file2.read()
    # with open ("donkey.txt") as file2:  # diiferent from file 1
    #     content2=file2.read()
    if content1 == content2 :
        print("Both Files have the same content ")
    else:
        print("Both Files have the different content ")
file_x_file()