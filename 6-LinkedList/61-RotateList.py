# Here find the rotation point(Length of list - k)
# After that point, break the list. connect last of the orginal list to the start of first list.
# but if k == length or > length then take k=k%length
# if k ==0 after that, return OG linked list 
# Do a dry run with different k's and think

# EDGE CASES:
#1. when k is a multiple of length or k == 0, then list remains the same(return head)
#2. if list is empty or one node long, ans remains the same(return head)

class Solution:
    def rotateRight(self, head, k: int):
        if head == None:
            return None
        
        # Finding length and bring t3 pointer to the last
        length = 0
        temp = head
        t3 = None
        while temp:
            length+=1
            t3 = temp
            temp=temp.next
        
        # if k is equal to length then return the list unmodified, if it's greater take % and modify the list[Do dry run and think!!]
        if k >= length:
            k = k % length
      
        if k == 0:
            return head
        
        rotate_point = length - k
        t2 = head
        t1 = head

        # Find rotate point
        for i in range(rotate_point-1):
            t1 = t1.next
        
        # Break off rotate point
        new_head = t1.next
        t1.next = None

        # Connect with the starting of the other list
        t3.next = t2

        return new_head

# Other Attempt
class Solution:
    def rotateRight(self, head, k: int):
        length = 1

        l = head

        # EDGE CASE: #2
        if not head or not head.next:
            return head

        # Find Length
        while l.next:
            length+=1
            l=l.next
        # Find where to break the list
        k = k % length if k > length else k
        # EDGE CASE: #1
        if k == length or k == 0: return head
        s = length - k - 1
        t1 = head
        t2 = head

        for i in range(s):
            t1 = t1.next
        
        # Find new head, connect the remaining list to the starting of the list(using l pointer which is already at the end!)
        head = t1.next
        t1.next = None
        l.next = t2

        return head

        