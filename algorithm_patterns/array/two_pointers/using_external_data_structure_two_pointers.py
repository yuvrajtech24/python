"""
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

### Test Cases

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

    [2,] => 7
    [2,11] => 13
    [2,15] => 17
    [7,11] => 18
    [7,15] => 22

### Naive solution:

start with initializing indices list with empty list
start the outer loop
for each iteration of outer loop:
    initialize the current number
    start the innner loop
    for each iteration of inner loop:
        update current sum by adding current and next number
        if current sum is equal to target:
            then update indices list
        else:
            move to next iteration of inner loop
return the indices list2
        
### Optimal solution

start by initializing dictionary for each element as key and its index as value
start outer loop
for each number in outer loop
    initialize the current_comp to zero
    calculate complement for current number 
    if current number's complement exist in hashmap:
        To avoid same number twice, check current number ans its complements index:
            if equal then skip the current iteration and move to next number
        then return the indices of the current element and its complement from dictionary
    else
        iterate to next number
"""
def two_sum_naive(nums, target):
    indices_list = []
    for i in range(0, len(nums) - 1):
        current_sum = 0
        for j in range(i + 1, len(nums)):
            current_sum = nums[i] + nums[j]
            if current_sum == target:
                indices_list.append(i)
                indices_list.append(j)
    return indices_list

def two_sum_optimal(nums, target):
    complement_lookup = {}
    for i in range(0, len(nums)):
        complement_lookup[nums[i]] = i
        
    for i in range(0, len(nums)):
        current_comp = 0
        current_comp = target - nums[i]
        if(current_comp in complement_lookup):
            if(current_comp == nums[i]):
                continue
            return [i, complement_lookup[current_comp]]

# Test Casess
print(two_sum_naive([2,7,11,15], 9))

print(two_sum_naive([3,2,4], 6))

print(two_sum_naive([3,3], 6))