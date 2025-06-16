# 4. Write a program to find whether a given number is prime or not.
num = int(input("Enter a number: "))
# By definition, a prime number is:
# A natural number greater than 1 that has exactly 
# two positive divisors 1 and itself.
'''Every number > √n that divides n has a partner < √n.

That partner gets tested early, so you don’t need to test the larger one.

This is why you can safely stop at √n in a prime-check loop.
if num <= 1:'''

if(num<=1):
    print("The Entered Number is Not Prime")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("The Entered Number is Prime Number")
    else:
        print("The Entered Number is Not Prime")
