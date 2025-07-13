"""
find the longest substring with k distinct character

string = acccpbbebi, k = 3

Input => 'acccpbbebi'
Output => 'pbbeb' , length = 5

distinct character = {
    what character: character count
    c: 3,
    p: 1,
    b: 2
}

number of distinct character = 4 (number of keys in dictionary / character tracker)

condition => ( no of distinct character <= k distinct character, k = 3 )

longest substring length = 5

Naive Solution:

Initialize the long_substring_length = (-inf)
for each character in string:
    for each character in substring:
        add first character to substring
        if there are distinct characters greater than k distinct characters:
            end the sub loop and move to next iteration or break
        else:
            update the long_substring_len
            
Optimal Solution:

Start with initialization of longest_substring_len
Initialize the window start = 0
Initialize the window end  = 0
Initialize the character_tracker = {}
update the character in character_tracker
    if the character is in character_tracker then update the character count by 1
    else add the character to tracker and initialize the count to 1
if number of distinct characters in window is greater than k distinct characters:
    deduct the character count by 1
    if the character count is equal to zero then remove the character from char_tracker
    shrink the window
else:
    expand the window
    update the longest_str_len
"""

"""
Note : When we optimze, we shrink window

shrink represents moving to next iteration of outer loop when we use two loops, 
for each loop we generate all possible substrings starting from the character present at that index
so when we optimize or shrink window, we are rejecting all the substring generated starting with leftmost character and move to next character or outer loop iteration
expansion means the inner loop iteration
shrinking means the outer loop iteration

so we do two loop work in single loop by expanding and shrinking
"""

def long_substring_k_distinct_naive(string_arr, k):
    long_substring_len = float("-inf")
    for i in range(0, len(string_arr)):
        window_str = ""
        char_tracker = {}
        for j in range(i, len(string_arr)):
            window_str += f"{string_arr[j]}"
            if(string_arr[j] in char_tracker):
                char_tracker[string_arr[j]] += 1
            else:
                char_tracker[string_arr[j]] = 1
            
            if(len(char_tracker) > k):
                break
            else:
                len_window_substring = len(window_str)
                long_substring_len = max(long_substring_len, len_window_substring)
    return {
        "longest length": long_substring_len,
        }

def long_substring_k_distinct_opt(string_arr, k):
    longest_substring_len = float("-inf")
    window_start = 0
    char_tracker = {}
    
    for window_end in range(0, len(string_arr)):
        
        if(string_arr[window_end] in char_tracker):
            char_tracker[string_arr[window_end]] += 1
        else:
            char_tracker[string_arr[window_end]] = 1    
        
        if(len(char_tracker) > k):
            char_tracker[string_arr[window_start]] -= 1
            if(char_tracker[string_arr[window_start]] == 0):
                char_tracker.pop(string_arr[window_start])
            window_start += 1
        else: 
            substring_len = window_end - window_start + 1
            longest_substring_len = max(longest_substring_len, substring_len)
    
    return longest_substring_len

print(long_substring_k_distinct_opt("acccpbbebi",3))