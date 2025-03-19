import math


def power(num):
    return math.pow(num, 2)


result = power(2)
print(result)

# this we can do with labda as below

op = lambda: math.pow(int(input("enter the number \n")), 2)
print(op)
