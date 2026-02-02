# This questions logic is not that hard to guess but I faced some diffculty in coding

# Have two lists to begin with - pending(tasks) and avaiable tasks
# Have a while loop with time running inside it
# For avaiable tasks. once the time is here do while loop and put everything into avaiable tasks since multiple items can have the same enqueue time
# While storing in avaiable time, store (processing time, index) for easy heap retreival - we want the shortest processing time first then index if processing time same. Use queue as a task processor, if queue is empty, heappop() FROM avaiable tasks and put into queue  with (index, finished time = processing time + current time)
# once finished time is reached, pop from the queue. This should be in the starting[THINK]. The main while loop will run untill avaiable or tasks is empty
# ALMOST CORRECT CODE
import heapq
from collections import deque
class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        for index, task in enumerate(tasks):
            task.append(index)
        #print(tasks)
        
        heapq.heapify(tasks)
        queue = deque()
        time = 1
        result = []
        avaiable_tasks = []
        while tasks or avaiable_tasks:
            # print("-------------------")
            # print("Time: ", time)
            if queue and queue[0][1] == time:
              queue.popleft() # Processing finished
              #print(queue)
            
            # Putting those tasks in avaiable list once the enqueue time is reached for tasks
            while tasks and tasks[0][0] <= time:
                enqueue_time, processing_time, index1 = heapq.heappop(tasks) 
                heapq.heappush(avaiable_tasks, [processing_time, index1])
           
            # print("avaiable tasks: ", avaiable_tasks)
            # print("tasks: ", tasks)

            if not queue and avaiable_tasks:
                processing_time, index1 = heapq.heappop(avaiable_tasks)
                finishing_time = processing_time + time
                queue.append([index1, finishing_time]) # Processing Start
                # print("queue: ", queue)
                result.append(index1)

            time+=1

        return result

# [IMP] My solution is almost correct but I am missing the time handling properly. We can skip to when the next task is avaiable without using queue. This is to reduce the run time a lot.[THINK] - HAVE TO CHANGE VERY LESS CODE
# CORRECT CODE
class Solution:
    def getOrder(self, tasks):
        available = []
        pending = []
        for i, (enqueueTime, processTime) in enumerate(tasks):
            heapq.heappush(pending, (enqueueTime, processTime, i))

        time = 0
        res = []
        while pending or available:
            while pending and pending[0][0] <= time:
                enqueueTime, processTime, i = heapq.heappop(pending)
                heapq.heappush(available, (processTime, i))

            if not available:
                time = pending[0][0]
                continue

            processTime, i = heapq.heappop(available)
            time += processTime
            res.append(i)

        return res

# Call the test function
if __name__ == "__main__":
    s = Solution()
    print(s.getOrder([[1,2],[2,4],[3,2],[4,1]]))
    print(s.getOrder([[7,10],[7,12],[7,5],[7,4],[7,2]]))

        