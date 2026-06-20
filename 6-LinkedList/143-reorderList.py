# Here, my logic is to find the middle node via fast and slow pointers
# break the list, use a stack to get the second half of the list in reverse
# and rearrange the pointers to get the answers
# [ALTERNATE WAY]if rearranging it in is tough then use the logic from merge two sorted lists(easy)

# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __str__(self):
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return " -> ".join(result)
## You can't use new_node here, you should modify the list in place(We can only use the existing nodes)
# In Commented method, I created a new node and a new linked list
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Middle function
        def find_middle(head):
            slow = head
            fast = head

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            return slow
        
        # Reverse function
        def reverse_list(head):
            t1 = None
            t2 = head
            t3 = None

            while t2:
                t3 = t2.next
                t2.next = t1
                t1 = t2
                t2 = t3
            
            return t1

        # Edge cases
        if not head.next or not head:
            return head
        
        # Find middle and break into two halves
        middle_node = find_middle(head)
        t2 = middle_node.next
        middle_node.next = None

        # Reversing the second half
        t3 = reverse_list(t2)
        
        # Alternate bw two halves and add to the result list(no new nodes)
        dummy = ListNode(-1)
        t4 = dummy
        t1 = head

        while t1 or t3:
            if t1:
                t4.next = t1
                t4 = t1
                t1 = t1.next
            
            if t3:
                t4.next = t3
                t4 = t3
                t3 = t3.next
        
        return dummy.next

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Testing the reorderList function
if __name__ == "__main__":
    values = [1, 2, 3, 4, 5, 6, 7]  # Example input
    head = create_linked_list(values)
    
    print("Original List:", head)
    
    solution = Solution()
    head = solution.reorderList(head)
    
    print("Reordered List:", head)
            

        
