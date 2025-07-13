# set data structure
set_list1 = {57, 99, 23, 9, 66, 77}
set_list2 = {23, 34, 56, 66,9, 101, 203}
print(set_list1)

# add element to set
set_list1.add(103)
print(set_list1)

# remove element from set
set_list1.remove(99)
print(set_list1)

# set operations - union
union_set = set_list1.union(set_list2)
print(union_set)

# set operations - intersection
intersection_set = set_list1.intersection(set_list2)
print(intersection_set)

# set operations - difference
difference_set1 = set_list1.difference(set_list2)
print(difference_set1)

# subset check
print(set_list1.issubset(set_list2))

# superset check
print(set_list1.issuperset(set_list2))