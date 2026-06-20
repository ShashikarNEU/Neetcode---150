# Don't confuse it with reverse method. Answer also will be reversed, they want the reversed answer
# Just read the input and add it from the starting, have carry variable
# if carry is not 0 after while loop, append carry also and return the answer

# In interview, don't forget to append carry if carry is not 0

# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        t1 = l1
        t2 = l2
        carry = 0
        dummy = ListNode(-1)
        t3 = dummy

        while t1 or t2:
            v1 = 0 if not t1 else t1.val
            v2 = 0 if not t2 else t2.val

            res = v1 + v2 + carry
            carry = res // 10
            v3 = res % 10

            new_node = ListNode(v3)
            t3.next = new_node
            t3 = new_node

            if t1:
                t1 = t1.next
            if t2:
                t2 = t2.next
        
        if carry != 0:
            new_node = ListNode(carry)
            t3.next = new_node
            t3 = new_node
        
        return dummy.next
                

             
        