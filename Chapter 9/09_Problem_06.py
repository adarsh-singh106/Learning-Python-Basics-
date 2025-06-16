# 6. Write a program to mine a log file and find out 
# whether it contains ‘python’. 
word=input ("Enter a word to search in Log file : ")
def log_search(word):
    # check wether that word exist or not 
    with open("log_file.txt") as f:

        content=f.read()  # f.read is InValid
        
        og_content=content # copy of the log_file is now present in content variabe
        if word in og_content :
            print(f"yes the word '{word}' is present in log file")
        else:
            print("NO , such word is present in log file")

log_search(word)