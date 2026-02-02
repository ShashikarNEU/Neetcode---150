# TRICKY QUESTION
# WE have to do ripple carry multiplication(school way)

# Refer video for logic -> https://neetcode.io/solutions/multiply-strings
# instead of having carry, have digit in (i1+i2)th place and carry at i1+i2+1 th place(Add them)

# reverse them before starting and reverse the result also

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"
        
        num1, num2 = num1[::-1], num2[::-1]

        res = [0] * (len(num1)+len(num2))

        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])

                res[i1+i2] += (digit)
                # if res[i1+i2] itself becomes more than 9 so, we do %, // to res[i1+i2]

                res[i1+i2+1] += (res[i1+i2]//10)

                res[i1+i2] = res[i1+i2]%10
               
        
        res = res[::-1]
        begin = 0

        # Removing leading zeros in the beginning
        while res[begin] == 0 and begin < len(res):
            begin+=1
        
        # output = ""
        # for i in range(begin, len(res)):
        #     output += str(res[i])
        # return output
        
        res = map(str, res[begin:])
        return "".join(res)
        


        

