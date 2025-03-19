my_list = [1,2,3]

#indexing

print("element at index 0-",my_list[0])
print("element at index 1-",my_list[1])
print("element at index 2-",my_list[2])

#append()  -->>Append object to the end of the list.

my_list.append(4)
my_list.append(5)
print(my_list)

#extend()-->we can extend with another list as well/append a new list

my_list.extend([6,7,9,8])
print(my_list)

#insert()-->it will used to insert element at specific index

my_list.insert(1,"shubham")
print(my_list)
print(len(my_list))

my_list.insert(0,0)
print(my_list)

my_list[1]="Amit"
print(my_list)

#remove-->to remove element from specific index

my_list.remove("Amit")
print(my_list)

print("_______________________________________________________")
print("_______________________________________________________")


#to create an copy of a list

my_copy_list = my_list.copy()
print(my_list)
print(my_copy_list)

#to sort the list we need to ake sure that strings should be removed

my_list.remove("shubham")
my_copy_list.remove("shubham")

my_copy_list.sort()
print(my_list)
print(my_copy_list)