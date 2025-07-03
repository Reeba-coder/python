#Write a Python program to input a number from the user and check whether it is a prime number or not. Also, print whether the number is even or odd.
def prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=int(input("Enter a number:"))
if prime(n) and n%2!=0:
    print(n , "is prime and odd")
else:
    print(n,"is not prime and even")
 
a=input("Enter a string:")
count=0
for i in a:
    if i.lower() in "aeiou":
        count+=1
print("The string is has following vowels=", count)

n=int(input("Enter a number:"))
for i in range(1,11):
    print(n,"*",i,"=", n*i)

def factorial(n):
    result=1
    for i in range(1,1+n):
        result*=i
    return result
n=int(input("Enter a number:"))
print("The factorial of number",n, "is", factorial(n))

a= input("Enter a string:")
if a==a[::-1]:
    print("THe string is palindrome",a)
else:
    print("THe string is not palindrome",a)
    
n=[1,2,3,3,4,5,6,7,8,9]
even=0
odd=0
for i in n:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("Enev number", even)
print("odd number",  odd)