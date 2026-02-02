# THIS IS A FOLLOW UP QUESTION FROM ReoraganizeString.py
# Refer that first

# We are using greedy(popping the max occurences) + heap approach here
# [TRICKY QUESTION] - https://neetcode.io/solutions/task-scheduler [WATCH VIDEO]
# So, we have to find the min time to form a sequence with n cooldown period bw letters here
# Take larger occurences to form a max heap[THINK!!], give larger occurences using heappop() -> do +1 to occurences when poped
# We need to track the cooldown period also, insert (count, letter) to max_heap and have a queue for cooldown purpose
# Insert [Time to pop it out, [occurences, Letter]], When count reaches the queue[front][0] time, 
# then pop it and push it to the max heap

import heapq
from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        queue = deque()
        hashMap = {}
        for task in tasks:
            if task in hashMap:
                hashMap[task]+=1
            else:
                hashMap[task]=1

        # Creating a number of [Occurances,Letter] heap
        # we need a max heap here so, inserting -y
        max_heap = [[-y,x] for x,y in hashMap.items()]
        print(hashMap)
        heapq.heapify(max_heap)
        print(max_heap)
        count = 0
        while queue or max_heap:
            count+=1
            if max_heap:
                task = heapq.heappop(max_heap)
                print(task[1], end=" ")
                task[0]+=1 # Since it's negative
                if task[0]!=0:
                    queue.append([count+n, task])
            else:
                print("Idle", end=" ")
            
            if queue and queue[0][0] == count:
                _, task = queue.popleft()
                heapq.heappush(max_heap, task)
        return count

# Other Attempt
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        hashMap = Counter(tasks)
        queue = deque()

        max_heap = []
        for k,v in hashMap.items():
            max_heap.append((-1 * v,k))
        
        heapq.heapify(max_heap)
        
        time = 0
        
        while queue or max_heap:
            if len(max_heap) != 0:
                value, letter = heapq.heappop(max_heap)
                value *= -1
                #print(letter)

                value-=1
                if value != 0:
                    queue.append((time+n, value, letter))
            # else:
            #     print("idle")
            
            if queue and queue[0][0] == time:
                time, value, letter = queue.popleft()
                heapq.heappush(max_heap, (-1*value, letter))
            
            time += 1
        
        return time
    
if __name__ == "__main__":
    s = Solution()
    print("\n")
    print(s.leastInterval(["A","A","A","B","B","B"],2))



        



        

        