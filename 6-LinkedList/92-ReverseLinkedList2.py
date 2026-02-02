# LOGIC
# Basic structure-> Have 4 pointers -  (StartLeft,StartRight,EndLeft,EndRight)
# StartRight and EndLeft are at left and right index respectfully
# StartLeft is one before Left and EndRight is one after Right

# Use for loops for getting to the node
# and use dummy node as -1 in the start, you can skip a lot of edges cases with this dummy node
# disconnect pointers acc
# Have a reverse fn and pass startRight to it
# after rversing, reconnect them
# and return dummy.next

# Remember dummy is the king here


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverse(head):
            begin = head
            t2 = head
            t1, t3 = None, None

            while t2 != None:
                t3 = t2.next
                t2.next = t1
                t1 = t2
                t2 = t3
            
            head = t1
            return head, begin
        
        if left == right:
            return head
        
        dummy = ListNode(0, head)
        t1 = dummy
        
        # Move to node before left position
        for _ in range(left - 1):
            t1 = t1.next
        
        startLeft = t1
        startRight = t1.next
        
        # Move to right position
        for _ in range(right - left + 1):
            t1 = t1.next
        
        endLeft = t1
        endRight = t1.next
        
        # Disconnect and reverse
        endLeft.next = None
        startLeft.next = None
        
        list_start, list_end = reverse(startRight)
        
        # Reconnect
        startLeft.next = list_start
        list_end.next = endRight
        
        return dummy.next

            
        
            