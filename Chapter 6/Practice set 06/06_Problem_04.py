# 4. Write a program to find whether a given username contains less than 10 
# characters or not.
user_name=input("Enter Your Username:")
if(len(user_name)<=10):
    if(len(user_name)<10):
        print(f"Length Of The entered Username Is Less Than 10 ,\nas Length of username is {len(user_name)}")
    else:
        print(f"Length Of The entered Username Is equals to 10 ,\nas Length of username is {len(user_name)}")
else:
    print(f"Length Of The entered Username Is greater Than 10 ,\nas Length of username is {len(user_name)}")