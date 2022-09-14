# Raise 
"""
def raise_int(input):
    if type(input) != float:
        raise TypeError("Not a float")
    else:
        print("Input is a Float")

raise_int(1.1)
"""
#Input validation
"""
try:
    user_int = int(input("Input number: "))
except Exception:
    print("Sorry, that is not a number")
    user_int = int(input("Input number: "))
    if(user_int%2 == 0):
        raise Exception("Input is even")
"""
#Try/Except
"""
def divide_by_zero(x,y):
    try:
       return x/y
    except ZeroDivisionError:
        print("Division by zero is not allowed")
    except TypeError:
        print("y is not a number")

divide_by_zero(5,0)
"""
#Import
"""
from math import sqrt
from random import randint
from calc import addition

print(sqrt(16))
print(randint(1,10))

print(addition(2,2))
"""
#Lambda

num_ls = list(range(1,11))
num_ls = list(map(lambda x: x+1,num_ls))
print(num_ls)