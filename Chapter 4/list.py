# 1. List Is The Collection of Multiple elements Of Different DataTypes
# 2. It is written in SQ.Bracket
# 3. Normal Type of Indexing as that of str 
# 4. After performing operation/Methods on list , it gates updated to the 
#   last funtion performed before moving to the next line of code
# 5. It is Mutable That Changes Can Be made in the Same List With Same Variable Name 
List=["ash","may","max",'@',2.8,78,False,True,"Brock"]
print(List[0])
print(List[6])
# print(List[895])  >>>> Gives Error
print(List[0:2])
print(List[:9]) # Is Same As print(List[:19]) #Does not Matter if range exeeceds The length
print(List[:19])
print(List[0:])
print("after changing the the element in list directly using indexing \n which  is not possible in tuple")
List[0]=45
print(List)