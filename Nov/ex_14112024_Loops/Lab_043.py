#Write a program to take input as user age and let him know if he can go to a club : age=21

age = int(input("enter the age :"))
print(age)
#print("you can go to the club "if age>=21 else "you will not be able to go to club")
if age>=21:   #no need of brackets in case of python
    print("you can go to the club")
else:
    print("you cant go to the club")

#check for edge cases
#we should consider edge cases such as :-1)if age is -ve or extremely high value program will break
#2)if you add alphaanumeric value ex:abc
#3)if age is grater than 130 as it is not possible

#next step is to optimize the code
#i,e handle all the edge cases
