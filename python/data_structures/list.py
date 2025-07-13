# list structure
list = ["hi", "how", "are", "you"]
print(list)

# get single element from a list
print(list[1])

# get range of elements from a list
print(list[1:3])

# add element to a list
list.append(1)
print(list)

list.insert(0, 2)
print(list)

# remove element from a list
list.remove(2)
print(list)

# update element from a list
list[0] = "ola"
print(list)

# sort list
# list.sort()

# search list
result = list.index(1)
print(result)

# reverse 
list.reverse()
print(list)

# copy
list2 = list.copy()
print("list 2 = ", list2)

# count elements in list
list.append(1)
list.append(1)
print(list)
result = list.count(1)
print(result)