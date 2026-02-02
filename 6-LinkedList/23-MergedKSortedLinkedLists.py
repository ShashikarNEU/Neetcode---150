# NOT THAT HARD 
# https://neetcode.io/solutions/merge-k-sorted-lists
# this is a follow up to merged2sortedlinkedlists question
# from the array of linked lists
# take 2 lists and merged and create a new lists, keep on adding them to it. repeat this process till the len of OG list becomes 1 and return that
# we have to do for i in range(0,len(lists),2), if i+1 goes outbounds then, put None
# Do a dry run and see

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def merge2SortedLinkedLists(self, list1, list2):
        p1 = list1
        p2 = list2

        p3 = ListNode(-1)
        head = p3

        while p1 or p2:
            if p1 and p2:
                if p1.val <= p2.val:
                    p3.next = p1
                    p1 = p1.next
                else:
                    p3.next = p2
                    p2 = p2.next
            elif p1 and not p2:
                p3.next = p1
                p1 = p1.next
            elif p2 and not p1:
                p3.next = p2
                p2 = p2.next

            p3 = p3.next

        return head.next
                
    def mergeKLists(self, lists):
        if lists == [] or lists == None:
            return None
        
        while len(lists) > 1:
            #mergedLists = []
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None

                mergedList = self.merge2SortedLinkedLists(l1,l2)

                lists.append(mergedList)
                lists.remove(lists[i])
                if lists[i+1] != None:
                    lists.remove(lists[i+1])
            #lists = mergedLists
        
        return lists[0]