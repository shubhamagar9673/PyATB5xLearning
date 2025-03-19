#to find out missing key

dict1 = {"a" : 1, "b" : 2, "c":3}
dict2 = {"a" : 1, "b" : 2}

missing_key =set(dict1.keys())-set(dict2.keys())
print(missing_key)



#sort a dict by its values in ascending

dict1 = {"a" : 3, "b" : 2, "c":1}