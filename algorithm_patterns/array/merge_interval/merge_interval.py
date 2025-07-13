"""
1) What is Merge Interval?

    The Merge Interval pattern deals with solving problems where you're given a collection of intervals (typically as [start, end] pairs), and you need to merge overlapping intervals into non-overlapping ones or perform operations like insertion, finding overlaps, or removing intervals.

    A classic example:
    Given [[1,3], [2,6], [8,10], [15,18]], return [[1,6], [8,10], [15,18]].

2) When to Use Merge Interval?

    You're working with ranges, time periods, meetings, memory blocks, etc.

    The problem involves overlapping intervals.

    You need to merge, insert, remove, or find gaps/overlaps between intervals.

    The input is a list of intervals and the solution needs sorted or merged representation.

    Common keywords: "interval", "range", "merge", "overlap", "insert", "non-overlapping", "schedule", "timeline".

3) Core Idea

    Sort the intervals by the start time.

    Initialize a result list (stack-like behavior).

    Iterate through each interval:

        If it overlaps with the last one in the result → merge them.

        Otherwise, just add it as-is.

    🔁 Merge condition:
    if current[0] <= last[1] → merge

    🧠 Merge logic:
    last[1] = max(last[1], current[1])

4) Time Complexity

    O(n log n): Due to sorting the intervals.

    Merging is O(n) since we iterate once.

➡️ Total: O(n log n)

5) Space Complexity

    O(n) in the worst case if all intervals are non-overlapping (result holds all).

    O(1) extra space if in-place modification is allowed (but depends on language/constraints).

6) Pattern Variations or Types

🟩 1. Merge Overlapping Intervals

Problem Type (Variation Name): 
Merge Overlapping Intervals

Description:
Given a list of intervals, merge all overlapping ones and return a list of non-overlapping intervals.

Example Leetcode Problems: 
56) Merge Intervals

Goal:
Return a list where all overlapping intervals are merged.

🧠 Key Idea:
Sort by start time, then merge overlapping intervals using a result list.

🔍 Plain English Algorithm:

    Sort intervals by start time.

    Initialize an empty result list.

    For each interval:

        If the result is empty or the current interval doesn't overlap, append it.

        If it overlaps with the last interval, merge them by updating the end time.

    Return the result list.

🟩 2. Insert and Merge Interval

Problem Type (Variation Name):
Insert and Merge

Description:
Given a sorted list of non-overlapping intervals and a new interval, insert and merge it into the list.

Example Leetcode Problems:

    57. Insert Interval

Goal:
Insert a new interval and merge if necessary, maintaining order and non-overlap.

🧠 Key Idea:
Add all intervals before the new one, merge overlaps, then add remaining.

🔍 Plain English Algorithm:

    Initialize result list.

    Add all intervals that end before new interval’s start.

    Merge overlapping intervals with the new one.

    Add all intervals that come after the merged new interval.

    Return the result list.

🟩 3. Remove Interval

Problem Type (Variation Name):
Remove Interval

Description:
Remove a given interval from a list of intervals, possibly splitting intervals if partially overlapped.

Example Leetcode Problems:

    1272. Remove Interval

Goal:
Return list after removing (subtracting) the given interval from each.

🧠 Key Idea:
Check overlap and slice existing intervals accordingly.

🔍 Plain English Algorithm:

    For each interval:

        If no overlap with the removal interval, keep as is.

        If it overlaps:

            Keep left part if any: [start, removal_start)

            Keep right part if any: (removal_end, end]

    Return the updated list.

🟩 4. Interval Intersection

Problem Type (Variation Name):
Interval Intersection

Description:
Find intersections (overlaps) between two lists of intervals.

Example Leetcode Problems:

    986. Interval List Intersections

Goal:
Return a list of intervals representing all intersections between two lists.

🧠 Key Idea:
Use two pointers to compare intervals from each list and find overlapping parts.

🔍 Plain English Algorithm:

    Use two pointers, one for each list.

    For overlapping intervals, add the intersection [max(start1, start2), min(end1, end2)].

    Move the pointer with the smaller end time forward.

    Repeat until one list ends.

🟩 5. Minimum Meeting Rooms

Problem Type (Variation Name):
Meeting Room Counter

Description:
Given meeting time intervals, find the minimum number of rooms required.

Example Leetcode Problems:

    253. Meeting Rooms II

Goal:
Determine the max number of overlapping intervals (rooms needed).

🧠 Key Idea:
Use a min-heap to track ongoing meetings by end time.

🔍 Plain English Algorithm:

    Sort intervals by start time.

    Use a min-heap to store end times of ongoing meetings.

    For each interval:

        Remove meetings that ended (heap top < current start).

        Add current end time to heap.

    Return heap size as the number of rooms needed.

🟩 6. Can Attend All Meetings

Problem Type (Variation Name):
Non-Overlapping Check

Description:
Check if a person can attend all meetings (i.e., no overlaps).

Example Leetcode Problems:

    252. Meeting Rooms

Goal:
Return true if no intervals overlap.

🧠 Key Idea:
Sort and compare adjacent intervals.

🔍 Plain English Algorithm:

    Sort intervals by start time.

    For each pair of adjacent intervals:

        If start[i+1] < end[i], return false.

    Return true if no overlaps are found.

🟩 7. Employee Free Time

Problem Type (Variation Name):
Common Free Intervals

Description:
Find free time slots common to all employees from their schedule.

Example Leetcode Problems:

    759. Employee Free Time

Goal:
Return the intervals when all employees are free.

🧠 Key Idea:
Flatten and merge all busy intervals, then find gaps.

🔍 Plain English Algorithm:

    Flatten all employee schedules into one list.

    Sort and merge overlapping intervals (busy times).

    The gaps between merged intervals are the free times.

🟩 8. Find Gaps in Intervals

Problem Type (Variation Name):
Missing Ranges / Find Gaps

Description:
Find missing ranges or gaps not covered by any interval.

Example Leetcode Problems:

    163. Missing Ranges

Goal:
Return a list of ranges not covered within a given bound.

🧠 Key Idea:
Compare the end of one interval to the start of the next to find gaps.

🔍 Plain English Algorithm:

    Start from the lower bound.

    For each interval:

        If current start > previous end + 1 → gap exists.

        Update end pointer.

    Check gap between last end and upper bound.


"""