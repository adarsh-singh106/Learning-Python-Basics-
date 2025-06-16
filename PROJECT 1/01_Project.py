dict={
    1:"snake",
    2:"water",
    3:"gun"
}
def choose(name):
    print(dict)
    print(f"Dear {name}\nchoose from the above dict\nand enter the corresponding key(i.e 1,2,3)")
    key=int(input("Enter Your key :"))
    return key
n1=input("Player-1 , Enter Your name :")
n2=input("Player-2 , Enter Your name :")
print("--------------------------------------------")
a=choose(n1)
print("--------------------------------------------")
b=choose(n2)
print("--------------------------------------------")
if((a==1 and b==2) or b==1 and a==2) :
    # n1 = snake and n2 = water , s>w
    if(a==1 and b==2):
        print(f"snake drinks the water hence \n the winner is {n1}")
    else:
        print(f"snake drinks the water hence \n the winner is {n2}")
elif((a==2 and b==3) or b==2 and a==3) :
    # n1 = water and n2 = gun , w>g
    if(a==2 and b==3):
        print(f"Gun will drowns in water hence \n the winner is {n1}")
    else:
        print(f"Gun will drowns in water hence \n the winner is {n2}")
elif((a==3 and b==1) or b==3 and a==1) :
    # n1 = gun and n2 = snake , g>s
    if(a==3 and b==1):
        print(f"Gun kills the snake hence \n the winner is {n1}")
    else:
        print(f"Gun kills the snake hence \n the winner is {n2}")

