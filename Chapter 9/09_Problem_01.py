# 1. Write a program to read the text from a given file ‘poems.txt’ and find out 
# whether it contains the word ‘twinkle’.
file_open=open("poems.txt","r") # is same as passing 2 parameters open("poems,txt","r")
text=file_open.read()
# print(text.find("twinkle"))
print(text) # content will be copied in text named variable
print(text.find("twinkle"))
print(text.count("twinkle"))
file_open.close


# Source code

'''f = open("poem.txt")
content = f.read()
if("twinkle" in content):
    print("The word twinkle is present in the content")

else:
    print("The word twinkle is not present in the content")

f.close()'''