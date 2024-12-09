# write a program to take 2 user inputs and sum the number and print the sum

num1 = int(input("enter the number1:"))  # here whatever inputs we are taking are in the form of string so we need to convert it into int befor doing any math
num2 = int(input("enter the number2:"))

# or we can alsoo convert it into int by following method

# num1 = int(num1)
# num2 = int(num2)

# str>Int

sum = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2

print("sum is =", sum)
print("sub is =", sub)
print("Mul is =", mul)
print("Div is =", div)
