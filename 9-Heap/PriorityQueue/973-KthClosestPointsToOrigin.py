# This question was easy
# use min heap, heappop() k elements so, record the distance, add sqrt(x^2+y^2) 
# in the 0th index in the list (distance,x,y)
# heapify will only use p[0](distance) element when heapifing

# or you can use a hash map to store (distance, [x,y]) but that's extra space

import math
import heapq
class Solution:
    def kClosest(self, points, k):
        for p in points:
            p.insert(0,math.sqrt(p[0]**2 + p[1]**2))
        #print(points)
        result = []
        heapq.heapify(points)
        #print(points)
        for _ in range(k):
            p = heapq.heappop(points)
            result.append([p[1],p[2]])
        return result

# Call the test function
if __name__ == "__main__":
    s = Solution()
    print(s.kClosest([[1,3],[-2,2]],1))
    print(s.kClosest([[3,3],[5,-1],[-2,4]],2))
            
        

        
            
        
        