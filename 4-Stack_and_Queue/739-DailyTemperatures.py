# Monotonically decreasing stack(Pattern)
# Same type of question as next greatest element 1 and 2
# Refer them also
# They are asked in amazon
# Do a dry run with example and understand the pattern

# Instead of using a hashTable, we can store the indexes in the stack
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        res = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                res[index] = i-index
            stack.append(i)
        return res

if __name__ == "__main__":
  s = Solution()
  print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))
  print(s.dailyTemperatures([30,40,50,60]))
  print(s.dailyTemperatures([30,60,90]))


