# Logic
# Just observe the exmaple test cases in leetcode and find the algo from there
# Two Pointer appoarch will work here and when there is a overlapping, take max of start times and min of the end times.[IMP]
# To move the pointers, compare end times and see which is samller, move the smaller one first as we can still find intersections with the larger end time [IMP]
class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        start = 0
        end = 0
        result = []

        if firstList == [] or secondList == []:
            return []

        while start < len(firstList) and end < len(secondList):
            if firstList[start][1] >= secondList[end][0] and firstList[start][0] <= secondList[end][1]:
                result.append([max(firstList[start][0],secondList[end][0]), min(firstList[start][1],secondList[end][1])])
                
            if firstList[start][1] >= secondList[end][1]:
                end+=1
            else:
                start+=1
        
        return result

# Other Attempt
class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        p1 = 0
        p2 = 0
        res = []

        if firstList == [] or secondList == []:
            return []

        while p1 < len(firstList) and p2 < len(secondList):
            if firstList[p1][1] >= secondList[p2][0] and firstList[p1][0] <= secondList[p2][1]:
                res.append([max(firstList[p1][0], secondList[p2][0]), min(firstList[p1][1],secondList[p2][1])])
            if firstList[p1][1] > secondList[p2][1]:
                p2+=1
            else:
                p1+=1
        
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))
    print(s.intervalIntersection([[1,3],[5,9]], []))
                
                
                
            