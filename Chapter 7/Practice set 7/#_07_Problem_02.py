# 2. Write a program to greet all the person names stored in a list ‘l’ and which starts 
# with S. 
# l = ["Harry", "Soham", "Sachin", "Rahul"]
list = ["Harry", "Soham", "Sachin", "Rahul"]
for item in list:
    if(item[0].lower()=="s"):
        print(f'''Hello!!!Mr.{item}
We are so glad that You topped The FF leaderboard''')
    