Student_info1 = {
    "name": "Pramod",
    # "age":"65",
    "age": "67",
    "address": {
        "Home_address":"ND",
         "OfficeAddress":"KA"
    }

}

Student_info2 = {
    "name": "Amit",
    # "age":"65",
    "age": "69",
    "address": {
        "Home_address":"GOA",
         "OfficeAddress":"KA"
    }

}

student_list=[Student_info1,Student_info2]
print(student_list)
print(student_list[0]["name"])
print(student_list[0]["age"])
print(student_list[0]["address"])
print(student_list[0]["address"]["OfficeAddress"])
print(student_list[1])
#print(student_list[2])  it will give us index out of bound
