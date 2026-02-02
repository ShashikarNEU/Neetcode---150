# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteFromList(self, head, index, length):
        if not head:
            return None
        
        # List has only one node and we have to delete it
        if index == 0 and not head.next:
            head = None
            return head
        
        # List has more than one node and index = 0
        if index == 0 and head.next:
            temp = head.next
            head.next = None
            head = temp
            return head

        temp = head
        for i in range(index-1):
            temp = temp.next
        
        # Last index case
        if index == length - 1:
            temp.next = None
            return head
        
        # General/Middle case
        current = temp.next
        node_after = current.next
        temp.next = node_after
        current.next = None

        return head

    def removeNthFromEnd(self, head, n):
        lp = head
        length = 0
        while lp:
            length+=1
            lp=lp.next
        print(length)
        head = self.deleteFromList(head, length - n, length)
        return head

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
            