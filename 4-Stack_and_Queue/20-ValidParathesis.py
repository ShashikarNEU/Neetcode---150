## I misunderstood the question earlier 
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order. [IMPORTANT]
# Every close bracket has a corresponding open bracket of the same type.
# Eg:= [({})] is accepted but [({)]} is not accpeted because the order is wrong here (We should close the lastest bracket first)

# Here I can compare manually - [],{},() but it's better to use a hashmap
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashMap = {'{':'}', '[':']','(':')'} # hashmap
        for string in s:
            if string in hashMap:
                stack.append(string)
            else:
                if len(stack) == 0:
                    return False
                topString = stack[-1] # top element
                if hashMap[topString] == string:
                    stack.pop()
                    continue
                else:
                    return False
      
        return len(stack) == 0

# Other Attempt
class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {"]":"[", ")":"(", "}":"{"}
        stack = []

        for string in s:
            if string == "}" or string == "]" or string == ")":
                if not stack:
                    return False
                elif stack[-1] != hashMap[string]:
                    return False
                else:
                    stack.pop()
                    
            else:
                stack.append(string)
        


        return True if not stack else False



                