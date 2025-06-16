# 5. Write a program which finds out whether a given name is present in a list or not.
name_list = ["adarsh","singh","Ash","sanket","sarena","misti","Brock"]
name=input("Enter Your Name to check Your Eligibility:")
if(name in name_list):
    print("Your Name Is Present In The List\nThus You Are Eligible")
else:
    print("Your Name Is not Present In The List\nThus You Are not Eligible")