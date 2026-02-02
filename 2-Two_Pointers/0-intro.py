# Two pointer pattern intro
# https://www.youtube.com/watch?v=-gjxg6Pln50&t=26s
# Two Types of two pointer is there
# Opp direction pointers, one at the start and one at the end, They meet towards the middle
# Usually for this pattern, we do it in a sorted array
# We move the pointers - right or left acc to the codn in the sorted array
# Example: sorted two sum
# When to use: Sorted arrays, range-based problems, sum-pair problems
def sortedTwoSum(arr, target):
  p1 = 0
  p2 = len(arr)-1

  while p1 < p2:
    sum = arr[p1] + arr[p2]
    if sum == target:
      return p1,p2
    if sum > target:
      p2-=1
    else:
      p1+=1
  return None

# same direction pointers, one slow and one fast, we use this in linked list
# while codn for exit in while fast and fast.next: because fast pointer 
# can end in the end of the list or it can go to null at the end
# When to use: Linked lists, cycle detection, optimal subarrays, sliding windows
# Example: Deduct a loop in a linked list
class Node:
  def __init__(self, val = 0, next = None):
    self.val = val
    self.next = next

def hasCycle(head):
  slow = head
  fast = head
  while fast and fast.next:
    if slow == fast:
      return True
    slow = slow.next
    fast = fast.next.next
  return False

if __name__ == "__main__":
  # Sorted Two Sum
  list1 = [1,2,3,4,5,6,7]
  target = 7
  print(sortedTwoSum(list1, target))

  # Deduct a loop in a linked list
  nod1 = Node(5)
  nod2 = Node(10)
  nod3 = Node(15)
  nod4 = Node(20)
  nod1.next = nod2
  nod2.next = nod3
  nod3.next = nod4
  nod4.next = nod3 # This creates a cycle
  head = nod1
  print(hasCycle(head))