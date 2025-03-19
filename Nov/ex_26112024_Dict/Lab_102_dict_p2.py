Student_info = {
    "name": "Shubham",
    # "age":"65",
    "age": "67",
    "address": "MH",

}

print(Student_info["name"])
print(Student_info["age"])
print(Student_info["address"])
Student_info["age"]=100
print(Student_info)

Student_info2 = dict(name="Pramod",age=67,address="MH")
print(Student_info2)

Student_info3 = {
    "name": "Shubham",
    # "age":"65",
    "age": "67",
    "address": {
        "Home_address":"MH",
         "OfficeAddress":"ND"
    }

}

print(Student_info3)
