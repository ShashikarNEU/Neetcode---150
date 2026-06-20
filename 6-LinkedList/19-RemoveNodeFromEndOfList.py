# Use dummy node and only consider length = 1 and n = 1 edge case. dummy solves the rest of the edge cases.

# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        t1 = head

        # Find length of the list
        length = 0
        while t1:
            length += 1
            t1 = t1.next
        
        if length == 1 and n == 1:
            return None
        
        t2 = dummy
        for i in range(length-n):
            t2 = t2.next
        
        prev = t2
        curr = t2.next
        after = curr.next

        prev.next = after
        curr.next = None
        
        return dummy.next

# Helper function to print the linked list
def print_linked_list(head):
    values = []
    while head:
        values.append(str(head.val))
        head = head.next
    print(" -> ".join(values) if values else "Empty List")

# Helper function to create a linked list from a list
def create_linked_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Main function to test removeNthFromEnd
def main():
    values = [1,2,3,4,5]  # Example list
    n = 1  # Remove 2nd node from the end
    head = create_linked_list(values)
    
    print("Original list:")
    print_linked_list(head)
    
    solution = Solution()
    new_head = solution.removeNthFromEnd(head, n)
    
    print("List after removing", n, "th node from the end:")
    print_linked_list(new_head)

# Run the test
main()
            