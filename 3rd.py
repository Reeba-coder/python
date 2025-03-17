name= "Reeba"
print ("Hello," + name)
#  you cannot use a multiple time double quotes in single string
apple = 'He said, "I want to eat apple".'
print (apple)
# you see the benefit of triple quotes and It's convinent if you write string on multiple lines
apple='''He said , 
I'm Reeba
Hey I'm good
" I want to eat apple".'''
print (apple) 
name = "Reeba"
print (name[0])
print (name[1])
print (name[2])
print (name[3])
print (name[4])
# print (name[5]) index error
 
#  String slicing
names="Reeba , Rasheed"
print (len (names))
fruit= "mango, apple"
mangolen=len(fruit)
print(mangolen)
print (fruit[4:11])
# print (fruit[-1:-10]) is not a valid because 12-1=11 and 12-10=2 (10,2) combination not right left value greater than right
print(fruit[-10:-1]) # is valid because the combination of (2,10)

# Quick quiz
nm="Reeba"
print (nm[-4:-2])