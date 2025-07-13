"""
209. Minimum Size Subarray Sum

Test Case
Input, nums = [2,3,1,2,4,3] target = 7
Output, 2

[2] => sum = 2 < 7
[2,3] => sum = 5 < 7
[2,3,1] => sum = 6 < 7
[2,3,1,2] => sum = 8 >= 7
update the min length = 4
break the inner loop
[3] => sum = 3 < 7
[3,1] => sum = 4 < 7
[3,1,2] => sum = 6 < 7
[3,1,2,4] => sum = 10 >= 7
update the min length = 4
break the inner loop
...

Naive solution

Start with min_length = Infinity
for each item in the list:
    initiate the window_sum = 0
    for each item in the sub list:
        add the current element to the window_sum
        if window_sum is greater than equal to target:
            update min_length
            break out of loop
            
Time Complexity = O(n^2)
Space Complexity = O(n)

Optimal solution

start with initializing min_length to infinity
initialize the window_start to zero index of list
initialize the window_end to zero index of list
initialize window_sum to element at window_start
for each item in the list:
    if window_sum is greater than equal to target:
        update the min_length
        then optimize by shrinking window, remove window_start item from window sum
        update the window_start
    else:
        expand window by update the window_end
        add window end item to window_sum
        
return the min_length

Time Complexity = O(n)
Space Complexity = O(1)

"""

def min_subarray_sum_naive(nums, target):
    min_length = float("inf")
    for i in range(0, len(nums)):
        window_sum = 0
        for j in range(i, len(nums)):
            window_sum += nums[j]
            if(window_sum >= target):
                # print(f"i = {i}, j = {j}, window sum = {window_sum}")
                min_length = min(min_length, j-i+1)
                break
    return 0 if min_length == float('inf') else min_length

def min_subarray_sum_opt(nums, target):
    min_length = float("inf")
    window_start = 0
    window_end = 0
    window_sum = nums[window_start]
    while(window_end < len(nums)):
        if(window_sum >= target):
            min_length = min(min_length, window_end-window_start+1)
            window_sum -= nums[window_start]
            window_start += 1
        else:
            window_end += 1
            if(window_end >= len(nums)):
                break
            window_sum += nums[window_end]

    return 0 if min_length == float('inf') else min_length

print(min_subarray_sum_opt([2,3,1,2,4,3], 7))
print(min_subarray_sum_opt([1,4,4], 4))
print(min_subarray_sum_opt([1,1,1,1,1,1,1,1], 11))