# 1) They can not return anything ->non return

# no return type with no parameter

def greet():
    print("Hello")
    greet()


# 2)they can return something
# No return type with argument

def greet_by_name(name):
    print("Hello,", name)


greet_by_name("Shubham")


# 3)They have parameters

# no return type with default argument

def say_hello_default_arg(name="Shubham"):
    print("Hello,", name.upper())
    say_hello_default_arg()
    say_hello_default_arg("omkar")

def multiple_args(name1="A", name2="B"):
    print("Hello," , name1 , name2)
    multiple_args()
    multiple_args(name1="Shubham")
    multiple_args(name1="Shubham",name2="Omkar")

# 4)They  dont have parameters;
#Argument + return Type

def sum_of_two(a,b):
    return a+b
result = sum_of_two(4,56)
print(result)

#we can also use default arguments

def sum_of_two_Number_default(num1="100", num2="200"):
    return num1+num2
result = sum_of_two_Number_default(34,34)
print(result)
result = sum_of_two_Number_default()
print(result)

