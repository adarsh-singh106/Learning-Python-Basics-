# 10. Write a program to wipe out the content of a file using python. 
# 10. Write a program to wipe out the content of a file using python. 
print("starting\n.\n.\n.")
def wipe_out():
    with open("highscore.txt","w") as f:
        og=f.write("")
        print("sucess")
wipe_out()

'''
           # efficient way of wrting the above
def wipe_file_content(file_path="highscore.txt"):
    try:
        with open(file_path, "w") as f:
            f.write("")  # Wipes out all content
        print(f"✅ '{file_path}' has been wiped clean.")
    except Exception as e:
        print(f"❌ Failed to wipe file: {e}")

print("Starting...\n.\n.\n.")
wipe_file_content()


'''
