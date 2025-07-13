"""
643. Maximum Average Subarray I

Test Cases

Input => nums = [1,12,-5,-6,50,3], k = 4
Output => max_avg = 12.75

i = 0, sub_arr = [1,12,-5,-6], avg = 0.5
i = 1, sub_arr = [12,-5,-6,50], avg = 12.75
i = 2, sub_arr = [-5,-6,50,3], avg = 10.5

Naive Solution

start with max_avg = float("-inf")
for each item in the list, until length of array minus window size:
    Initialize the window sum to zero
    for each item in sub list, until item index is less than k:
        add the current element to window sum
    calculate the average for current window sum
    update the max avg

Time Complexity => O(n^2)
Space Complexity => O(1)    

Optimize Solution

start with max_avg = float("-inf")
initialize window_start to 0 index
initialize window_end to k-1
initialize window_sum to 0
for each item in list, until item is less than k:
    add each element to window_sum

for each item in list:
    calcualte the window_avg
    update the max_avg
    remove the left element from window_sum
    increment window_start
    increment window_end
    add new element from right to window_sum
    
Time Complexity => O(n)
Space Complexity => O(1)

return max_avg
"""

def max_avg_subarray_naive(nums, k):
    max_avg = float("-inf")
    for i in range(0, len(nums)-k+1):
        window_sum = 0
        for j in range(i, i+k):
            window_sum += nums[j]
        window_avg = window_sum / k
        max_avg = max(max_avg, window_avg)
        
    return max_avg

def max_avg_subarray_opt(nums, k):
    max_avg = float("-inf")
    window_start = 0
    window_end = k - 1
    window_sum = 0
    for i in range(0, k):
        window_sum += nums[i]
        
    for i in range(0, len(nums)-k+1):
        window_avg = window_sum / k
        max_avg = max(max_avg, window_avg)
        if window_end + 1 < len(nums):  # need explanation
            window_sum -= nums[window_start]
            window_start += 1
            window_end += 1
            window_sum += nums[window_end] # need explanation, goes out of bond if line 68 removed
    # do something
    return max_avg        

print(max_avg_subarray_opt([1,12,-5,-6,50,3],4))
print(max_avg_subarray_opt([5], 1))