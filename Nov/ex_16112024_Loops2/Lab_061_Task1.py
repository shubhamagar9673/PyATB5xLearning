"""Write a program that prints number from 0 to 100 . However, for multiples of 3,
print "Fizz" instead of the number , and for multiple of 5, print"BUZZ".
for numbers that are multiples of both 3 and 5, print "FIZZBUZZ"
(For and if loop)"""

for i in range(101):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)