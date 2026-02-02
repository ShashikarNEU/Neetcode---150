# [MED-HARD]
# Here we have to find the longest str of same character with k replacements
# No need replace with k, decrement it
# Have a window and a codn, increment it as along the condn is valid, if the codn fails
# increment p1 untill the codn passes
# Have a hashTable bw p1 and p2(When you increment p1, remove p1 item from hashmap)
# Do window length - max value from hash map = letters that have to be replaced
# if that value is less than <= k, then, the window is valid(Condition)

# Main Logic -> window size - max occurances char = rest of the charcaters, we are trying to convert rest of the char to max char so, rest of chars number should <= k. if > k, then we increment p1 and remove from hash map untill it becomes <=k. 

from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
       p1 = 0
       p2 = 0
       hashTable = {}
       window = 0
       max_window = 0
       while p2 < len(s):
          if s[p2] in hashTable:
             hashTable[s[p2]] += 1
          else:
             hashTable[s[p2]] = 1
            
          max_val = max(hashTable.values())
          
          while p2 - p1 + 1 - max_val > k:
             hashTable[s[p1]] -= 1
             p1+=1
             
          # this will happen when window - max_val <= k
          window = p2-p1+1
          max_window = max(window, max_window)
          p2+=1
       return max_window

# Other Attempt 
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        p1 = 0
        p2 = 0
        hashTable = defaultdict(int)
        maxLength = 0
        max_value = 0

        while p2 < len(s):
            hashTable[s[p2]]+=1
            max_value = max(hashTable.values()) 
            while p2-p1+1-max_value > k:
                hashTable[s[p1]]-=1
                p1+=1
            maxLength = max(maxLength, p2-p1+1)
            p2+=1
        return maxLength
        
          
if __name__ == "__main__":
  s = Solution()
  print(s.characterReplacement("AABABBA",1))


         
         