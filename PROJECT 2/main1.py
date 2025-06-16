from random import randint 
n=randint(1,100)
a=int
guess=0
print("-----------------------------------")
print("Welcome !!!\nTo\nWord Guessing Game")
while (a != n) :
    a=int(input("Enter The Number between [1,100] :"))
    guess+=1
    if a > 100 or a < 1 :
        print("-----------------------------------")
        print("Pagal Hai ky Bhai\nek se soo ke bich bola na")
    elif a < n :
        print("-----------------------------------")
        print("Higher Number Please")
    elif a > n :
        print("-----------------------------------")
        print("Lower Number Please")
if a == n :
    print("-----------------------------------")
    print(f"Win Win !! You Gussed It correctly,\nthe Correct Number is {n}\nYou Won With Number of Guesses = {guess}")
    
