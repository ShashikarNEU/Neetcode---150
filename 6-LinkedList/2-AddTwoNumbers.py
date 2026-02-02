# Don't confuse it with reverse method. Answer also will be reversed, they want the reversed answer
# Just read the input and add it from the starting, have carry variable
# if carry is not 0 after while loop, append carry also and return the answer

# In interview, don't forget to append carry if carry is not 0

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:          
    def addTwoNumbers(self, l1, l2):        
        current = ListNode() # Dummy node
        head = current
        carry = 0
        val1 = 0
        val2 = 0

        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            result = total % 10
            carry = total // 10 if total > 9 else 0
            node = ListNode(result)
            current.next = node
            current = node

            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        
        if carry != 0:
            node = ListNode(carry)
            current.next = node
            current = node
      
        return head.next # skip dummy node
                

             
        