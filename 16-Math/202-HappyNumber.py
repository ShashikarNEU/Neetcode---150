# Do num seperation logic and sum square together
# Use a set cuz of the cycle

# if False, num will loop endlessly in a cycle
# TC = logn, SC = logn
class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squares(n):
            res = 0
            while n > 0:
                r = n % 10
                res += r**2
                n = n // 10
            
            return res
        
        visited = set()
        
        while True:
            n = sum_of_squares(n)
            #print(n)
            if n == 1:
                return True
            if n in visited:
                return False
            visited.add(n)
        
        return False



        