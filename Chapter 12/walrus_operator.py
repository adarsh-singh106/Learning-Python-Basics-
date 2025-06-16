'''

:= is called the Walrus Operator.

It lets you assign and use a variable at the same time.

Useful in if, while, and other expressions to save lines of code.

It makes code shorter and easier to read — especially in loops and conditionals

'''
# numbers = [1, 2, 3, 4, 5]
# if len(numbers) > 3:
#     print(f"List is too long ({len(numbers)} elements, expected <= 3)")

if (value := input("Enter something: ")) != "":
    print(f"You typed: {value}")
if (input("Enter something: ")) != "":
    print(f"You typed: {value}")

value = input("Enter something: ")
if value != "":
    print(f"You typed: {value}")
