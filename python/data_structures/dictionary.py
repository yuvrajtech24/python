# dictionary structure
students = {
    "stu1": "ram",
    "stu2": "sham",
    "stu3": "helen" 
}
# get key
print(students["stu3"])

# add key
students["stu4"] = "rekha"
# print(students)

# update key
students["stu2"] = "sita"
# print(students)

# remove element
del students["stu1"]
# print(students)

# list of keys
print(students.keys())

# list of values
print(students.values())

# copy dictionary
passed_students = students.copy()
print("passed students => ", passed_students)