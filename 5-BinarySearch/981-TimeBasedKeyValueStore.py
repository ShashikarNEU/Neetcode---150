# everything will be inserted acc to timestamp
# we can't insert 5 after inserting 10. so, the timestamps will be automatically sorted
# To fetch them, do binary search on the timestamps, feeling doubtful when to return timestamps? don't be
# Read question. it's given if timestamp_prev <= timestamp(given). then return that value of timestamp_prev
# so, in binary search when value <= target. low=middle+1, record middle then
# and return that middle after binary search
from collections import defaultdict
class TimeMap:
    def __init__(self):
        self.hashTable = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashTable[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        val_time_list = self.hashTable[key]

        low = 0
        high = len(val_time_list)-1
        res = ""

        while low <= high:
            middle = (low+high)//2

            if val_time_list[middle][1] > timestamp:
                high = middle - 1
            elif val_time_list[middle][1] <= timestamp:
                res = val_time_list[middle][0]
                low = middle + 1
        
        return res

# Other Attempt
class TimeMap:
    def __init__(self):
        self.hashMap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashMap[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        nums = self.hashMap[key]
        start = 0
        end = len(nums)-1
        res = ""

        # if the length = 1 and it satisfies the codn[EDGE CASE]
        if len(nums) == 1 and nums[0][0] <= timestamp:
            return nums[0][1]

        while start <= end:
            middle = (start+end)//2
            if nums[middle][0] <= timestamp:
                start = middle + 1 
                res = middle
            elif nums[middle][0] > timestamp:
                end = middle - 1
        
        return nums[res][1] if res != "" else ""


    