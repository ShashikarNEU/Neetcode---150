# https://neetcode.io/solutions/letter-combinations-of-a-phone-number
# This recursion follows the test case example [23]
# for 23, abc and edf -> a goes with [edf], lly b and c to create 9 answers
# So, think this in terms of recursion, we are moving to next digit till the length of ans is reached, store ans and backtrack to check for the rest of the letters. For digits traversal, use index in argument and do index + 1 and access digit[index]
# Think about this for a while

# Recursive Soln
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        phoneHashTab = {
            "2": "abc",
            "3": "edf",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        if digits == "":
            return []
        res = []
        def backtrack(index, curr):
            if len(curr) == len(digits):
                res.append(curr)
                return
            for letter in phoneHashTab[digits[index]]:
                backtrack(index + 1, curr + letter)
        backtrack(0, "")
        return res
                
# Call the test function
if __name__ == "__main__":
    s = Solution()
    print(s.letterCombinations("23"))
                        


