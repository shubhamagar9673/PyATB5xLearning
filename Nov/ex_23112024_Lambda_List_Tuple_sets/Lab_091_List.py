# List-->>Collection of items
# grocery_List = butter,bread,sugar

my_list = [1, 2, 3]  # same type of data i,e int
my_list2 = [3.12, "passwprd", 2]  # can contain different datatypes

print(my_list)
print(len((my_list)))
print(my_list[0])
print(my_list[1])
print(my_list[2])
#print(my_list[3])  # List index out of range
print(my_list2)


#reassigning the values

my_list[0]="Shubham"
my_list[1]="rameshrao"
my_list[2]="magar"
print(my_list)


#to iterate items in list
#here we have not used range beacuse at the end it returns a list

for i in my_list2:
    print(i)