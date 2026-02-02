# Unique Problem(no pattern)
# Tricky

# In ur mind, form a diff arr (gas[i] - cost[i]), from that arr, we should start from any point and complete
# the loop without total < 0. 
# and always sum(gas) > sum(cost), if not, return -1
# one n loop is enough, no need of looping around, when total < 0, update it as 0 and set res = i+1, start of the non -ve total
# will always be the ans
# Diffcult to understand even with dry run ik, just know the code

class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        total = 0
        res = 0

        if sum(gas) < sum(cost):
            return -1

        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                res = i+1
        
        return res