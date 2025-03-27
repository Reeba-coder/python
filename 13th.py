#DocString in python
# Python Docstring are a string Literal that appear right after the definition of function,method
# class or module 
def square(n):
    '''Take in a number n, return the square of n'''# it's docstring
    print(n**2)
square(5)
print(square.__doc__) # Docstring is not ignore Like comments it's print astit 
import this # it's print the Zen of python (That provide a poem of python (Easter egg))