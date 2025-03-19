#write a program to calculate even or odd

def find_even_odd(num):
    if num%2 ==0:
        print("even")
    else:
        print("odd")
find_even_odd(5)


#to convert it into lambda
n = int(input("Enter a number \n"))
check_odd_even = lambda num:"even"if num%2==0 else "odd"
print(check_odd_even(n))