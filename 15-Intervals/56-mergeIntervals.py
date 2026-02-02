# FOLLOW UP TO INSERT INTERVALS(57 - Leetcode)
# Same logic as insert intervals but remember, intervals is not sorted here
# So, sort it first. Have a result array, add the first element and check last element in result with intervals[i]
# and apply cases from insert intervals, if overlap, pop it and merge then insert. if no overlap, just insert intervals[i]
# Remember, always use result[-1] when comparing
# Alternatively, you can use a heap here instead of sorting
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        result = []
        if intervals == []:
            return []
        sorted_intervals = sorted(intervals, key = lambda interval : interval[0])
        result.append(sorted_intervals[0])
        for i in range(1,len(sorted_intervals)):
            if result[-1][1] < sorted_intervals[i][0]:
                result.append(sorted_intervals[i])
            elif result[-1][0] <= sorted_intervals[i][1] and result[-1][1] >= sorted_intervals[i][0]:
                interval = result.pop()
                new_interval = [min(interval[0], sorted_intervals[i][0]), max(interval[1], sorted_intervals[i][1])]
                result.append(new_interval)
        return result
               
# Test cases
if __name__ == "__main__":
    s = Solution()
    test_cases = [
        ([[1,3], [2,6], [8,10], [15,18]], [[1,6], [8,10], [15,18]]),
        ([[1,4], [4,5]], [[1,5]]),
        ([[1,3], [5,7], [8,10]], [[1,3], [5,7], [8,10]]),  # No overlap
        ([[1,10], [2,3], [4,5], [6,7]], [[1,10]]),  # Nested intervals
        ([[5,10], [1,4], [6,8]], [[1,4], [5,10]]),
        ([[1,4]], [[1,4]]),  # Single interval
        ([], []),  # Empty input
    ]

    for i, (intervals, expected) in enumerate(test_cases, 1):
        result = s.merge(intervals)
        print(f"Test {i}: {'Pass' if result == expected else 'Fail'} - Output: {result}")          
            