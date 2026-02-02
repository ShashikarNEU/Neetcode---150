# Be mindful of the while loop while temp is not None: -> means temp will be null at the end of the list
# if while temp.next is not None: means that it will be in the last node, for loop in range(len(list)-1) also
# means it will be in the last index
# Cases to consider while inserting/deleting
# Case 1: inserting/deleting at front, length = 1
# Case 2: inserting/deletingg at front, length > 1
# Case 3: inserting/deleting at last
# Case 4: General case - in the middle
class ListNode:
    #NOTHING CAN BE CHANGED HERE
    def __init__(self, val = 0, next= None):
        self.val = val
        self.next = next
                
############################################################
#  class  Slist
###########################################################   
class Slist():
    def __init__(self):
        #NOTHING CAN BE CHANGED HERE
        self._first = None
        self._last = None
        self._len = 0 
        
    #############################
    # WRITE All public functions BELOW
    # YOU CAN HAVE ANY NUMBER OF PRIVATE FUNCTIONS YOU WANT
    #############################
    def append(self, val):
        new_node = ListNode(val)
        head = self
        if head._first is None:
            head._first = new_node
            head._last = new_node
            head._len += 1
        else:
            temp = head._last
            temp.next = new_node
            head._last = new_node
            head._len += 1
    
    def prepend(self, val):
        new_node = ListNode(val)
        head = self
        if head._first is None:
            head._first = new_node
            head._last = new_node
            head._len += 1
        else:
            tmp = head._first
            head._first = new_node
            new_node.next = tmp
            head._len += 1
    
    def insert(self, value, index):
        new_node = ListNode(value)
        head = self
        if head._len < index:
            print("index to insert must be smaller than length of the list")
        else:
            if head._first is None:
                head._first = new_node
                head._last = new_node
                head._len += 1
            else:
                if index == 0:
                    self.prepend(value)
                    return
                
                temp = head._first

                for i in range(index-1):
                    temp = temp.next
                
                if temp.next is not None:
                    temp2 = temp.next
                    temp.next = new_node
                    new_node.next = temp2
                    head._len += 1
                else:
                    self.append(value)
    
    def delete(self, index):
        head = self

        if head._len <= index:
            print("index to delete must be less than length(0 to n-1)")
            return -1
        
        if head._first is None:
            print("List is empty!!")
            return -1
            
        temp = head._first
        value = temp.val
        # if the value to delete is the first node and len = 1
        if index == 0 and head._len == 1:
            head._first = None
            head._last = None
            head._len -= 1
            return value
        
        # if the value to delete is the first node and len > 1
        if index == 0 and head._len > 1:
            node_after = head._first.next
            head._first = node_after
            temp.next = None
            head._len -= 1
            return value
        
        for i in range(index - 1):
            temp = temp.next

        value = temp.val

        # if the value to delete is the last node   
        if index == head._len - 1:
            temp.next = None
            head._last = temp
            head._len -= 1
        else:
            # General case
            node_after = temp.next
            temp2 = temp.next.next
            temp.next = temp2
            node_after.next = None
            head._len -= 1
        return value
    
    def find(self,value):
        head = self
        if head._first is None:
            print("List is empty!!")
            return -1
        temp = head._first
        for i in range(head._len):
            if value == temp.val:
                return i
            temp = temp.next
        return -1
    
    def findNode(self, value):
        head = self
        if head._first is None:
            print("List is empty!!")
            return None, None
        
        temp = head._first

        if temp.val == value:
            return None, temp
        
        for i in range(head._len-1):
            if temp.next.val == value:
                return temp, temp.next
            temp = temp.next
    
        return None, None
 
    def deleteFromValue(self,value):
        head = self
        if head._first is None:
            print("List is empty!!")
            return
    
        node_prev, node = self.findNode(value)

        if node_prev is None and node is None:
            print("value not found")
            return
        
        # if the value to delete is the last node
        if node.next is None and node_prev is not None:
            node_prev.next = None
            head._last = node_prev
            head._len -= 1
            return
    
        # if the value to delete is the first node and len = 1
        if node_prev is None and head._len == 1:
            head._first = None
            head._last = None
            head._len -= 1
            return

        # if the value to delete is the first node and len > 1
        if node_prev is None and head._len > 1:
            node_after = node.next
            head._first = node_after
            node.next = None
            head._len -= 1
            return
        
        # General case
        node_after = node.next
        node_prev.next = node_after
        node.next = None
        head._len -= 1
        return

def test_append(list):
    for i in range(5):
        list.append(i+1)
    return list

def test_prepend(list):
    for i in range(10):
        list.prepend(100*(i+1))
    return list

def print_list(list):
    temp = list._first
    while temp is not None:
        print(temp.val, end = "")
        if temp.next is not None:
            print("->", end="")
        temp = temp.next

# Linked list(Not slist)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
    
    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            self.head = new_node
            new_node.next = temp

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="")
            if temp.next:
                print("->", end="")
            temp = temp.next
        
# Call the test function
if __name__ == "__main__":
    # list = Slist()
    # test_append(list)
    # test_prepend(list)
    # print_list(list)

    # Example usage
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.prepend(4)
    ll.display()  # Output: 1 -> 2 -> 3 -> None