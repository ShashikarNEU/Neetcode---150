# Pretty simple logic - use max heap(use -ve numbers in heapq)
import heapq
class Solution:
    def lastStoneWeight(self, stones):
        for i in range(len(stones)):
            stones[i]*=-1
        heapq.heapify(stones)
        while len(stones)>1:
            stone_1 = -heapq.heappop(stones)
            stone_2 = -heapq.heappop(stones)
            if stone_1 != stone_2:
                heapq.heappush(stones, -(stone_1 - stone_2))
        if len(stones) != 0:
            stones[0]*=-1
            return stones[0]
        return 0

# Call the test function
if __name__ == "__main__":
    s = Solution()
    print(s.lastStoneWeight([2,7,4,1,8,1]))
    print(s.lastStoneWeight([1]))


