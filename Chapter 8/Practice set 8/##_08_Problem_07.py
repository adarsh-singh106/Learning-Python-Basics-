# 7. Write a python function to remove a given word from a list ad strip it at
#  the same time.

def remove_and_strip(word_list, word_to_remove):
    return [item.strip() for item in word_list if item.strip() != word_to_remove]

# Example usage:
words = [" apple ", "banana", " orange ", "banana ", "grape"]
filtered_words = remove_and_strip(words, "banana")
print(filtered_words)  # Output: ['apple', 'orange', 'grape']
