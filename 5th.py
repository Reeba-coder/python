# Functions in python
# function is used to seperate the code
#Function is a Block of code that perform a specific task when it is called.
# By using function you I'm print geometric mean 
# If you want using function you need def keyword 
def calculategmean (a,b):
    mean=(a*b)/(a+b)
    print (mean)
def greatervalue(a,b):
    if(a>b):
        print("First Number is greater:")
    else:
        print("Second Number is greater:")
a=10
b=7
calculategmean(a,b)
greatervalue(a,b)
c=7
d=47
calculategmean(c,d)
greatervalue(c,d)
#If you want to write a function but don't want to write its body yet, you can leave it for
#  later and write it like this. To avoid from error
# def islesser(a,b):
#     pass