# 11. Write a python program to rename a file to “renamed_by_ python.txt.
import os

# Define the original file name and the new file name
original_file = "new106.txt"  # Ensure this file exists in the directory
new_file_name = "new0.txt"

# Rename the file
os.rename(original_file, new_file_name)

print(f"File renamed to {new_file_name}")
