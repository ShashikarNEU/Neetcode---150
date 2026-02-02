# Have two pointers - first and last and compare
class Solution:
    def isPalindrome(self, s: str) -> bool:
       strList = [string for string in s if string.isalnum()] # isalnum() is used to get alphanumeric charcaters - letters and numbers
       p1 = 0
       p2 = len(strList) - 1
       print("".join(strList))

       while p1 < p2:
        if strList[p1].lower() != strList[p2].lower():
          return False
        p1+=1
        p2-=1

       return True