# [HINT] you need to use hashmap to get random pointer nodes in const time
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        temp = head
        hashTable = {}
        current = Node(-1)
        new_head = current
        # Create the new list with only next pointer first
        while temp:
            p = Node(temp.val)
            current.next = p
            current = p
            temp=temp.next
        new_head = new_head.next # skip the dummy node
        p1 = head
        p2 = new_head
        # Store the same values in the hash table(node from old list, node from the new linked list)
        while p1:
            hashTable[p1] = p2
            p2=p2.next
            p1=p1.next
        p3 = head
        p4 = new_head
        print(hashTable)
        #print_list(new_head)
        # iterate the old list, new list with next, find random pointers and use the hash table to get the node of the new list and link them in the new list
        while p3:
            r1 = p3.random
            if r1 is not None:
                node = hashTable.get(r1)
                p4.random = node
            p4=p4.next
            p3=p3.next
        return new_head

# Other Attempt
class Solution:
    def copyRandomList(self, head):
        p1 = head
        p2 = Node(-1)
        p3 = p2
        hashMap = {}

        # Creating a new linked list without random pointers
        while p1:
            new_node = Node(p1.val)
            p2.next = new_node
            p2 = new_node
            hashMap[p1] = new_node
            p1 = p1.next
        
        # p3 is the new linked list
        # To remove -1 from the new list
        p3 = p3.next
        temp = head
        new_head = p3
        while temp:
            if not temp.random:
                p3.random = None
            else:
                p3.random = hashMap[temp.random]
            p3 = p3.next
            temp = temp.next
        
        return new_head

# Printing the original list
def print_list(head):
    nodes = []
    while head:
        random_val = head.random.val if head.random else "None"
        nodes.append(f"({head.val}, Random: {random_val})")
        head = head.next
    print(" -> ".join(nodes))

def main():
    # Creating nodes
    node1 = Node(7)
    node2 = Node(13)
    node3 = Node(11)
    node4 = Node(10)
    node5 = Node(1)

    # Setting up next pointers
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    # Setting up random pointers
    node2.random = node1
    node3.random = node5
    node4.random = node3
    node5.random = node1

    print("Original list:")
    print_list(node1)

    # Copying the list
    solution = Solution()
    copied_head = solution.copyRandomList(node1)

    print("Copied list:")
    print_list(copied_head)

# Run the test
main()

            