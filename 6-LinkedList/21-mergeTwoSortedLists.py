# Logic for this question is very easy - have two pointers and 
# add them to a new list based on which val is smaller
# Have a dummy node to start with and keep on adding nodes from the both list depending on which is smaller, increment the t1,t2
# after adding, Our new list should also have the pointer in the last to easily do new_pointer.next = min(t1 or t2) then t1=t1.next or t2=t2.next
# if t2 is only there, # if t1 is only there and # if both are empty return None -> Consider these cases inside the while loop and in starting also

# Don't confuse AND , OR in while loop. and needs both to work and or only needs one to work.

# general linked list tips
# In linked list questions, always handle edges cases first(if head of list1 is empty)
# Don't use append fn, use append internally, because n time for every append fn call

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution: 
    def mergeTwoLists(self, list1, list2):
        t1 = list1
        t2 = list2
        temp = ListNode() # dummy node
        head = temp # Head of our new list

        # if t2 is only there
        if not t1 and t2:
            return t2
        # if t1 is only there
        if not t2 and t1:
            return t1
        # if both are empty return None
        if not t2 and not t1:
            return None
        
        while t1 or t2:
            if t1 and t2:
                if t1.val <= t2.val:
                    temp.next = t1
                    temp = t1
                    t1=t1.next
                else:
                    temp.next = t2
                    temp = t2
                    t2 = t2.next

            if not t1 and t2:
                temp.next = t2
                temp = t2
                t2 = t2.next

            if not t2 and t1:
                temp.next = t1
                temp = t1
                t1 = t1.next
            
        return head.next

# Other Attempt
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        t3 = ListNode(-1)
        head = t3

        t1 = list1
        t2 = list2

        while t1 or t2:
            if t1 and t2:
                if t1.val <= t2.val:
                    t3.next = t1
                    t3 = t1
                    t1 = t1.next
                else:
                    t3.next = t2
                    t3 = t2
                    t2 = t2.next
            elif t1 and not t2:
                t3.next  = t1
                break
            elif t2 and not t1:
                t3.next = t2
                break
        
        return head.next 

if __name__ == "__main__":
    s = Solution()
    
    # Creating first linked list: 1 -> 3 -> 5
    list1 = ListNode(1)
    #list1.next = ListNode(3)
    #list1.next.next = ListNode(5)

    # Creating second linked list: 2 -> 4 -> 6
    list2 = ListNode(2)
    list2.next = ListNode(4)
    list2.next.next = ListNode(6)

    # Merging the lists
    merged_list = s.mergeTwoLists(list1, list2)

    # Printing merged list
    temp = merged_list
    while temp:
        print(temp.val, end=" -> ")
        temp = temp.next
