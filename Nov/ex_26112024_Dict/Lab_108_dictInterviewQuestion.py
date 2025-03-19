# function that returns a maximum value from a dictionary
# {"a":10,"b":10,"c":30}

def max_Value_in_dictionary(dictionary):
    #return max(dictionary.values())
    return min(dictionary.values())


print(max_Value_in_dictionary({"a": 10, "b": 10, "c": 30}))
