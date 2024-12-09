name = "this is the big line"
print(type(name))
# name = name+1       #Concatination between string and int is not possible ,we can only concatinate str with str
name = name + str(1)  # after converting it into string we can do
print(name)

First_Name = "Shubham"
Last_Name = "Magar"
Full_Name = First_Name + " " +Last_Name
print(Full_Name)
print(type(Full_Name))
