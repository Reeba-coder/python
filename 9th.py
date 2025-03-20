# Tuples in python 
tup=(1,3,5,7)
print(type(tup)) # Tuples doen't like list 
print(tup)
print(len(tup))
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
if 9 in tup:
    print("yes")
else:
    print("No")
tup2=tup[1:3] #To create new tuple Slicing allow in Tuple as like List
print(tup2)