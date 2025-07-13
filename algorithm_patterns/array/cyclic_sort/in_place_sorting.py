"""
1) What is Cyclic Sort?

    Cyclic Sort is an in-place sorting algorithm. With linear time complexity and constant space complexity.

2) When to Use Cyclic Sort?

    The array size is n. Range should be less than n always.
    The elements of array fall within a fixed range, e.g. (1 to n), (0 to n-1), etc.
    The elements are distinct, although variations exist for duplicates or missing numbers.
    Works well with index manipulation.
    Often combined with math tricks or cycle detection.
    
    arr size n = 6
    arr = [2,6,4,3,1,5] 
    range = [1,6] or [1,n]
    index = value - 1

3) Core Idea (for 0 to n-1):

    The Cyclic Sort algorithm works by placing each number at its correct index
    The value of element should equal its position or index.
    The Cyclic Sort pattern iterates over the array one number at a time, and if the current number you are iterating is not at the correct index, you swap it with the number at its correct index.
    If current element and its index are not equal, swap it until it becomes equal (unless there's a conflict, then it's a duplicate).
    All three of these problems rely on placing numbers at the right index.

4) Time Complexity: O(n)

5) Space Complexity: O(1) (in-place)

6) Pattern Variations

✅ Variation 1. In-Place Sorting using Cyclic Sort (1 to n)

    Goal: 
    Sort an array of n numbers from (1 to n) without extra space.
    
    🧠 Key Idea: 
    Each number knows where it should go, (value = index + 1). Keep moving it there.
    
    🔍 Plain English Algorithm:

    1) Start at the beginning of the array.
    2) For each number:
        2.1) Calculate its correct index as num - 1.
        2.2) If the number is not at its correct index:
            2.2.1) Swap it with the number at that correct index.
        2.3) Else:
            2.3.1) Move to the next number.
    3) Keep repeating until the entire array is sorted.


✅ Variation 2. Missing Number (from 0 to n)

    Goal: One number from 0 to n is missing.
    
    🧠 Key Idea: Put every number at the index equal to its value.
    
    🔍 Plain English Algorithm:
    
    1) Loop through each number in the array.
    2) If the number is within the array range (< len(nums)) and not in its correct index 
        swap it with the number at correct index.
    3) After sorting is done, loop through the array again.
    4) The first index where the value doesn’t match the index is the missing number.
    5) If all match, then the missing number is n.

✅ Variation 3. Find the Duplicate Number (from 1 to n)

    Goal: One number is repeated. Find it.
    
    🧠 Key Idea: Duplicate causes conflict during placement, so you catch it when the target spot already has the same value.
    
    🔍 Plain English Algorithm:

    1) Loop through the array.
    2) For each number:
        2.1) If it is not at its correct index (i.e., value v should be at index v-1):
            2.1.1) Check if it’s already at its correct index:
                2.1.1.1) If yes → we found the duplicate → return it.
                2.1.1.2) If no → swap it to its correct index.
    3) If loop finishes and no duplicate found (unlikely in valid input), return -1.

7) 🎓 Final Thought

    Think of the array as a hash map, where index = key and value = actual number. satisfy condition (key = value). That is index and key value should be same.
"""

def cyclic_sort(arr):
    
    """
     0 1 2 3 4
    [3,5,1,4,2] i = 0
    [1,5,3,4,2] i = 0
    [1,2,3,4,5] i = 1
    
    start at the begining of the array
    for each number
        calcualte its correct position (index = value - 1)
        check if current element is at its correct position (the current position is equal to correct position) 
            if yes then move to next number
        else
            swap the current element with element at correct position
    """
    
    for i in range(0,len(arr)):
        correct_position = arr[i] - 1
        if(i == correct_position):
            continue
        else:
            arr[i], arr[correct_position] = arr[correct_position], arr[i] 
    
    return arr

# print(cyclic_sort([3,5,1,4,2])) # [1,2,3,4,5]
# print(cyclic_sort([1, 2, 3, 4, 5])) # [1,2,3,4,5]
# print(cyclic_sort([5, 4, 3, 2, 1])) # [1,2,3,4,5]
# print(cyclic_sort([3, 1, 5, 4, 2])) # [1, 2, 3, 4, 5]
# print(cyclic_sort([1])) # [1]
# print(cyclic_sort([2, 1])) # [1,2]
# print(cyclic_sort([3, 0, 1, 2])) # [0, 1, 2, 3] 

def cyclic_sort_missing(arr):
    missing_value = 0
    
    # do something
    """
    start with first element
    cyclic sort the array 
        for each element
            calculate its correct position
            if number is not at its correct position
                swap the number with element at correct position
            else
                move to next number
                
    for each element
        if number not equal to its index than its missing number 
            return the index
        else 
            move to next number 
            
     0,1,2
    [3,0,1]
    
    value = index
    """
    
    # cyclic sort
    for i in range(0, len(arr)):
        
        if(arr[i] >= len(arr)):
            continue
        
        correct_position = arr[i]
        if(i != correct_position):
            arr[i], arr[correct_position] = arr[correct_position], arr[i]
        else:
            continue
    
    for i in range(0, len(arr)):
        if(arr[i] != i):
            return i
        else:
            continue
        
    return missing_value

# print(cyclic_sort_missing([3, 0, 1])) # 2
# print(cyclic_sort_missing([4, 2, 1, 0])) # 3
# print(cyclic_sort_missing([1])) # 0
# print(cyclic_sort_missing([0])) # 1 - error
# print(cyclic_sort_missing([])) # 0
# print(cyclic_sort_missing([0, 1, 2, 4, 5])) # 3

def cyclic_sort_duplicate(arr): 
    """
    start with first element of array
    for each element
        calculate correct index of current element
        if current number is not at its correct index
            check if current number is already available at correct index
                return that duplicate value
            if not available
                then swap the current number with number at correct index
    return -1
    """
    i = 0
    while(i < len(arr)):
        correct_position = arr[i] - 1 
        if(i != correct_position):
            if(arr[i] == arr[correct_position]):
                return arr[i]
            else:
                arr[i],arr[correct_position] = arr[correct_position], arr[i]
        else:
            i += 1
    return -1

# n = 4
# range(1,4)
# index = value - 1

#                            0,1,2,3
# print(cyclic_sort_duplicate([3,2,3,1]))    # 3
# print(cyclic_sort_duplicate([3,4,2,7,8,2,1,3])) # 3
# print(cyclic_sort_duplicate([1,3,4,2,2])) # 2
