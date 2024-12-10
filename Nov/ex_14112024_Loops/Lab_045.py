#program to find max number between two

#Step1:-user inputs->> two integers
#Step2:- o/p will be one int whichever is the max number
#Step3:-it should also support float numbers as well

num1 = float(input("enter first number:"))
num2 = float(input("enter second number:"))

if num1>=num2:
    print("number one is greater",num1)
else:
    print("number two is greater",num2)

#Step4:-edge cases
#1) if num1 ==num2 >>it is handeled in this case we are printing num1 by giving condition as num1>=num2
#2)if user enters abc i,e string ->> this can be handled by try catch block
#3)-ve values should also needs to be handled

