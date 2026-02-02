# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next      
        return slow
    
# [VERY IMP]
# I had a small confusion in middle
# for even inputs like 1->2->3->4
# middle will return 3 not 2

# for odd inputs 1->2->3->4->5, it will return 3