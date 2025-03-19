set1={1,2,3}
set2 = {4,5,6}
my_set= set1.union(set2) #It will return unique values
print(my_set)

set3 = {1,2,3,4,5}
set4={4,5,6,7,8}
my_set2= set3.union(set4)
print(my_set2)

set3 = {1,2,3,4,5}
set4={4,5,6,7,8}
my_set2= set3.intersection(set4)  #will print common elements betn set# s
print(my_set2)

set3 = {1,2,3,4,5}
set4={4,5,6,7,8}
my_set2= set3.difference(set4) #it will give difference of set3 wrt to set 4
my_set3=set4.difference(set3)  #it will give difference of set4 wrt to set 3
print(my_set2)
print(my_set3)



