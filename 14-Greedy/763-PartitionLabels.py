from collections import defaultdict

# Optimal Soln(Greedy)
# Form a hashTable with end occurences of letters
# Have a size=0 and end=-1 variable
# Go through every letter and find out if the last occurence is more than end and end == last occurence, add size to result
class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        # Form a hashTable with end occurences of letters
        hashMap = defaultdict(int)

        for i in range(len(s)):
            hashMap[s[i]] = i
        
        size = 0
        end = 0
        i = 0
        res = []

        end = -1

        # Go through every letter and find out if the last occurence is more than end and end == last occurence, add size to result
        while i < len(s):
            end = max(hashMap[s[i]], end)
            
            size += 1
            if i == end:
                res.append(size)
                size = 0
            i+=1
        
        return res

# Method #2- Use hashMap to find first,last occurence of every letter in the hashTable
# Take hashMap.Values()
# Sort them acc to starting values
# Do merge intervals of the whole list
# and return length of the merges

# I just did this due to merge intervals practice. For greedy, pls do optimal version above

class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        # Form a hashTable with first,last occurences of letters
        hashMap = {}
        for i, char in enumerate(s):
          if char not in hashMap:
              hashMap[char] = [i, i]
          else:
              hashMap[char][1] = i
        
        # 2. Get intervals AND SORT THEM by start time
        if not hashMap:
            return []
        
        intervals = list(hashMap.values())
        
        res = []

        current_interval = intervals[0]

        for i in range(1, len(intervals)):
            if current_interval[1] < intervals[i][0]:
                res.append(current_interval)
                current_interval = intervals[i]
            elif current_interval[1] >= intervals[i][0] and current_interval[0] <= intervals[i][1]:
                current_interval[0] = min(current_interval[0], intervals[i][0])
                current_interval[1] = max(current_interval[1], intervals[i][1])
        
        res.append(current_interval)
        ans = []
        for start, end in res:
            ans.append(end-start+1)
        
        return ans


                
        
            

            



        