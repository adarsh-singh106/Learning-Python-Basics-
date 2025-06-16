# 2. Write a program to fill in a letter template given below with name and date. 
# letter = '''  
# Dear <|Name|>, 
# You are selected! 
# <|Date|> 
# ''' 
name=input("Enter your Name : ") 
date=input("enter date : ")
print("Using f quote and entering the name indirectly ")
print(f'''Dear {name}, 
You are selected! 
{date}'''
 )
print("using replace function of str")
letter = '''  
Dear <|Name|>, 
You are selected! 
<|Date|>'''
print(letter.replace("<|Name|>","ash").replace("<|Date|>","24-05-2025"))
