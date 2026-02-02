# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# While loop codn - fast pointer will reach the end first, but it will land in the last node or 
# null, we don't know which - so we need both fast and fast.next as exit codn for while loop [Think about this]
class Solution:
    def hasCycle(self, head) -> bool:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False