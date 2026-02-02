# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Same appoarch as next greater element with monotonic stack
# But you can't use hashTable, as nums can be repeating
# so push (val, index) into the stack. find the length of the linked list first tho
class Solution:
    def nextLargerNodes(self, head):
        length = 0
        temp = head
        while temp:
            length+=1
            temp=temp.next
        
        stack = []
        res = [0]*length
        t1 = head
        index = 0
        while t1:
            while stack and stack[-1][0] < t1.val:
                _, popped_index = stack.pop()
                res[popped_index] = t1.val
            
            stack.append((t1.val, index))
            index+=1
            t1=t1.next
        return res