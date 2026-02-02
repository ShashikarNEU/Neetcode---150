# Here, my logic is to find the middle node via fast and slow pointers
# break the list, use a stack to get the second half of the list in reverse
# and rearrange the pointers to get the answers
# [ALTERNATE WAY]if rearranging it in is tough then use the logic from merge two sorted lists(easy)

# Definition for singly-linked list.
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
    def middleNode(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # if list is of size 2, ans is same
        if not head or not head.next or not head.next.next:
            return head
        
        stack = []
        middle = self.middleNode(head)
        t1 = middle
        middle = middle.next # Middle element will be always last, so keep it in the first half of the list
        while middle:
            stack.append(middle)
            middle = middle.next
        print(len(stack))
        t1.next = None # Breaking the list
        t1 = head
        #print(stack)
        while t1 and stack:
            t3 = stack.pop()
            t2 = t1.next
            t1.next = t3
            t3.next = t2
            t1 = t2
            # if len(stack) == 0:
            #     break
        return head
            
class Solution:
    def middleNode(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def reverseList(self, head):
        t1 = None
        t2 = head
        t3 = None

        while t2:
            t3 = t2.next
            t2.next = t1
            t1 = t2
            t2 = t3
        
        head = t1
        return head
    
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        p1 = head
        middle = self.middleNode(head)
        p2 = middle.next
        middle.next = None
        p2 = self.reverseList(p2)
        p3, p4 = None, None

        while p1 and p2:
            p3 = p1.next
            p1.next = p2
            p4 = p2.next
            p2.next = p3
            p1 = p3
            p2 = p4
        
        return head
    
    # Other Attempt
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        middle = self.middleNode(head)
        t3 = middle.next
        middle.next = None
        dummy = ListNode(-1)
        t4 = dummy

        t2 = self.reverseList(t3)
        t1 = head

        while t1 or t2:
            if t1 and t2:
                t4.next = t1
                t4 = t1
                t1 = t1.next

                t4.next = t2
                t4 = t2
                t2 = t2.next                
            elif t1 and not t2:
                t4.next = t1
                t4 = t1
                t1 = t1.next
            elif t2 and not t1:
                t4.next = t2
                t4 = t2
                t2 = t2.next

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
            

        
