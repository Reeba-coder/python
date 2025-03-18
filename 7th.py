#Introduction to list in python
marks=[3,5,8,10,12,16,7,9]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[-3]) # Negative index -3 lenght you find to subtract -3 with total lenght 4-3=1 
# if you see this output after run that show you value of 5 that place on index 1
if 5 in marks:
    print("Yes")
else:
    print("No")
print(marks[0:3:2]) #jump indexing
# List comprehension
lst=[i for i in range(4)]
print(lst) # provide output[0,1,2,3]
lst=[i*i for i in range(4)]
print(lst)# provide output[0,1,4,9]
lst=[i*i for i in range(10) if i%2==0]
print(lst) # provide output[0,4,16,36,64] print only even index values
