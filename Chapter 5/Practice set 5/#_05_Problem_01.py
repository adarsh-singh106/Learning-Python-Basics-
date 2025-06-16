# 1. Write a program to create a dictionary of Hindi words with values as their English 
# translation. Provide user with an option to look it up! 
Hindi_dict={
    "ladka":"Boy",
    "ladki":"Girl",
    "pita":"father",
    "maa":"mother",
    "gand":"ass",
    "ganja":"Drugs"

}
print(Hindi_dict.keys())
key_for_dict=input("Enter any of the key from above available opptons:")
print(Hindi_dict.get(key_for_dict))