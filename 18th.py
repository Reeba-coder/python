#Program 1: Find the largest of three numbers
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
if a>=b and a>=c:
    print("The largest number is:",a)
elif b>=a and b>=c:
    print("The largest number is:",b)
else:
    print("The largest number is ",c)

# Program 2: Check if number is even or odd using function
def number(n):
    if n%2==0:
        print("The number is even")
    else:
        print("The number is odd")
n=int(input("Enter a number:"))
number(n)

#Program 3: Print table of a number using loop
n=int(input("Enter a number:"))
for i in range(1,11):
    print(n ,"*",i,"=",n*i)

#Program 4: Count vowels in a string
a=input("Enter a string:")
count=0
for i in a:
    if i.lower() in "aeiou":
        count+=1
print("The number of vowels in the string is:" ,count)

#Program 5: Check if number is prime using function
def prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=int(input("Enter a number:"))
if prime(n):
    print(n,"is prime")
else:
    print(n,"is not prime")