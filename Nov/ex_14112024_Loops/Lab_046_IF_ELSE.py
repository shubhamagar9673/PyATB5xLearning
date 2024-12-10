# Program to find max number among three

# Step1:- user inputs >>num1,num2,num3 will be int
# Step2:- o/p > int or string with max number
# Step3:-this we can do it by if -elseif-else statement
# syntax for this is:-
"""
if condition1:
    print("do 1")
    elif condition2:
    print("do 2")
else:
    print("do 3 ")
    """

num1 = int(input("enter first number:"))  # 5   10
num2 = int(input("enter second number:"))  # 3  12
num3 = int(input("enter third number:"))  # 2   11

# 5>3 and 5>2  -->>5
# num1>num2 and num1> num3 -->num1

# if number 2 is greater
# 12>10 and 12>11 -->12
# num2>num1 and num2 >num3 --> num2

# if above both conditions are false then by default num3 will be greater

if num1 > num2 and num1 > num3:
    print("number 1 is greater", num1)
elif num2 > num1 and num2 > num3:
    print("number two is greater", num2)
else:
    print("number three is greater", num3)

# Step4:-Edge Cases
