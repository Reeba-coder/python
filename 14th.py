# Recursion in Python
# call itself is called recursion
def factorial(n):
    if(n==0):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(7))
# Fibonocci series calculate function
def fibonacci(n):
    fib=[0,1]
    while len(fib)<n:
        fib.append(fib[-1]+fib[-2])
    return fib
num=10
print(fibonacci(num))