# Big Hint:- which triplet index to select? ans is in the target

# Check target[0] in 0th index of every triplet, target[1] in 1st index of evry triplet and target[2] in 2nd index of every index
# only allow it if a,b,c <= target[i]. (WE DON'T WANT MAX NUMBER TO COME INSIDE OUR LOGIC AND SPOIL EVERYTHING)
# FIND (max(a),max(b),max(c)) and compare with target.

class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        # target = [2,7,5]
        # inputs = [[2,5,3],[1,7,5]] -> combine them

        # target = [3,2,5]
        # inputs = [[3,4,5]] middle 2 is not there anywhere in index 1 -> return False

        #tuples = set()
        max_a = -1
        max_b = -1
        max_c = -1

        for a,b,c in triplets:
            if a <= target[0] and b <= target[1] and c <= target[2]:
                max_a = max(max_a, a)
                max_b = max(max_b, b)
                max_c = max(max_c, c)
                #tuples.add((a,b,c))

        #print(tuples)
        
        max_triplet = list((max_a,max_b,max_c))
        return max_triplet == target
            
        



        