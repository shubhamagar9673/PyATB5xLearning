# Create a program to sum of three number from the user input ,
# if user does not enter any number use default as 100,200 and 300
num1 = int(input("Enter first number\n"))
num2 = int(input("Enter second number\n"))
num3 = int(input("Enter third number\n"))


def sum_of_three_numbers(n1=100, n2=200, n3=300):
    return n1+n2+n3


result = sum_of_three_numbers(num1, num2, num3)
print(result)

result2 = sum_of_three_numbers()
print(result)
