# [MED-HARD] -> TRICKY QUESTION
# Data structure context
# Have a hashmap with key: Node(VALUE will be a pointer to the node)
# To handle the order of the priority order have a double linked list, where 
# inserting and deleting is O(1) time. Have Right node and Left node in this structure(Left<->Right)

# When data is inserted into the hashtable, value pointer will point to the node and node will inserted before right cuz its
# most recented node. when updating a val, delete it and insert the node before right to keep priority
# when size>k, delete the left.next node since it's not used or updated.
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.size = capacity
        # Least recented used node
        self.left = Node(0,0)
        # Most recented used node
        self.right = Node(0,0)

        # Initial setup (Left <-> Right) doubly linked
        self.left.next = self.right
        self.right.prev = self.left

    # This will insert node just before right
    # For single linked list, we have to trasverse it(n time) and insert before right
    # but here, since self.right is avaiable and it's doubly linked, you can just go one back and insert in O(1) time[IMP]
    def append(self, node):
        head = self.right
        head = head.prev
        after = head.next
        head.next = node
        node.prev = head
        node.next = after
        after.prev = node
        return node
    
    # since it's doubly linked list, it's O(1) time and initial case is (left-node-right) so no need of handling edge cases
    def remove(self, node):
        before = node.prev
        after = node.next
        before.next = after
        after.prev = before
    
    # For Get, return hashtable(key).val since value is a node but, we have to move node to most recented used so, we delete the node and append it before right node. [GENERAL LOGIC]if we keep doing this then, all recented used nodes will move towards right and LRU node will be in the left
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.append(self.cache[key])
            return self.cache[key].value
        return -1
        
    # For Put, 2 cases, 
    # Case 1 - if key exists, just update the value but we should also 
    # update the priority also so, remove(node) and append it before 
    # right with new value. make sure to link it to hashTable[key] = new node inserted
    # Case 2 - if key does not exist, append new node before right and link it to the hashTable, hashTable[key] = new node

    # Main logic of this question -> if size of hashTable > capacity 
    # then, delete self.left.next node and delete it's hashTable record
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            node = self.append(Node(key, value))
            self.cache[key] = node
        else:
            self.cache[key] = Node(key, value)
            self.append(self.cache[key])
        
        if len(self.cache) > self.size:
            LRU = self.left.next
            self.remove(LRU)
            del self.cache[LRU.key]

# Other Attempt
class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.k = capacity
        self.hashMap = {}
        self.left = Node(-1,-1)
        self.right = Node(-1,-1)

        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node):
        temp = self.right
        t1 = temp.prev
        t1.next = node
        node.prev = t1
        node.next = temp
        temp.prev = node
    
    def remove(self, node):
        temp = node
        t1 = node.prev
        t2 = node.next
        t1.next = t2
        t2.prev = t1
        node.next = None
        node.prev = None

        return node

    def get(self, key: int) -> int:
        if key in self.hashMap:
            node = self.hashMap[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            old_node = self.hashMap[key]
            self.remove(old_node)
            new_node = Node(key, value)
            self.hashMap[key] = new_node
            self.insert(new_node)
        else:
            new_node = Node(key, value)
            self.hashMap[key] = new_node
            self.insert(new_node)
        
        if len(self.hashMap) > self.k:
            temp = self.left
            key = temp.next.key
            self.remove(temp.next)
            del self.hashMap[key]

# Call the test function
if __name__ == "__main__":
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1) # cache is {1=1}
    lRUCache.put(2, 2) # cache is {1=1, 2=2}
    lRUCache.get(1)    # return 1
    lRUCache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    lRUCache.get(2)    # returns -1 (not found)
    lRUCache.put(4, 4) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    lRUCache.get(1)    # return -1 (not found)
    lRUCache.get(3)    # return 3
    lRUCache.get(4)    # return 4
        
        