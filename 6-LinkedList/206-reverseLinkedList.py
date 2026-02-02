# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# When reversing a list, consider one link reversal inside the loop, not 3 links - Think about the rest
# Hint - assign only one pointer to the list outside the loop(t2), assign the rest inside the loop and reverse link once
# in the while loop and notice how everything repeats    
class Solution:
    def reverseList(self, head):
        if not head or not head.next:
            return head
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

# Other Attempt
class Solution:
    def reverseList(self, head):
        t1, t3 = None, None
        t2 = head

        while t2 != None:
            t1 = t2.next
            t2.next = t3
            t3 = t2
            t2 = t1
        
        head = t3
        return head


def print_list(head):
    temp = head
    while temp:
        print(temp.val, end=" ")
        temp=temp.next
    
if __name__ == "__main__":

  # Deduct a loop in a linked list
  nod1 = Node(5)
  nod2 = Node(10)
  nod3 = Node(15)
  nod4 = Node(20)
  nod1.next = nod2
  nod2.next = nod3
  nod3.next = nod4
  head = nod1
  print_list(head)
  head = nod1
  s = Solution()
  head = s.reverseList(head)
  print("\nREVERSED LIST:-")
  print_list(head)

            