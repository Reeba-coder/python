#List method in python
l=[1,5,3,7,2,1,4]
print(l)
l.sort()
l.append(9) # To add number in your list
print(l)
l.reverse()
print(l)
print(l.index(3))
print(l.count(1))
m=l.copy() #Duplicate of your original list  you change in this but your
#original list always same
# m[0]= 0
# print(l)
l.insert(1,90) #this means that you add 90 in index 1 
print(l)
m=[10,11,12]
# l.extend(m) 
k=l+m
print(k)

