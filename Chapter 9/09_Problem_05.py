# 5. Repeat program 4 for a list of such words to be censored
no_of_words = int(input("Enter number of words to be cleaned: "))
words = []

'''
# most efficient
no_of_words = int(input("Enter number of words to be cleaned: "))
words = [input(f"Enter your words no. {i+1}: ") for i in range(no_of_words)]

'''
for i in range(1, no_of_words + 1):
    word = input(f"Enter your words no. {i}: ")
    words.append(word)

print("Words to be cleaned:", words)


def word_cleaner(words):
    try:
        for item in words :
            with open("donkey.txt", "r") as file:
                content = file.read()

            if item in content:
                cleaned_content = content.replace(item, "#" * len(item))
                with open("donkey.txt", "w") as file:
                    file.write(cleaned_content)
                    print(f"✅ Given word '{item}' cleaned successfully.")
            else:
                print(f"❌ The word '{item}' does not exist in the file.")
        
    except FileNotFoundError:
        print("⚠️ File 'donkey.txt' not found.")

word_cleaner(words)

# most efficient way to write def word_cleaner(words)
'''


def word_cleaner(words):
    try:
        with open("donkey.txt", "r") as file:
            content = file.read()

        original_content = content  # Keep a backup to compare later

        for item in words:
            content = content.replace(item, "#" * len(item))

        if content != original_content:
            with open("donkey.txt", "w") as file:
                file.write(content)
            print("✅ All specified words cleaned successfully.")
        else:
            print("❌ None of the specified words were found in the file.")

    except FileNotFoundError:
        print("⚠️ Error: File 'donkey.txt' not found.")
        
'''