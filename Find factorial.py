import math
from math import *

a = 1
b = math.factorial(5)
print (b)

def fectorial():
    print("Find factorial")
    result = 1
    n = int(input("Enter number "))
    for i in range(1,n+1):
        result *= i

    print("Factorial of {0} is {1}".format(n,result))

fectorial()
