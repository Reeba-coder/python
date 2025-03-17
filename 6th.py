# Function arguments
# Default Argument  
def average (a, b):
    print("The Average of is:" , (a+b)/2)

average (10,20)
def avg (a , b=10):
    print ("The number of Average is:" , (a+b)/2)

# avg (b=3) if you rewrite the value of b but not write the value of a then pass the
#  TypeError like this "TypeError: avg() missing 1 required positional argument: 'a'"
avg(a=10)
#Variable length argument  
def average1(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print("The average is:", sum/len(numbers))
average1 (10,45,23,97,72) # the variable length is usd this way if you find a length more than 3 numbers
def average1(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    # print("The average is:", sum/len(numbers)) 
    # By using return function
    return sum/len(numbers)
c= average1 (5,4,3,2,1)
print (c)    