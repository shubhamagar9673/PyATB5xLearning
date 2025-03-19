# Dictionary from two lists


keys = ["name", "role", "experience"]
Values = ["shubham", "SDET", "4"]

my_dict = dict(zip(keys, Values))
print(my_dict)

# merge two dictionaries

dict1 = {"a" : 1, "b" : 2}
dict2 = {"c" : 1, "d" : 2}

merged_dict  = dict1 | dict2
print(merged_dict)
print(merged_dict.get("a"))