# 4. What will be the length of following set s: 
# s = set() 
# s.add(20) 
# s.add(20.0) 
# s.add('20') # length of s after these operations? 
s = set() 
s.add(20) # as value of 20 and 20.0 remains the same thus they both treated as same
s.add(20.0) 
s.add('20')
print(len(s))

