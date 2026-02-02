class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        intervals = sorted(intervals, key = lambda intervals: intervals[0])
        if intervals == []:
            return True
        current_interval = [intervals[0][0],intervals[0][1]]

        for i in range(1, len(intervals)):
            if current_interval[1] > intervals[i][0] and current_interval[0] < intervals[i][1]:
                return False
            elif current_interval[1] <= intervals[i][0]:
                current_interval[1] = intervals[i][1]
                current_interval[0] = intervals[i][0]
        return True

if __name__ == "__main__":
    s = Solution()
    print(s.canAttendMeetings([[0,30],[5,10],[15,20]]))
    print(s.canAttendMeetings([[7,10],[2,4]]))