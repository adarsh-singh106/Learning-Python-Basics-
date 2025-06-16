# 4. A file contains a word “Donkey” multiple times. You need to write a program 
# which replace this word with ##### by updating the same file.  
word=input("Enter a Word To Be removed : ")
def word_cleaner(word):
    with open ("donkey.txt","r") as file:
        word_pad=file.read()
        if word in word_pad :
            new=word_pad.replace(word,"#"*len(word))
            with open("donkey.txt","w") as file:
                file.write(new)
            print("Given Word Cleaned Successfully")
        else:
            print(f"the word {word} Does not exist in the file")

word_cleaner(word)
'''
ai-version 

word = input("Enter a word to be removed: ")

def word_cleaner(word):
    try:
        with open("donkey.txt", "r") as file:
            content = file.read()

        if word in content:
            cleaned_content = content.replace(word, "#" * len(word))
            with open("donkey.txt", "w") as file:
                file.write(cleaned_content)
            print("✅ Given word cleaned successfully.")
        else:
            print(f"❌ The word '{word}' does not exist in the file.")
    except FileNotFoundError:
        print("⚠️ File 'donkey.txt' not found.")

word_cleaner(word)
'''