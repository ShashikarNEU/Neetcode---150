# Use Pointers[TRICKY QUESTION]

# See this question and read, dry run this once
# manage grp prev, grp next and connect groupPrev to head of the reversed list(t1 here)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getKthNode(self, temp, k):
        while temp and k>0:
            temp=temp.next
            k-=1  
        return temp
        
    def reverseKGroup(self, head, k: int):
        # Edge case
        if not head or k <= 1:
            return head
        
        dummy = ListNode(-1,head)
        groupPrev = dummy
        while True:
          kth = self.getKthNode(groupPrev,k)
          if not kth:
              break
          groupNext = kth.next

          t1 = groupNext
          temp = groupPrev.next
          t2 = groupPrev.next
         
          while t2 != groupNext:
              t3 = t2.next
              t2.next = t1
              t1 = t2
              t2 = t3
          
          groupPrev.next = t1
          temp.next = groupNext
          groupPrev = temp
        
        return dummy.next







