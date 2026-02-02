# Can use set or hashTable here. Logic:- Basic Variable Window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1 = 0
        p2 = 0
        max_len = 0
        char_set = set()
        
        while p2 < len(s):
            while s[p2] in char_set:
                char_set.remove(s[p1])
                p1 += 1
            
            char_set.add(s[p2])
            #print(char_set) 
            window = p2 - p1 + 1
            max_len = max(max_len, window)
            p2 += 1
        
        return max_len
