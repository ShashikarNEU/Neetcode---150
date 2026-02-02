# https://neetcode.io/solutions/insert-interval [WATCH THIS FIRST!!]
# Basic Logic for intervals insertion
# iterate the intervals array, don't look at it from multiple intervals, what to do
# consider one interval and see if the new interval lesser than interval[i], greater than the new interval or overlap
# if new interval is less return new interval + intervals array from that index
# if new interval is greater, add interval of that index to the result since it's less
# if overlap happens, merge it min(intervals[i] - start, newInterval start), max(intervals[i] - end, newInterval end)
# After merging it, don't append it to result, it can also overlap with next intervals[i], just assign it to newInterval = mergedInterval [IMP -- READ HERE]
# overlap will happen even if intervals[i] is fully within new interval but ans will be same new interval

class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = []
        for i in range(len(intervals)):
            # Case 1: when new interval end < interval[i](start), return new interval + intervals array from i
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]
            # Case 2: when new interval start > interval[i], then add interval[i] to result
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
            # Case 3: Overlap happens -> Opp codn of case 1 and 2 combined [Draw diagram and think], you can use else here(Easier)
            elif newInterval[1] >= intervals[i][0] and newInterval[0] <= intervals[i][1]:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]

        # Almost all cases, case 1 will return the answer but if it reaches the end, new interval won't be added to the array
        # so, add it in that case 
        result.append(newInterval)

        return result
    
# Use else for Case 3(Overlap) - Easier
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = []
        for i in range(len(intervals)):
            # Case 1: when new interval end < interval[i](start), return new interval + intervals array from i
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]
            # Case 2: when new interval start > interval[i], then add interval[i] to result
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
            # Case 3: Overlap happens -> Opp codn of case 1 and 2 combined [Draw diagram and think], you can use else here(Easier)
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]

        # Almost all cases, case 1 will return the answer but if it reaches the end, new interval won't be added to the array
        # so, add it in that case 
        result.append(newInterval)

        return result