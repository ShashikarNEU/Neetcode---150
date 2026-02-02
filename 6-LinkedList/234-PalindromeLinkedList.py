# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
     def middleNode(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next   
        return slow
     
     def display(self, head):
        temp = head
        while temp:
            print(temp.val, end="")
            if temp.next:
                print("->", end="")
            temp = temp.next
     
     def isPalindrome(self, head):
         if not head or not head.next:
             return True
  
         middle = self.middleNode(head)
         
         head2 = middle
         self.display(head2)
         

         stack = []
         while head2:
             stack.append(head2.val)
             head2 = head2.next
         temp = head

         while temp and stack:   
             val = stack.pop()

             if val != temp.val:
                 return False
             
             temp=temp.next
         return True

# Helper function to create a linked list from a list
def create_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Test Cases
test_cases = [
    [1, 2, 2, 1],   # True
    [1, 2, 3, 2, 1], # True
    [1, 2, 3, 4],   # False
    [7],            # True
    [9, 9],         # True
    [1, 2],         # False
    [1, 2, 3, 4, 5, 4, 3, 2, 1], # True
    []              # True (empty list)
]

# Running Test Cases
solution = Solution()
for case in test_cases:
    head = create_linked_list(case)
    print(f"Input: {case} -> Output: {solution.isPalindrome(head)}")
    
             
    
    
        