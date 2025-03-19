cities = ("London","Paris","Tokyo","Mumbai")
print("Paris" in cities)
print("New Delhi" in cities)

#we can not append anything in the tuple
#to do that we need to convert it into list and then we can append

t = (12,34,56)
my_list=list(t)
my_list.append(4)
t=tuple(my_list)
print(t)