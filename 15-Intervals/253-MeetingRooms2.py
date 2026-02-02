# Easy if you know the min heap pattern(Two pointers of that version, code is 90% same)
# LC 194 Car Pooling(min heap pattern, refer that first)
# Two Pointer Appoarch
# Logic (https://neetcode.io/solutions/meeting-rooms-ii)
# Refer video and draw diagram. this explantion will be diffcult to understand on only reading
# idea here is to find the max no of meetings going on at a particular of time
# so to do this, have p1 and p2 pointers, iterate with p1 as base(similar to sliding window pattern), if you encounter
# end time < start, count-=1 while (what if there are multiple ends less than that start)
# when p1 reaches the start's last index, it's over.
# here, count refers to the number of rooms at a particular point in time.
# max count is the answer
class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        start_times = []
        end_times = []

        for start, end in intervals:
            start_times.append(start)
            end_times.append(end)
        
        start_times.sort()
        end_times.sort()

        currentRooms = 0
        maxRooms = float('-inf')
        p1 = 0
        p2 = 0

        while p1 < len(start_times):
            currentRooms+=1

            while p2 < len(end_times) and end_times[p2] <= start_times[p1]:
                currentRooms-=1
                p2+=1
            
            maxRooms = max(maxRooms, currentRooms)
            p1+=1
        
        return maxRooms

# CAN BE SOLVED USING MIN HEAP ALSO
# PLS CHECK THE HEAP SECTION

if __name__ == "__main__":
    s = Solution()
    print(s.minMeetingRooms([[0,30],[5,10],[15,20]]))
    print(s.minMeetingRooms([[7,10],[2,4]]))