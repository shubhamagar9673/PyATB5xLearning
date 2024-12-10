"""
write a program that classifies a triangle based on its side lengths . Given three input values
representing the lengths of the sides, determine if triangle is equilateral (all sides equal)
,isosceles(exact two sides are equal),or scalene(no side equal).Use if-else statement to classify the triangle

"""

side1= int(input("Enter side 1 of the triangle:"))
side2= int(input("Enter side 2 of the triangle:"))
side3= int(input("Enter side 3 of the triangle:"))

if side1==side2 and side2==side3:
    print("Triangle is equilateral")
elif side1==side2 or side1==side3 or side2==side3:
    print("triangle is isosceles")
else :
    print("Triangle is scalene")
