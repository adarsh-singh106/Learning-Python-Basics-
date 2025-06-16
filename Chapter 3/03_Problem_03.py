# 3. Write a program to detect double space in a string.
String="my name is adarsh singh,and i am good for nothing"
ds_index=String.find("  ")
print("-----------------------------------------")
print(f"Using .find funtion , it finds that word/charater in string \n and returns its index i.e {ds_index}")
ds_no=String.count("  ")
print("-----------------------------------------")
print(f"using count function , it count no. of times that word/character appers in \n that string {ds_no}")