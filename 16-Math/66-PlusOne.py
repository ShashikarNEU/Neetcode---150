# EDGE CASE - all digits are 9's
# Do Ripple carry addition logic(similar to add numbers in linked list)

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        t1 = len(digits)-1
        t2 = 0
        carry = 0
        ans = []

        while t1 >= 0 or t2 >= 0:
            num1 = 0 if t1 < 0 else digits[t1]
            num2 = 0 if t2 < 0 else 1

            res = num1 + num2 + carry
            carry = res // 10
            res = res % 10
            ans.append(res)

            t1-=1
            t2-=1
        
        if carry != 0:
            ans.append(carry)
        
        return ans[::-1]

        