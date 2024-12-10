#leap year is the year which is multiple of 4 , except for years evenly divisible by 100 but not by 400

enter_year=int(input("enter the year:"))
print(enter_year)

if (enter_year%4 ==0 and enter_year%100 !=0 ) or (enter_year%400==0):
    print("year is leap year")
else:
    print("year is not a leap year")