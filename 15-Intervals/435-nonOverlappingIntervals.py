# FOLLOW UP TO MERGE INTERVALS - Leetcode 56
# Instead of using result array, we can use current_interval = [start, end] since we don't need the result array and keep updating start,end when no overlap happens
# When overlap happens, update min(end, prevEnd) and corr start to current interval([IMP] -> Remove the larger end interval as it can overlap more easily)

# When overlap, why take min and not take the first one interval?
# Think about this case -> [[1,100], [11,22], [23,34], [35,46]]

# easier way -> no need to write overlap codn and use else
# Same logic as above but we use only end here. no need to store start here
# We only want the prevEnd and End in case of overlap. when no overlap, end < intervals[i][0] -> update end = interva;s[i][1]

class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if intervals == []:
            return 0
        # Sort it acc to start value in asc order
        sorted_intervals = sorted(intervals, key = lambda interval : interval[0])

        #result = []
        
        count = 0
        current_interval = [sorted_intervals[0][0], sorted_intervals[0][1]]
        #result.append(sorted_intervals[0])

        for i in range(1,len(sorted_intervals)):
            if current_interval[1] <= sorted_intervals[i][0]:
                current_interval[0] = sorted_intervals[i][0]
                current_interval[1] = sorted_intervals[i][1]
                #result.append(sorted_intervals[i])
            elif current_interval[1] > sorted_intervals[i][0] and current_interval[0] < sorted_intervals[i][1]:
                count+=1
                current_interval[1] = min(current_interval[1], sorted_intervals[i][1])
                if current_interval[1] == sorted_intervals[i][1]:
                    current_interval[0] = sorted_intervals[i][0]

        return count

class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if intervals == []:
            return 0
        # Sort it acc to start value in asc order
        sorted_intervals = sorted(intervals, key = lambda interval : interval[0])

        count = 0
        prev_end = sorted_intervals[0][1]

        for i in range(1,len(sorted_intervals)):
            if prev_end <= sorted_intervals[i][0]:
                prev_end = sorted_intervals[i][1]
            else:
                count+=1
                prev_end = min(prev_end, sorted_intervals[i][1])
                
        return count

# Consider only the last index(new_interval[1]) as the first index does not matter here
# result arr does not matter, so, don't give imp to start point(consider only the end point)
class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        count = 0
        intervals.sort(key = lambda interval: interval[0])
        current_interval = intervals[0]

        for i in range(1, len(intervals)):
            if current_interval[1] <= intervals[i][0]:
                current_interval = intervals[i]
            elif current_interval[1] > intervals[i][0]:
                current_interval[1] = min(intervals[i][1], current_interval[1])
                count+=1
        
        return count

if __name__ == "__main__":
    s = Solution()
    # Test cases
    test_cases = [
        ([], 0),
        ([[1,2]], 0),
        ([[1,2], [2,3], [3,4]], 0),
        ([[1,3], [2,4], [3,5]], 1),
        ([[1,2], [1,3], [2,3]], 1),
        ([[1,5], [2,3], [3,4], [4,6]], 1),
        ([[1,10], [2,3], [3,4], [5,6], [7,8]], 1),
        ([[1,100], [11,22], [23,34], [35,46]], 1),
    ]

    for intervals, expected in test_cases:
        print(f"Input: {intervals} | Expected: {expected} | Output: ", end="")
        print(s.eraseOverlapIntervals(intervals))
                
                
            