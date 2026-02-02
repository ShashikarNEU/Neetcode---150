# TRICKY PROBLEM (EXACT SAME QUESTION AS LC 1296. Divide Array in Sets of K Consecutive Numbers)
# Use min_heap + hashMap(Counter)
# when number are repeating the struggle is to come back to the min no
# use a min heap for that

# Numbers have to be consecutive 
# if not, return False
# if hashMap[key] becomes zero, pop it out from the heap

# Form a hashMap(Counter) and have a min_heap
# find min from heap and loop from min to grp_size, decrement count
# when hashMap[key] becomes zero, pop it. IF it's not the key(i) which became 0, you have the EDGE CASE HERE
# return False
# Use DRY RUN or watch video to get the EDGE CASE [Eg:- 1 1 2 3 4 5, k = 3]

# Video -> https://neetcode.io/solutions/hand-of-straights

from collections import Counter
import heapq


class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        hashMap = Counter(hand)

        min_heap = list(hashMap.keys())
        heapq.heapify(min_heap)

        while min_heap:
            first = min_heap[0]

            for i in range(first, first+groupSize):
                if i not in hashMap:
                    return False
                hashMap[i]-=1

                if hashMap[i] == 0:
                    min_value = heapq.heappop(min_heap)
                    # EDGE CASE
                    if i != min_value:
                        return False
        
        return True
        