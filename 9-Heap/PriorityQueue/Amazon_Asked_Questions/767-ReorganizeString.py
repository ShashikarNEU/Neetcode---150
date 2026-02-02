from collections import Counter, deque
import heapq

# GREEDY + HEAP
class Solution:
    def reorganizeString(self, s: str) -> str:
        hashTable = Counter(s)

        max_heap = []
        for u,v in hashTable.items():
            max_heap.append((-1 * v,u))
        
        heapq.heapify(max_heap)
        res = ""
        prev_letter = ''
        prev_count = 0

        while max_heap:
            count, letter = heapq.heappop(max_heap)
            if prev_letter != '' and prev_count!= 0:
                heapq.heappush(max_heap, (prev_count, prev_letter))
            res += letter
            count+=1
            prev_count = count
            prev_letter = letter
        
        return res if len(res) == len(s) else "" 

# GREEDY + HEAP + QUEUE
class Solution:
    def reorganizeString(self, s: str) -> str:
        hashMap = Counter(s)
        q = deque()
        max_heap = []
        for key, value in hashMap.items():
            heapq.heappush(max_heap, (-1*value, key))
        
        result = ""
        time = 0

        while max_heap or q:
            time += 1
            if max_heap:
              count, string = heapq.heappop(max_heap)
              result += string
              count+=1
              if count != 0:
                  q.append((time+1, count, string))
            else:
                return ""
            
            if q and q[0][0] == time:
                _, count, string = q.popleft()
                heapq.heappush(max_heap, (count, string))
            
        
        return result
            
            
                
                
            
            
        