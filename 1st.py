print("Hey",6,7.5,sep="~")
a=1
print(a)
# print ("The type of a is " type [a])
b =complex(8,2)
# print ("the complex number is " b)
list= [8,2,3,[-4,5],["apple","Banana"]]
print (list)

# Exercise no 1: create a small calculator
a=56
b=3
print ("The value of",a ,"+" ,b ,"is=", a+b)
print ("The value of",a ,"-" ,b, "is=", a-b)
print ("The value of",a ,"*" ,b, "is=", a*b)
print ("The value of",a ,"/" ,b, "is=", a/b)

# To convert string into integer ( Explict type casting)
a="1"
b="2"
# print (a+b) is invalis because if you add both is provide 12 instead of 3
print (int (a) +int (b))