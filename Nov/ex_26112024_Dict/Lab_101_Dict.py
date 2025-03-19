my_dict = {
    "name": "Shubham",
    "age": "25",
    "role": "SDET",
    "Experience": 3
}
print(my_dict)
print(my_dict["age"])

my_dict["role"] = "Manual tester"
print(my_dict)

del my_dict["age"]
print(my_dict)


#to iterate within the dictionary

for key,value in my_dict.items():
    print(key, "->", value)

print("Age" in my_dict)
print("role" in my_dict)