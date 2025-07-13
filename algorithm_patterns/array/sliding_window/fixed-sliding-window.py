"""
s,e
[1,2,3,4,5]
 s   e

[1,2,3]             => sum = 6, avg = 2 
    [2,3,4]         => sum = 9, avg = 3
        [3,4,5]     => sum = 12,avg = 4
        
Naive Solution
        
for each item in list, until item is less than length of array minus k
        for each item in sublist, until item is less than k 
            add the current item to running sum
        then divide the runnning sum by number of elments in sublist to get avg
        add calculated avg to avg_arr list        
        
Time Complexity = O(N*K)
Space Complexity = O(1)

Optimal Solution

represent window by creating window start and end variables
    initialize window sum
    Initiate start pointer at 0 index and end pointer at k-1 index
    calculate initial window sum by iterating over window start to end index
    calculate the window avg by dividing window sum by k and push to avg array
    for each element in list
        deduct window start element from window sum
        increment the window start
        increment the window end
        add the window end element to the window sum
        calculate the avg by dividing the window sum by k and push to avg array
    
"""

def avg_sub_array_naive(arr,k):
    avg_arr = []
    for i in range(0,len(arr)-k+1,1):
        sum = 0
        avg = 0

        for j in range(0,k,1):
            sum = sum + arr[i+j]
        avg = sum / k
        print(f"index {i}, sum = {sum}")
        print(f"index {i}, avg = {avg}")
        avg_arr.append(avg)
    
    return avg_arr

def avg_sub_array_optimal(arr, k):
    avg_arr = []
    window_sum = 0
    window_start = 0
    window_end = 0
    window_start = 0
    window_end = k-1
    
    for i in range(window_start, window_end, 1):
        window_sum = window_sum + arr[i]
        avg_arr.append(window_sum / k)
    
    for i in range(1, len(arr)-1,1):
        window_sum = window_sum - arr[window_start]
        window_start += 1
        window_end += 1
        window_sum += arr[window_end]
        avg_arr.append(window_sum / k)

    return avg_arr

# Test Cases
print(avg_sub_array_naive([1,2,3,4,5],3))
# Output - [2,3,4]

