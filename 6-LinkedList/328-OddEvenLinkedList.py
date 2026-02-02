# This is a pointer based questions

# Two ways to solve these pointer based questions
# 1. Use Dummy node(-1)
# 2. Solve it in linked list place, t1.next = t2.next logic


# have odd -> head and even -> head.next
# and do odd.next = even.next and move odd forward. now do the same for even
# while loop codn -> even will reach the end first. it can reach the end in two ways. even will be None or on the last element.
# so, do while even and even.next -> if one of these codns is true, exit loop

class Solution:
    def oddEvenList(self, head):
        if not head:
            return None
        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next
        
        # Linking the lists here
        odd.next = even_head

        return head
        

