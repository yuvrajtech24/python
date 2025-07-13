""" 
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

nums = [2,3,1,2,4,3] 
target =  7 
min_len_sub_arr = ?

Approach

[2]           =>  2 < 7
[2,3]         =>  5 < 7
[2,3,1]       =>  6 < 7
[2,3,1,2]     =>  8 > 7
update the min_len_sub_arr = 4

[3]           =>  3 < 7 
[3,1]         =>  4 < 7
[3,1,2]       =>  6 < 7
[3,1,2,4]     =>  10 > 7
update the min_len_sub_arr = 4

[1]         =>  1 < 7
[1,2]       =>  3 < 7
[1,2,4]     =>  7 == 7
update the min_len_sub_arr = 3

[2]         =>  2 < 7
[2,4]       =>  6 < 7
[2,4,3]     =>  9 > 7
update the min_len_sub_arr = 3

[4]         =>  4 < 7
[4,3]       =>  7 == 7
update the min_len_sub_arr = 2
return 

Naive Solution

initialize the min length of sub array to infinite
  for each item in the list
    initialize sum of sub array to zero
    for each item in the sub list
      add current element to sum of sub array
      if sum is greater than equal to target
        then update minimum length
        break from loop
  return the minimum length of sub array
  
Optimal Solution


""" 

def min_sum_sub_arr_naive(arr, target):
  min_len = float('inf')
  
  for i in range(0, len(arr)):
    current_sum = 0
    for j in range(i, len(arr)):
      current_sum += arr[j]
      if(current_sum >= target):
        min_len = min(min_len,j-i+1)
        break
  
  return 0 if min_len == float("inf") else min_len

def min_sum_sub_arr_opt(arr, target):
  min_length = float("inf")
  
  return min_length

# Test Cases

# target = 7, nums = [2,3,1,2,4,3], output = 2
print(f"min length 1 = {min_sum_sub_arr_naive([2,3,1,2,4,3], 7)}")

# target = 4, nums = [1,4,4], output = 1
print(f"min length 2 = {min_sum_sub_arr_naive([1,4,4], 4)}")

# target = 11, nums = [1,1,1,1,1,1,1], output = 0
print(f"min length 3 = {min_sum_sub_arr_naive([1,1,1,1,1,1,1], 11)}")