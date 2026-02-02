# Definition for singly-linked list.

# While loop checking codn explained
# if t1 is null before reaching the end of the loop, it won't exiting. 
# once it's checks every line only it will check the while codn. BE AWARE OF THIS!!

# https://www.youtube.com/watch?v=o811TZLAWOo
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head):
        if not head:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        t1 = head
        t2 = head.next

        while t1 and t2:
            t1.next = t2.next
            t2.next = t1
            prev.next = t2
            prev = t1
            t1 = t1.next
            t2 = t1.next if t1 else None
        
        return dummy.next


            