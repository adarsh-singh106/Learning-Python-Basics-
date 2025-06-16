# 8. Write a program to make a copy of a text file “this. txt”
def fetch_file():
    with open("log_file.txt") as ff:
        Content=ff.read()
        og_copy=Content
        with open("this.txt","w") as op:
            op.write(og_copy)
            print("copy is generated")

fetch_file()

'''

# 8. Write a program to make a copy of a text file “this.txt”

def fetch_file():
    try:
        with open("log_file.txt", "r") as source_file:
            content = source_file.read()

        with open("this.txt", "w") as copy_file:
            copy_file.write(content)

        print("✅ File copied successfully to 'this.txt'")

    except FileNotFoundError:
        print("⚠️ Source file 'log_file.txt' not found.")

fetch_file()


'''