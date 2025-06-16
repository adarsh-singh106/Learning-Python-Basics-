# 7. Write a program to find out the line 
# number where python is present from ques 6. 
word = input("Enter a word to search in Log file: ")

def log_search(word):
    try:
        with open("log_file.txt", "r") as file:
            lines = file.readlines()

        line_no = 1
        found = False
        for line in lines:
            if word in line:
                print(f"✅ The word '{word}' is present at line no. {line_no}")
                found = True
            line_no += 1

        if not found:
            print(f"❌ The word '{word}' is not found in the file.")
    except FileNotFoundError:
        print("⚠️ File not found.")

log_search(word)

 
 # most efficient version
'''

# 7. Find line number(s) where a word (e.g., 'python') appears in the log file

word = input("Enter a word to search in log file: ")

def log_search(word):
    try:
        found = False
        with open("log_file.txt", "r") as f:
            lines = f.readlines()

        for i, line in enumerate(lines, start=1):
            if word in line:
                print(f"✅ The word '{word}' is present at line number {i}")
                found = True

        if not found:
            print(f"❌ The word '{word}' is not found in the file.")

    except FileNotFoundError:
        print("⚠️ Error: The log file 'log_file.txt' was not found.")

log_search(word)


'''